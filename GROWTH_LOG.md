# TrendTrackr Growth Log

## 2026-07-17 — Launch

**Pivot rationale:** Jack decided to retire the SetupRig/PetTrackr niche-site model (both are still live on GitHub Pages, GSC-verified, but no further active work) and replace it with a single new project: TikTok-viral products, verified against real Amazon data before being recommended. Jack supplied the seed data himself — a live pull of Amazon's Kitchen & Dining Best Sellers page (real ASINs, ratings, prices), which is a stronger verification source than a web search summary would be.

**Site built:** New repo `JCALLAHAN10/trendtrackr`, GitHub Pages site, new theme (coral/teal on near-black, Poppins font) distinct from both prior sites. Associates tag: jcallahan1542-20.

**Launch article:** `best-viral-water-bottles-tumblers.html` — Owala FreeSip 24oz (#1 Best Seller, 4.7★/130k), Stanley Quencher H2.0 30oz (#2 Best Seller, 4.7★/201k — the tumbler that originally started this trend), HydroJug Traveler 32oz (#3 Best Seller, 4.6★/19k). All three sourced directly from the live Best Sellers page Jack shared, with real amazon.com/dp/ links. Rather than the `/s?k=` search-link pattern used on the old sites, this site uses direct product `/dp/<ASIN>` links since we have confirmed real ASINs — cleaner and more likely to convert.

**Deliberately not included:** Etekcity Food Scale (#4 on the same Best Sellers page) — it's a real, verified best-seller too, but it doesn't fit the "TikTok-viral" framing of this first article (it's a generic kitchen bestseller, not a social-trend item) and there weren't enough similar-fit products yet to build it into its own guide. Holding it for a future "trending kitchen gadgets" article once more verified candidates are gathered.

**Verification approach going forward:** Given WebSearch hit a session-wide rate limit today (mid-run on the old sites' final actions), this launch leaned entirely on user-supplied live Amazon data rather than search-based product discovery. This is actually a stronger verification standard than search summaries — real ASINs/ratings straight from Amazon's own Best Sellers rankings. Future articles should keep using this pattern: pull directly from Amazon Best Sellers/New Releases pages for a category, cross-reference with genuine TikTok virality (not just "trending" claims), and only ship picks with real, current Amazon listings.

**Search Console — done same day, not deferred this time:** Registered `https://jcallahan10.github.io/trendtrackr/` as a URL-prefix property, verified via the same account-level HTML meta tag used on SetupRig/PetTrackr, confirmed live in the rendered DOM, then verified in Search Console. Submitted `sitemap.xml` — status starts as "Couldn't fetch" until Google's first crawl pass, which is normal. Unlike the old sites (where this was added weeks late), TrendTrackr launches with indexing infrastructure in place from day one.

**Not yet done:** Amazon Associates click tracking (site is brand new, expect 0 clicks initially — same discovery-problem pattern seen on SetupRig/PetTrackr, this isn't a signal of a problem yet, just too early to have data).

**Next priority:** Get 2-3 more launch articles built from real Amazon Best Sellers data across different categories (beauty/skincare, tech accessories, home organization are all categories with well-documented TikTok-to-Amazon crossover) — Jack can paste more live Best Sellers pages the same way he did for Kitchen & Dining, which is proving to be a faster and more reliable verification path than web search right now.

## 2026-07-17 — Repo cleanup + click tracking instrumentation

**Repo cleanup executed:** Jack confirmed the pivot noted above should actually happen at the account level, not just in narrative — `pettrackr` and `setuprig` were deleted from GitHub entirely so TrendTrackr is the only active project. This was done deliberately (not by accident): both were still live/GSC-verified per the note above, but Jack was explicit he wants a single focused site rather than three, and neither of the retired niches (pets, gaming/desk setups) matches the "viral trending products" direction he wants to grow.

**Click tracking finally added:** The "Not yet done" item from launch day is done. GA4 (`gtag.js`) and a Pinterest tag are wired into both `index.html` and the water bottles article, both currently pointed at placeholder IDs (`G-XXXXXXXXXX` / `PINTEREST_TAG_ID_PLACEHOLDER`) — swap these for real IDs before trusting the numbers. Every Amazon affiliate link now fires a `affiliate_click` event with a `link_label` parameter unique to that product and placement (e.g. `owala_title`, `owala_button`), which is what lets per-product CTR actually be measured instead of guessed at. Scroll-depth tracking was added site-wide in 25% increments.

**Homepage card upgraded:** Added a real, truthful ratings/best-seller-count line to the water bottles card on the homepage (data pulled directly from the article, nothing fabricated) and made the card title itself a second click-through entry point to the article, alongside the existing "Read the guide" button.

**Pinterest save button added:** A "Save this guide to Pinterest" link was added to the article, since Pinterest is the intended free-traffic channel for this project. It shares the article URL directly; there's no dedicated Open Graph image yet, so Pinterest will fall back to whatever it can find on the page — a real product lifestyle image per article would meaningfully improve how these pins look once added.

**Deliberately not added:** No fake urgency/scarcity copy ("selling out fast," countdown timers) and no fabricated discount percentages. TrendTrackr's whole positioning is "verified, not hype" — adding manufactured urgency would directly contradict the trust angle that differentiates this site from typical TikTok-finds listicles, so those competitor patterns were left out on purpose rather than missed.

**Next priority (still open from before):** 2-3 more launch articles from real Amazon Best Sellers data in new categories, plus swapping the GA4/Pinterest placeholder IDs for real ones as soon as those accounts exist so click data actually starts flowing.

## 2026-07-17 — Real GA4 property created, bug found and fixed in the CRO script

**GA4 property created for real:** Jack asked to set things up for success, so rather than leave the GA4 tag as a placeholder, a real property was created directly (account "TrendTrackr", property "TrendTrackr", US/Los Angeles timezone, USD currency, Shopping industry, data-sharing settings left off except what's strictly required). Measurement ID **G-QZNTTBBY76** replaced the `G-XXXXXXXXXX` placeholder in both `index.html` and the article. The Pinterest tag is still a placeholder — no Pinterest business account exists yet to get a real tag ID from.

**Custom dimension registered:** Created an event-scoped custom dimension "Link Label" mapped to the `link_label` event parameter (GA4 property 545982473). Without this, `click_optimizer_agent.py`'s GA4 Data API queries against `customEvent:link_label` would silently return nothing.

**Bug found and fixed in click_optimizer_agent.py:** The scroll-depth query was written to look for a `customEvent:percent_scrolled` dimension that the site never actually sends — `ttTrack()` reuses the same `link_label` parameter for every event type (affiliate_click, article_click, scroll_depth, share_click), so there's no separate `percent_scrolled` parameter to query. Also, the per-product CTR query wasn't filtered by event name at all, which would have mixed clicks, scrolls, and shares together under one flat `link_label` breakdown. Both queries now filter on `eventName` explicitly (`affiliate_click` for CTR, `scroll_depth` for scroll depth) before grouping by `link_label`. This was caught and fixed before the script was ever run against real data, so no bad numbers went anywhere.

**What's still needed before click_optimizer_agent.py can actually run:**
1. A GCP service account with "Viewer" access on GA4 property `properties/545982473`, and its JSON key saved somewhere the script can read (`GA4_CREDENTIALS_JSON`). Not created yet — this involves generating a downloadable credential file, which needs to happen with Jack directly rather than unattended.
2. Jack's own `ANTHROPIC_API_KEY` (tied to his own Claude billing — has to come from him).
3. Real site traffic — the site is brand new, so even once wired up, `MIN_SESSIONS_FOR_CONFIDENCE` (200 sessions/week) won't be met for a while, and the script will correctly no-op until then.
4. A real Pinterest tag ID, once a Pinterest business account exists (still just a placeholder).

## 2026-07-17 — GSC indexing check, TikTok research applied, real OG/Pinterest images added

**Search Console checked:** The homepage (`https://jcallahan10.github.io/trendtrackr/`) is already indexed and confirmed live on Google ("URL is on Google"). The article page (`articles/best-viral-water-bottles-tumblers.html`) was not yet indexed — used the URL Inspection tool to request priority crawling for it. Google's own guidance is that resubmitting doesn't change queue position, so this is a one-time ask; indexing itself can still take hours to days.

**Jack shared 2 TikTok videos for analysis — one applicable, one not:**
1. `@callmekevy` — a tutorial on Amazon-affiliate-via-Pinterest for beginners. This directly validates the site's existing strategy (Pinterest traffic → Amazon Associates links) and the caption's own steps map cleanly onto gaps we had: design eye-catching branded pins for each guide, embed a direct pin image (not just a bare link) so pins render properly in Pinterest's feed, and post consistently rather than one-off. Applied below.
2. `@operation.ecom` — a retail-arbitrage tutorial (buying clearance/wholesale goods to resell as an Amazon *seller*, using tools like SellerAmp and Boxem). This is a fundamentally different business model from TrendTrackr (Amazon *selling*, not *affiliate marketing*) and doesn't apply here — noted honestly rather than forced in, per the "verified, not hype" standard applied to our own research too.

**Real OG/Pinterest images built and wired up:** The site had no image assets at all — GROWTH_LOG previously flagged that the Pinterest save button had no dedicated image to share, so Pinterest was falling back to nothing. Built two original, on-brand graphics (coral/teal/near-black, Poppins — matching `css/style.css`, no Amazon or manufacturer product photography used, to stay clear of image licensing issues): `images/og-water-bottles.png` (1200×630 Open Graph/Twitter card image) and `images/pin-water-bottles.png` (1000×1250 vertical Pinterest pin graphic, listing all 3 verified picks with their real ratings and a CTA). Wired `og:image`/`twitter:image` meta tags into both `index.html` and the article, and updated the Pinterest share link to pass `media=` pointing directly at the new pin graphic, so pins now render with a real, branded image instead of nothing.

**Still open:** everything listed above (GA4 service account, Jack's own Anthropic API key, real traffic, real Pinterest tag) plus actually posting the new pin to a live Pinterest account — that still needs Jack's Pinterest login/account to exist before anything can be posted there.

**Jack transcribed the full `@callmekevy` video by hand — one more actionable point surfaced:** the creator specifically calls out Pinterest SEO as something that can "quietly stop your growth" if ignored, separate from just posting consistently. Tightened the pin share description to front-load real search terms (`TikTok Viral Water Bottles 2026: Owala FreeSip vs Stanley Quencher vs HydroJug Traveler...`) instead of a generic sentence, since Pinterest's own ranking leans on keyword-rich titles/descriptions rather than hashtags.

**Pinterest launch checklist — ready to execute the moment an account exists (no account exists yet, confirmed by checking pinterest.com in-browser):**
1. Business account (not personal) — gives access to analytics and the real conversion tag.
2. Profile bio/username optimized with core niche keywords ("TikTok-viral Amazon finds," "verified best sellers") — Pinterest indexes profile keywords, not just pin text.
3. A board structure organized by product category (e.g., "Water Bottles & Tumblers," future boards per new article category), each with a keyword-rich board title/description, not generic names.
4. Pin the `pin-water-bottles.png` graphic already built, using the keyword-front-loaded description already wired into the article's share link.
5. Consistent posting cadence going forward (daily/near-daily, per the tutorial) once there's more than one pin-worthy asset — batching all pinning into one day and going quiet is exactly what the "quietly stop your growth" warning is about.
6. Swap the real Pinterest tag ID into `index.html`/article `pintrk('load', ...)` calls once the business account exists, replacing the current placeholder.

## 2026-07-17 — Pinterest live: account set up + first pin published

Jack created a Pinterest **Business** account (username `jcallahan154`, display name TrendTrackr) and handed over the browser to finish setup. Executed the launch checklist above, minus what's still gated:

**Done:**
- **Profile aligned to the site's positioning** — bio set to "TikTok-viral products, verified against real Amazon Best Seller data before we ever recommend them. Verified, not hype. New picks added regularly." (Jack explicitly confirmed the direction: best-sellers / kitchen / hydration, not the fashion/dupes angle a namesake account at the `trendtrackr` handle happens to use — that's a different person, not Jack's account.)
- **First board created:** "Water Bottles & Tumblers" (public, keyword-named for Pinterest SEO rather than a generic label).
- **First pin PUBLISHED and confirmed live** on the profile's Created tab: the `pin-water-bottles.png` graphic, titled "TikTok-Viral Water Bottles & Tumblers (2026): Owala vs Stanley vs HydroJug," keyword-rich description, linking directly to the live article (`.../articles/best-viral-water-bottles-tumblers.html`). This is the first real, free traffic path into the site — independent of the pending GitHub push, because the article page itself is already live.
- Uploaded the pin image directly (the generated PNG staged to `/mnt/user-data/outputs/` so the Chrome uploader could read it), so posting did NOT require the site update to be pushed first.

**Notably NOT done (deliberately):** Did not click through the multi-step "Describe your business" onboarding wizard Pinterest nudged — it's an unknown-length flow that may ask for more account/ad details, and it's not needed to post pins. Left for Jack to complete if/when he wants.

**Still gated on the GitHub push (5 commits stacked locally, unpushed — token still needed):**
- The Pinterest **website claim** (entered the URL + added the `p:domain_verify` meta tag to the repo, but it can't verify until that tag is live on the site) — needed for pin attribution + Pinterest analytics.
- The real Pinterest conversion **tag ID** still a placeholder in the site's `pintrk('load', ...)`.
- The OG/preview images + SEO meta + GA4 fix from the earlier commits.

**Next lever for traffic:** more pins. One live article = one pin so far. Per the "post consistently" advice, the highest-value next step is 2–3 more verified articles (new Best Seller categories) → each becomes its own pin + board. That, plus getting the push through, is the path to compounding Pinterest traffic.
