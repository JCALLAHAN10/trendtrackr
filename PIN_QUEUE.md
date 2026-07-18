## ⚠️ STAY-HUMAN RULES — HIGHEST PRIORITY (Jack: a bot flag would be CATASTROPHIC)
Researched Pinterest's actual 2026 spam/bot detection. Findings baked in below:
- **Volume:** Jack set the cap at **~5 pins/day account-wide** (2026-07-18). Fresh
  unique pins only. Account was born 2026-07-18, so still keep it calm and spaced —
  the risk is bursty/robotic *behavior*, not the count. Never a sudden spike.
- **🔑 ONE PIN PER DESTINATION URL PER DAY (biggest rule).** Pinterest flags multiple
  pins pointing to the SAME url in a day as spam. Treat the base article URL as the key
  — IGNORE #anchors (article.html#owala == article.html). So each daily run must pick
  QUEUED pins that EACH point to a DIFFERENT article. Never post two pins to the same
  article on the same day. (Space same-URL repins 2–3 days apart.)
- **Fresh pins beat repins.** Every pin we post is a fresh unique image + unique
  description — good, keep it. Never mass-repin the same image to many boards.
- **No bursts.** Space pins across the day, several minutes+ apart minimum; vary the
  time of day run to run. Distributed, not concentrated.
- **Vary everything:** unique keyword-loaded description per pin (identical text = #1
  bot tell), rotate boards/categories, alternate lanes across days.
- **Human Chrome session only**, never an API. Don't rapid-fire logins/follows/saves.
- **On ANY captcha / "unusual activity" / verify screen: STOP, post nothing more,
  flag Jack.** That's the real ban trigger — never push through.

DAILY PICKING RULE (human poster — posting is human-clicked as of 2026-07-18, no
auto-poster): from QUEUED entries, choose up to ~5 whose destination URLs are all
DIFFERENT (one per URL/day). Prefer URLs not pinned in the last 2 days. Open each
save-URL in your logged-in Chrome minutes apart, click Save, verify, mark POSTED.

# PIN_QUEUE.md — ready-to-post Pinterest pins

## POSTING RULES (human poster MUST follow these — Jack's directives; posting is human-clicked, auto-poster retired 2026-07-18)
1. **Cap = ~5 pins/day TOTAL across both lanes** (Jack's call, 2026-07-18 — he
   confirmed 5/day is fine; the number isn't the risk, behavior is). Space them
   out (minutes+ apart, never a burst), vary the time of day, one pin per
   destination URL/day. (This supersedes the earlier "2/day warm-up" note.)
2. **Space them HOURS apart, vary the time daily** (task randomizes start + gaps).
3. **Keyword-load every description (Jack: "use as many tags as possible").**
   Pinterest is search, not a feed — it ranks on keyword-rich text. Every description
   below front-loads the product + MANY adjacent search terms (category, use-case,
   room, occasion, synonyms — e.g. a water bottle also carries "tumbler, hydration,
   gym bottle, cup with straw, aesthetic"). When writing NEW pins, stuff in every
   term a real person might search. More relevant keywords = more surfaces to be found on.
4. **Post method:** open the Save URL in Jack's logged-in Chrome → board-picker dialog
   → click the named board (create it in-dialog if it doesn't exist yet) → confirm the
   "Saved to <board>" screen. Pinterest's /pin-creation-tool/ is broken; ONLY use these save-URLs.
5. After each confirmed save, change that entry's `Status: QUEUED` → `Status: POSTED <date>`
   and commit PIN_QUEUE.md. If fewer than 3 QUEUED remain, note "queue low" in the report.

Posted 2026-07-18 (day one, already live): 6 pins across 3 boards. Queue below drips from 2026-07-19.

---

## Article-level pins

### Tech Accessories guide
- Board: Tech Accessories & Amazon Must-Haves (create in-dialog if missing)
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-tech-accessories.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpin-best-tiktok-viral-tech-accessories.png&description=Best%20TikTok%20Viral%20Tech%20Accessories%202026%20%E2%80%94%20Amazon%20must%20haves%2C%20desk%20setup%20essentials%2C%20phone%20accessories%2C%20AirTag%20tracker%2C%20outlet%20extender%20charging%20station%2C%20budget%20wireless%20earbuds%2C%20noise%20cancelling%20headphones%2C%20cable%20management%2C%20tech%20gadgets%2C%20dorm%20essentials%2C%20cool%20gadgets%2C%20amazon%20finds%20%E2%80%94%20verified%20against%20Amazon%20Electronics%20Best%20Sellers.
- Status: QUEUED

### Kitchen Gadgets guide
- Board: Kitchen Gadgets & Cooking Tools (create in-dialog if missing)
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-kitchen-gadgets.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpin-best-tiktok-viral-kitchen-gadgets.png&description=Best%20TikTok%20Viral%20Kitchen%20Gadgets%202026%20%E2%80%94%20cooking%20tools%2C%20kitchen%20must%20haves%2C%20vegetable%20chopper%2C%20air%20fryer%20accessories%2C%20oil%20sprayer%2C%20meat%20thermometer%2C%20chicken%20shredder%2C%20meal%20prep%20gadgets%2C%20cooking%20hacks%2C%20kitchen%20essentials%2C%20home%20cook%2C%20amazon%20finds%20%E2%80%94%20verified%20against%20Amazon%20Kitchen%20Best%20Sellers.
- Status: QUEUED

---

## Single-product pins (images live at /images/pp-*.png)

### Owala FreeSip
- Board: Water Bottles & Tumblers
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-viral-water-bottles-tumblers.html%23owala&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpp-owala.png&description=Owala%20FreeSip%20water%20bottle%20%E2%80%94%20Amazon%27s%20%231%20best%20selling%20water%20bottle%2C%204.7%20stars%2C%20130k%20ratings.%20Viral%20TikTok%20water%20bottle%2C%20insulated%20tumbler%2C%20gym%20water%20bottle%2C%20cup%20with%20straw%2C%20hydration%2C%20travel%20bottle%2C%20aesthetic%20water%20bottle%2C%20amazon%20finds%20%E2%80%94%20verified%20best%20seller.
- Status: QUEUED

### Stanley Quencher
- Board: Water Bottles & Tumblers
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-viral-water-bottles-tumblers.html%23stanley&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpp-stanley.png&description=Stanley%20Quencher%20H2.0%20tumbler%20%E2%80%94%20201k%20ratings%2C%204.7%20stars%2C%20the%20viral%20cup%20that%20started%20the%20trend.%20Stanley%20cup%2C%20tumbler%20with%20handle%20and%20straw%2C%2030oz%20insulated%20tumbler%2C%20ice%20retention%2C%20aesthetic%20water%20bottle%2C%20gym%2C%20car%20cup%20holder%2C%20amazon%20finds%20%E2%80%94%20verified%20best%20seller.
- Status: QUEUED

### HydroJug Traveler
- Board: Water Bottles & Tumblers
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-viral-water-bottles-tumblers.html%23hydrojug&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpp-hydrojug.png&description=HydroJug%20Traveler%2032oz%20tumbler%20%E2%80%94%204.6%20stars%2C%20the%20biggest%20of%20the%20viral%20water%20bottles.%20Large%20water%20bottle%2C%20insulated%20tumbler%20with%20handle%20and%20straw%2C%20daily%20water%20intake%2C%20hydration%20goals%2C%20gym%20bottle%2C%20aesthetic%2C%20amazon%20finds%20%E2%80%94%20verified%20Amazon%20best%20seller.
- Status: QUEUED

### Vtopmart Drawer Organizers
- Board: Home Organization & Restock Finds
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-home-organization.html%23vtopmart&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpp-vtopmart.png&description=Vtopmart%20clear%20drawer%20organizers%20%E2%80%94%20the%20viral%20restock%20TikTok%20trays%2C%2049k%20ratings.%20Drawer%20organization%2C%20clear%20bins%2C%20pantry%20organization%2C%20makeup%20organizer%2C%20bathroom%20organization%2C%20desk%20organizer%2C%20restock%2C%20aesthetic%20home%2C%20amazon%20finds%20%E2%80%94%20verified%20Amazon%20best%20seller.
- Status: QUEUED

### Velvet Hangers
- Board: Home Organization & Restock Finds
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-home-organization.html%23hangers&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpp-hangers.png&description=Slim%20velvet%20hangers%20%E2%80%94%20Amazon%27s%20%232%20organization%20best%20seller%2C%20234k%20ratings.%20Closet%20organization%2C%20closet%20makeover%2C%20space%20saving%20hangers%2C%20non%20slip%20hangers%2C%20wardrobe%20organization%2C%20aesthetic%20closet%2C%20restock%2C%20amazon%20finds%20%E2%80%94%20verified%20best%20seller.
- Status: QUEUED

### Rubbermaid Brilliance
- Board: Home Organization & Restock Finds
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-home-organization.html%23rubbermaid&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpp-rubbermaid.png&description=Rubbermaid%20Brilliance%20containers%20%E2%80%94%20the%20viral%20fridge%20restock%20containers%2C%2059k%20ratings.%20Food%20storage%20containers%2C%20fridge%20organization%2C%20meal%20prep%2C%20pantry%20organization%2C%20airtight%20containers%2C%20kitchen%20organization%2C%20restock%2C%20amazon%20finds%20%E2%80%94%20verified%20best%20seller.
- Status: QUEUED

### Veken Shower Caddy
- Board: Home Organization & Restock Finds
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-home-organization.html%23veken&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpp-veken.png&description=Veken%20no-drill%20shower%20caddy%20%E2%80%94%20renter%20friendly%20bathroom%20organization%2C%2014k%20ratings.%20Shower%20organization%2C%20bathroom%20storage%2C%20adhesive%20shelf%2C%20no%20drill%2C%20dorm%20essentials%2C%20rental%20apartment%2C%20small%20bathroom%2C%20amazon%20finds%20%E2%80%94%20verified%20best%20seller.
- Status: QUEUED

### Cisily Sink Caddy
- Board: Home Organization & Restock Finds
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-home-organization.html%23cisily&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpp-cisily.png&description=Cisily%20sink%20caddy%20sponge%20holder%20%E2%80%94%20the%20viral%20sink%20station%2C%2013k%20ratings.%20Kitchen%20sink%20organization%2C%20sponge%20holder%2C%20kitchen%20organization%2C%20counter%20organization%2C%20stainless%20steel%2C%20aesthetic%20kitchen%2C%20amazon%20finds%20%E2%80%94%20verified%20Amazon%20best%20seller.
- Status: QUEUED
