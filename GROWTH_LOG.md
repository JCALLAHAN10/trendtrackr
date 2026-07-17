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
