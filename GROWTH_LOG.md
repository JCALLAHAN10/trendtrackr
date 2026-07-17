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
