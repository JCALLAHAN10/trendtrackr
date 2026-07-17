"""
click_optimizer_agent.py

Autonomous CRO subagent for TrendTrackr (jcallahan10.github.io/trendtrackr) —
the verified-TikTok-viral-products-via-Amazon-affiliate-links site, repo
JCALLAHAN10/trendtrackr, Associates tag jcallahan1542-20.

WHAT IT DOES
------------
On a schedule (cron, or the built-in loop at the bottom), this script:
  1. Pulls real performance data — GA4 engagement metrics, per-product click-through
     rates (via the `link_label` GA4 custom event parameter already wired into
     index.html and every article page), and Pinterest referral performance.
  2. Packages that data + every page's current HTML into a single prompt.
  3. Calls the Claude API with a system prompt that forces structured, scoped,
     testable layout-change recommendations (JSON, not prose) — and that
     explicitly forbids fake urgency/scarcity, because TrendTrackr's whole
     positioning is "verified, not hype."
  4. Auto-applies only the low-risk/high-confidence changes directly to the
     relevant HTML file; everything else is queued to review_queue.json for
     a human sign-off.
  5. Logs every run (in the same GROWTH_LOG.md style the site already uses)
     so you can see what changed and why, and compare snapshots over time.

REQUIRED SETUP
--------------
  pip install anthropic google-analytics-data requests

Environment variables (all required unless noted):
  ANTHROPIC_API_KEY          Your Claude API key (from console.anthropic.com — this
                             is tied to your own billing, so it has to come from you).
  GA4_PROPERTY_ID            "properties/545982473" — this is TrendTrackr's real GA4
                             property (created 2026-07-17, Measurement ID G-QZNTTBBY76,
                             already live in index.html and the article). The
                             `link_label` custom dimension this script queries is
                             already registered in that property's Custom definitions.
  GA4_CREDENTIALS_JSON       Path to a GCP service-account JSON key with "Viewer"
                             access on the GA4 property above. Not yet created — see
                             GROWTH_LOG.md for the 4 remaining steps to generate one.
  PINTEREST_ACCESS_TOKEN     Pinterest API access token (optional — if unset,
                             Pinterest metrics are skipped and noted as such).
  PINTEREST_AD_ACCOUNT_ID    Pinterest ad account ID (optional, same as above).
  SITE_ROOT                  Path to a local clone of JCALLAHAN10/trendtrackr
                             (defaults to "./trendtrackr"). The script walks
                             index.html plus every articles/*.html file.

This script assumes every page already fires the `ttTrack()` calls wired into
index.html and the articles (GA4 `gtag('event', ...)` with a `link_label`
parameter for every affiliate click, plus `scroll_depth` events). Those become
the custom dimension this script queries for per-product CTR.
"""

import os
import re
import json
import glob
import time
import logging
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta

import requests
from anthropic import Anthropic

# Optional import — only needed if you're pulling live GA4 data.
try:
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import (
        RunReportRequest, Dimension, Metric, DateRange, FilterExpression, Filter,
    )
    GA4_AVAILABLE = True
except ImportError:
    GA4_AVAILABLE = False


def _event_name_filter(event_name):
    """Build a GA4 dimension filter restricting a report to a single event name.

    Necessary because every event type on this site (affiliate_click,
    article_click, share_click, scroll_depth) reuses the same `link_label`
    event parameter for its value — see ttTrack() in index.html/articles/*.html.
    Without this filter, a report grouped by customEvent:link_label mixes
    product clicks, scroll-depth percentages, and share clicks together.
    """
    return FilterExpression(
        filter=Filter(field_name="eventName", string_filter=Filter.StringFilter(value=event_name))
    )

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("click_optimizer_agent")

# --------------------------------------------------------------------------
# CONFIG
# --------------------------------------------------------------------------

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
GA4_PROPERTY_ID = os.environ.get("GA4_PROPERTY_ID")
GA4_CREDENTIALS_JSON = os.environ.get("GA4_CREDENTIALS_JSON")
PINTEREST_ACCESS_TOKEN = os.environ.get("PINTEREST_ACCESS_TOKEN")
PINTEREST_AD_ACCOUNT_ID = os.environ.get("PINTEREST_AD_ACCOUNT_ID")
SITE_ROOT = os.environ.get("SITE_ROOT", "./trendtrackr")

RUN_INTERVAL_HOURS = 24        # how often the loop at the bottom fires
LOOKBACK_DAYS = 7              # rolling window for all metrics pulls
MIN_SESSIONS_FOR_CONFIDENCE = 200  # don't act on noise below this sample size

REVIEW_QUEUE_PATH = "review_queue.json"
RUN_HISTORY_PATH = "run_history.jsonl"

CLAUDE_MODEL = "claude-sonnet-4-5"

# --------------------------------------------------------------------------
# SYSTEM PROMPT
# --------------------------------------------------------------------------
# This is the exact system prompt the subagent uses. Keep it narrow and
# structured — the whole point of this agent is that it proposes small,
# testable, reversible changes, not full redesigns.

SYSTEM_PROMPT = """You are a conversion-rate-optimization (CRO) subagent for TrendTrackr, a site
that recommends TikTok-viral products only after verifying them against real
Amazon Best Sellers data (real ASINs, real ratings, real rank) rather than
just social buzz. That "verified, not hype" positioning is the site's entire
differentiator, and it is a hard constraint on every recommendation you make,
not just a style note. Traffic arrives mostly on mobile, via Pinterest and
organic search. Your one job is to look at real engagement data and the
current page HTML, then propose a small set of concrete, testable layout/copy
changes that should increase click-through rate on affiliate links without
increasing bounce rate and without undermining the verified/trustworthy tone.

Hard rules:
1. Every recommendation must name the exact page it applies to (the file path
   as given in the input, e.g. index.html vs articles/some-article.html) and
   reference a specific HTML element (by its class, id, or a short unique
   text excerpt) that exists in that page's markup. Never propose changes to
   elements that aren't in the provided markup, and never point a change at
   the wrong page.
2. Every recommendation must be small and reversible: a copy tweak, a badge
   addition, a reordering, a color/contrast change, a CTA repositioning. Do
   NOT propose full redesigns, new pages, or structural rewrites.
3. Every recommendation must state the specific data point that motivated it
   (e.g. "product #3 has a 1.8% CTR vs a 6.1% site average, and its card is
   the only one without a rating badge").
4. Assign each recommendation a risk_level of "low", "medium", or "high".
   - "low" = pure copy/badge/styling change, no layout restructure, easily reverted.
   - "medium" = reordering existing elements or changing CTA placement.
   - "high" = anything touching tracking code, links, or page structure.
5. Assign a confidence score 0.0-1.0 based on how strong the supporting data is.
   Do not exceed 0.6 confidence if the underlying sample size is small or the
   metric is a single-session anomaly.
6. Output ONLY through the provided structured tool call. Do not add
   conversational text outside the tool call.
7. If the data doesn't support any confident recommendation this cycle, return
   an empty recommendations array rather than inventing changes to justify your
   existence.
8. Never recommend anything that would mislead a user (fake scarcity/fake
   review counts/manipulated numbers, "selling out fast" language that isn't
   backed by real inventory data). Recommendations must only reposition,
   restyle, or reword TRUTHFUL information already present in the data or the
   HTML (real ratings, real Best Sellers rank, real review counts). If you
   want to suggest urgency, it must be tied to something real and verifiable
   (e.g. "newest pick, climbing the Best Sellers list fast" is fine because
   it's already in the copy and is true; "only 3 left in stock" is not fine
   unless that figure is actually present in the input data).
"""

RECOMMENDATION_TOOL = {
    "name": "submit_cro_recommendations",
    "description": "Submit structured landing-page optimization recommendations.",
    "input_schema": {
        "type": "object",
        "properties": {
            "summary": {
                "type": "string",
                "description": "One-paragraph plain-English summary of this cycle's findings.",
            },
            "recommendations": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "target_page": {
                            "type": "string",
                            "description": "Relative file path of the page this change applies to, exactly as given in the input (e.g. 'index.html' or 'articles/best-viral-water-bottles-tumblers.html').",
                        },
                        "target_selector": {
                            "type": "string",
                            "description": "CSS selector or unique text excerpt identifying the element to change.",
                        },
                        "current_state": {
                            "type": "string",
                            "description": "What the element currently looks like / says.",
                        },
                        "proposed_change": {
                            "type": "string",
                            "description": "The exact new copy, attribute, or ordering to apply.",
                        },
                        "supporting_metric": {
                            "type": "string",
                            "description": "The specific data point justifying this change.",
                        },
                        "expected_impact": {
                            "type": "string",
                            "description": "What metric should move, and roughly how much.",
                        },
                        "risk_level": {
                            "type": "string",
                            "enum": ["low", "medium", "high"],
                        },
                        "confidence": {
                            "type": "number",
                            "minimum": 0,
                            "maximum": 1,
                        },
                    },
                    "required": [
                        "target_page", "target_selector", "current_state", "proposed_change",
                        "supporting_metric", "expected_impact", "risk_level", "confidence",
                    ],
                },
            },
        },
        "required": ["summary", "recommendations"],
    },
}

# --------------------------------------------------------------------------
# DATA MODEL
# --------------------------------------------------------------------------

@dataclass
class PerformanceSnapshot:
    window_start: str
    window_end: str
    sessions: int = 0
    bounce_rate: float = 0.0
    avg_engagement_seconds: float = 0.0
    scroll_depth_p50: float = 0.0
    product_ctr: dict = field(default_factory=dict)   # {"product_1_button": 0.041, ...}
    site_avg_ctr: float = 0.0
    pinterest_impressions: int = 0
    pinterest_ctr: float = 0.0
    pinterest_available: bool = False


# --------------------------------------------------------------------------
# STEP 1 — DATA INPUTS
# --------------------------------------------------------------------------

def fetch_ga4_snapshot() -> PerformanceSnapshot:
    """Pull bounce rate, engagement time, scroll depth, and per-link CTR from GA4.

    Per-product CTR comes from the `link_label` event parameter fired by the
    site's track() function (see index.html) on every `affiliate_click` event,
    joined against total sessions for the same window.
    """
    end = datetime.utcnow().date()
    start = end - timedelta(days=LOOKBACK_DAYS)
    snapshot = PerformanceSnapshot(window_start=str(start), window_end=str(end))

    if not GA4_AVAILABLE or not GA4_PROPERTY_ID or not GA4_CREDENTIALS_JSON:
        log.warning("GA4 not configured — skipping live pull, returning zeroed snapshot.")
        return snapshot

    os.environ.setdefault("GOOGLE_APPLICATION_CREDENTIALS", GA4_CREDENTIALS_JSON)
    client = BetaAnalyticsDataClient()

    # Site-level engagement metrics.
    overview_request = RunReportRequest(
        property=GA4_PROPERTY_ID,
        dimensions=[],
        metrics=[
            Metric(name="sessions"),
            Metric(name="bounceRate"),
            Metric(name="averageSessionDuration"),
        ],
        date_ranges=[DateRange(start_date=str(start), end_date=str(end))],
    )
    overview = client.run_report(overview_request)
    if overview.rows:
        row = overview.rows[0]
        snapshot.sessions = int(float(row.metric_values[0].value))
        snapshot.bounce_rate = float(row.metric_values[1].value)
        snapshot.avg_engagement_seconds = float(row.metric_values[2].value)

    # Per-link CTR, broken out by the custom `link_label` event parameter —
    # filtered to affiliate_click specifically, since that's the revenue-relevant
    # metric and the same parameter name is reused by other event types.
    ctr_request = RunReportRequest(
        property=GA4_PROPERTY_ID,
        dimensions=[Dimension(name="customEvent:link_label")],
        metrics=[Metric(name="eventCount")],
        date_ranges=[DateRange(start_date=str(start), end_date=str(end))],
        dimension_filter=_event_name_filter("affiliate_click"),
    )
    ctr_response = client.run_report(ctr_request)
    clicks_by_label = {
        row.dimension_values[0].value: int(row.metric_values[0].value)
        for row in ctr_response.rows
        if row.dimension_values[0].value
    }
    if snapshot.sessions:
        snapshot.product_ctr = {
            label: round(count / snapshot.sessions, 4)
            for label, count in clicks_by_label.items()
        }
        if snapshot.product_ctr:
            snapshot.site_avg_ctr = round(
                sum(snapshot.product_ctr.values()) / len(snapshot.product_ctr), 4
            )

    # Median scroll depth from the `scroll_depth` custom event — same
    # `link_label` parameter, filtered to this event name, holding values
    # like "25%", "50%", etc.
    scroll_request = RunReportRequest(
        property=GA4_PROPERTY_ID,
        dimensions=[Dimension(name="customEvent:link_label")],
        metrics=[Metric(name="eventCount")],
        date_ranges=[DateRange(start_date=str(start), end_date=str(end))],
        dimension_filter=_event_name_filter("scroll_depth"),
    )
    scroll_response = client.run_report(scroll_request)
    depths = []
    for row in scroll_response.rows:
        try:
            pct = int(row.dimension_values[0].value.replace("%", ""))
            depths.extend([pct] * int(row.metric_values[0].value))
        except (ValueError, AttributeError):
            continue
    if depths:
        depths.sort()
        snapshot.scroll_depth_p50 = depths[len(depths) // 2]

    return snapshot


def fetch_pinterest_snapshot(snapshot: PerformanceSnapshot) -> PerformanceSnapshot:
    """Pull impressions/CTR for the Pinterest referral channel, if configured."""
    if not PINTEREST_ACCESS_TOKEN or not PINTEREST_AD_ACCOUNT_ID:
        log.info("Pinterest API not configured — skipping (organic-only Pinterest traffic still shows up in GA4 as a referral source).")
        return snapshot

    url = f"https://api.pinterest.com/v5/ad_accounts/{PINTEREST_AD_ACCOUNT_ID}/analytics"
    end = datetime.utcnow().date()
    start = end - timedelta(days=LOOKBACK_DAYS)
    params = {
        "start_date": str(start),
        "end_date": str(end),
        "columns": "IMPRESSION_2,CLICKTHROUGH_2",
        "granularity": "TOTAL",
    }
    headers = {"Authorization": f"Bearer {PINTEREST_ACCESS_TOKEN}"}

    try:
        resp = requests.get(url, params=params, headers=headers, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        if data:
            row = data[0] if isinstance(data, list) else data
            impressions = row.get("IMPRESSION_2", 0)
            clicks = row.get("CLICKTHROUGH_2", 0)
            snapshot.pinterest_impressions = impressions
            snapshot.pinterest_ctr = round(clicks / impressions, 4) if impressions else 0.0
            snapshot.pinterest_available = True
    except requests.RequestException as e:
        log.warning(f"Pinterest API call failed: {e}")

    return snapshot


def build_snapshot() -> PerformanceSnapshot:
    snapshot = fetch_ga4_snapshot()
    snapshot = fetch_pinterest_snapshot(snapshot)
    return snapshot


# --------------------------------------------------------------------------
# STEP 2 — CALL CLAUDE
# --------------------------------------------------------------------------

def get_site_pages() -> dict:
    """Return {relative_path: html_content} for index.html + every article page."""
    pages = {}
    index_path = os.path.join(SITE_ROOT, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            pages["index.html"] = f.read()
    for path in sorted(glob.glob(os.path.join(SITE_ROOT, "articles", "*.html"))):
        rel = os.path.relpath(path, SITE_ROOT)
        with open(path, "r", encoding="utf-8") as f:
            pages[rel] = f.read()
    if not pages:
        raise FileNotFoundError(
            f"No HTML pages found under SITE_ROOT={SITE_ROOT!r} — check the path to your trendtrackr clone."
        )
    return pages


def build_user_message(snapshot: PerformanceSnapshot, pages: dict) -> str:
    pages_block = "\n\n".join(
        f"### {path}\n```html\n{html}\n```" for path, html in pages.items()
    )
    return f"""Here is the current performance data (rolling {LOOKBACK_DAYS}-day window):

{json.dumps(asdict(snapshot), indent=2)}

Minimum sample size for confident action: {MIN_SESSIONS_FOR_CONFIDENCE} sessions.
Current session count: {snapshot.sessions}.

Here are every page's current HTML, each labeled with its relative path —
use that exact path as target_page in your recommendations:

{pages_block}

Review the data against the HTML and submit your recommendations via the
submit_cro_recommendations tool. If sessions are below the minimum sample
size, either return no recommendations or clearly cap every confidence score
at 0.4 or below."""


def call_claude(snapshot: PerformanceSnapshot, pages: dict) -> dict:
    client = Anthropic(api_key=ANTHROPIC_API_KEY)
    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        tools=[RECOMMENDATION_TOOL],
        tool_choice={"type": "tool", "name": "submit_cro_recommendations"},
        messages=[{"role": "user", "content": build_user_message(snapshot, pages)}],
    )
    for block in response.content:
        if block.type == "tool_use" and block.name == "submit_cro_recommendations":
            return block.input
    raise RuntimeError("Claude did not return a tool_use block — check model/tool config.")


# --------------------------------------------------------------------------
# STEP 3 — APPLY OR QUEUE RECOMMENDATIONS
# --------------------------------------------------------------------------

def apply_low_risk_change(html: str, rec: dict) -> tuple:
    """Best-effort direct text substitution for low-risk copy/badge changes.

    Returns (new_html, applied: bool). Falls back to queuing if the current
    text can't be located verbatim in the HTML (safer than guessing).
    """
    current = rec["current_state"].strip()
    proposed = rec["proposed_change"].strip()
    if current and current in html:
        return html.replace(current, proposed, 1), True
    return html, False


def process_recommendations(result: dict, pages: dict) -> None:
    applied, queued = [], []
    dirty_pages = set()

    for rec in result.get("recommendations", []):
        target_page = rec.get("target_page")
        is_auto_eligible = (
            rec["risk_level"] == "low"
            and rec["confidence"] >= 0.65
            and target_page in pages
        )
        if is_auto_eligible:
            new_html, ok = apply_low_risk_change(pages[target_page], rec)
            if ok:
                pages[target_page] = new_html
                dirty_pages.add(target_page)
                applied.append(rec)
            else:
                queued.append(rec)
        else:
            queued.append(rec)

    for target_page in dirty_pages:
        full_path = os.path.join(SITE_ROOT, target_page)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(pages[target_page])
    if applied:
        log.info(f"Auto-applied {len(applied)} low-risk change(s) across {len(dirty_pages)} page(s) under {SITE_ROOT}.")

    if queued:
        existing = []
        if os.path.exists(REVIEW_QUEUE_PATH):
            with open(REVIEW_QUEUE_PATH, "r", encoding="utf-8") as f:
                existing = json.load(f)
        existing.extend(queued)
        with open(REVIEW_QUEUE_PATH, "w", encoding="utf-8") as f:
            json.dump(existing, f, indent=2)
        log.info(f"Queued {len(queued)} change(s) for human review in {REVIEW_QUEUE_PATH}.")

    with open(RUN_HISTORY_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "timestamp": datetime.utcnow().isoformat(),
            "summary": result.get("summary", ""),
            "applied_count": len(applied),
            "queued_count": len(queued),
        }) + "\n")


# --------------------------------------------------------------------------
# STEP 4 — THE LOGIC LOOP
# --------------------------------------------------------------------------
#
#   1. Pull a fresh PerformanceSnapshot (GA4 + Pinterest).
#   2. If sessions < MIN_SESSIONS_FOR_CONFIDENCE, log and skip this cycle —
#      don't let the agent act on statistical noise (a brand-new site like
#      trendtrackr will hit this every cycle until real traffic shows up —
#      that's expected, not a bug).
#   3. Read every page's current HTML (index.html + articles/*.html).
#   4. Call Claude with the system prompt + snapshot + all pages, forcing the
#      structured tool_use response with a target_page per recommendation.
#   5. Auto-apply every "low" risk + confidence >= 0.65 recommendation
#      directly to its target page. Queue everything else for human review.
#   6. Log the run (summary, counts) to run_history.jsonl for auditability.
#   7. Sleep until the next cycle (or exit, if run via external cron).
#
def run_once() -> None:
    log.info("Starting optimization cycle...")
    snapshot = build_snapshot()

    if snapshot.sessions and snapshot.sessions < MIN_SESSIONS_FOR_CONFIDENCE:
        log.info(
            f"Only {snapshot.sessions} sessions in the last {LOOKBACK_DAYS}d "
            f"(need {MIN_SESSIONS_FOR_CONFIDENCE}) — skipping this cycle to avoid noisy changes."
        )
        return

    pages = get_site_pages()
    result = call_claude(snapshot, pages)
    log.info(f"Claude summary: {result.get('summary')}")
    process_recommendations(result, pages)
    log.info("Cycle complete.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Autonomous CRO subagent for the landing page.")
    parser.add_argument(
        "--loop", action="store_true",
        help="Run continuously, sleeping RUN_INTERVAL_HOURS between cycles. "
             "Omit this flag to run a single cycle (recommended if you're driving "
             "this from an external cron job instead).",
    )
    args = parser.parse_args()

    if not ANTHROPIC_API_KEY:
        raise SystemExit("ANTHROPIC_API_KEY is not set — export it before running this script.")

    if args.loop:
        while True:
            run_once()
            log.info(f"Sleeping {RUN_INTERVAL_HOURS}h until next cycle.")
            time.sleep(RUN_INTERVAL_HOURS * 3600)
    else:
        run_once()
