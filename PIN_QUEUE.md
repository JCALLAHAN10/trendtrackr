—## ⚠️ STAY-HUMAN RULES — HIGHEST PRIORITY (Jack: a bot flag would be CATASTROPHIC)
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
> **FOCUS MODE (2026-07-29, updated):** Confirmed winners (proven Pinterest landing pages) = **Water Bottles & Tumblers (anchor) + Kitchen Gadgets.** Home Organization TRIMMED (deprioritized). Car Accessories = **PROBE** (2 test pins below — pin them and watch GA4 for external landings before investing). All other topics parked.


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
- Status: POSTED 2026-07-20

### Kitchen Gadgets guide
- Board: Kitchen Gadgets & Cooking Tools (create in-dialog if missing)
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-kitchen-gadgets.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpin-best-tiktok-viral-kitchen-gadgets.png&description=Best%20TikTok%20Viral%20Kitchen%20Gadgets%202026%20%E2%80%94%20cooking%20tools%2C%20kitchen%20must%20haves%2C%20vegetable%20chopper%2C%20air%20fryer%20accessories%2C%20oil%20sprayer%2C%20meat%20thermometer%2C%20chicken%20shredder%2C%20meal%20prep%20gadgets%2C%20cooking%20hacks%2C%20kitchen%20essentials%2C%20home%20cook%2C%20amazon%20finds%20%E2%80%94%20verified%20against%20Amazon%20Kitchen%20Best%20Sellers.
- Status: POSTED 2026-07-18 (live: pinterest.com/pin/990651249301968054)

---

## Single-product pins (images live at /images/pp-*.png)

### Owala FreeSip
- Board: Water Bottles & Tumblers
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-viral-water-bottles-tumblers.html%23owala&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpp-owala.png&description=Owala%20FreeSip%20water%20bottle%20%E2%80%94%20Amazon%27s%20%231%20best%20selling%20water%20bottle%2C%204.7%20stars%2C%20130k%20ratings.%20Viral%20TikTok%20water%20bottle%2C%20insulated%20tumbler%2C%20gym%20water%20bottle%2C%20cup%20with%20straw%2C%20hydration%2C%20travel%20bottle%2C%20aesthetic%20water%20bottle%2C%20amazon%20finds%20%E2%80%94%20verified%20best%20seller.
- Status: POSTED 2026-07-20

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
- Status: POSTED 2026-07-20

### Velvet Hangers
- Board: Home Organization & Restock Finds
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-home-organization.html%23hangers&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpp-hangers.png&description=Slim%20velvet%20hangers%20%E2%80%94%20Amazon%27s%20%232%20organization%20best%20seller%2C%20234k%20ratings.%20Closet%20organization%2C%20closet%20makeover%2C%20space%20saving%20hangers%2C%20non%20slip%20hangers%2C%20wardrobe%20organization%2C%20aesthetic%20closet%2C%20restock%2C%20amazon%20finds%20%E2%80%94%20verified%20best%20seller.
- Status: PARKED 2026-07-29 (trimmed — home org deprioritized; kitchen+water are the proven winners)

### Rubbermaid Brilliance
- Board: Home Organization & Restock Finds
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-home-organization.html%23rubbermaid&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpp-rubbermaid.png&description=Rubbermaid%20Brilliance%20containers%20%E2%80%94%20the%20viral%20fridge%20restock%20containers%2C%2059k%20ratings.%20Food%20storage%20containers%2C%20fridge%20organization%2C%20meal%20prep%2C%20pantry%20organization%2C%20airtight%20containers%2C%20kitchen%20organization%2C%20restock%2C%20amazon%20finds%20%E2%80%94%20verified%20best%20seller.
- Status: PARKED 2026-07-29 (trimmed — home org deprioritized; kitchen+water are the proven winners)

### Veken Shower Caddy
- Board: Home Organization & Restock Finds
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-home-organization.html%23veken&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpp-veken.png&description=Veken%20no-drill%20shower%20caddy%20%E2%80%94%20renter%20friendly%20bathroom%20organization%2C%2014k%20ratings.%20Shower%20organization%2C%20bathroom%20storage%2C%20adhesive%20shelf%2C%20no%20drill%2C%20dorm%20essentials%2C%20rental%20apartment%2C%20small%20bathroom%2C%20amazon%20finds%20%E2%80%94%20verified%20best%20seller.
- Status: PARKED 2026-07-29 (trimmed — home org deprioritized; kitchen+water are the proven winners)

### Cisily Sink Caddy
- Board: Home Organization & Restock Finds
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-home-organization.html%23cisily&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpp-cisily.png&description=Cisily%20sink%20caddy%20sponge%20holder%20%E2%80%94%20the%20viral%20sink%20station%2C%2013k%20ratings.%20Kitchen%20sink%20organization%2C%20sponge%20holder%2C%20kitchen%20organization%2C%20counter%20organization%2C%20stainless%20steel%2C%20aesthetic%20kitchen%2C%20amazon%20finds%20%E2%80%94%20verified%20Amazon%20best%20seller.
- Status: PARKED 2026-07-29 (trimmed — home org deprioritized; kitchen+water are the proven winners)


### Travel Essentials guide — PARKED 2026-07-29 (Option A: off-topic, do not pin)
- Board: Travel Essentials & Packing Tips (create in-dialog if missing)
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-travel-essentials.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpin-travel-essentials.png&description=TikTok%20Viral%20Travel%20Essentials%202026%20%E2%80%94%20carry%20on%20essentials%2C%20packing%20tips%2C%20compression%20packing%20cubes%2C%20travel%20neck%20pillow%2C%20portable%20charger%20power%20bank%2C%20compression%20socks%20for%20flying%2C%20universal%20travel%20adapter%2C%20long%20haul%20flight%20essentials%2C%20airplane%20must%20haves%2C%20vacation%20packing%20list%2C%20travel%20hacks%2C%20amazon%20finds%20%E2%80%94%20verified%20against%20real%20Amazon%20Best%20Sellers.
- Status: PARKED 2026-07-29 (focus mode)

### Home Gym & Fitness guide (article-level — added 2026-07-21)
- Board: Home Gym & Fitness (create in-dialog if missing)
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-home-gym-fitness.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fpin-home-gym-fitness.png&description=TikTok%20Viral%20Home%20Gym%20%26%20Fitness%20Gear%202026%20%E2%80%94%20adjustable%20chest%20workout%20trainer%2C%20twister%20arm%20trainer%2C%20push%20up%20board%2C%20resistance%20bands%20set%2C%20doorway%20pull%20up%20bar%2C%20exercise%20mat%2C%20small%20space%20home%20gym%2C%20apartment%20workout%20equipment%2C%20amazon%20finds%20%E2%80%94%20cross%20checked%20against%20real%20Amazon%20sales%20data.
- Status: PARKED 2026-07-29 (focus mode — off-topic)

---

## FOCUS QUEUE — Option A (added 2026-07-29): ONLY the 3 winning topics, water bottles lead
> Growth-lane focus (Jack-approved). Fresh unique pins, water bottles first. Off-topic
> pins (Travel, Home Gym, Tech, Pet, Cleaning, Car) are PARKED below — do NOT pin them.
> Daily pick rule still applies: up to ~5/day, ONE pin per destination URL/day, spaced out.

### Owala vs Stanley vs HydroJug comparison
- Board: Water Bottles & Tumblers
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-viral-water-bottles-tumblers.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fq5-water-vs.png&description=Owala%20vs%20Stanley%20vs%20HydroJug%20%E2%80%94%20which%20viral%20insulated%20tumbler%20actually%20wins%3F%20Compared%20on%20leak-proof%20lids%2C%20ice%20retention%20and%20car-cup%20fit%2C%20all%20Amazon%20best-seller%20verified.%20Water%20bottle%2C%20tumbler%2C%20hydration%2C%20gym%20water%20bottle%2C%20cup%20with%20straw%2C%20aesthetic%20water%20bottle%2C%2030oz%20tumbler%2C%20insulated%20bottle%2C%20amazon%20finds.
- Status: QUEUED

### Best tumbler for your car cup holder
- Board: Water Bottles & Tumblers
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-viral-water-bottles-tumblers.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fq6-water-carcup.png&description=The%20best%20insulated%20tumbler%20that%20actually%20fits%20a%20standard%20car%20cup%20holder%20%E2%80%94%20we%20checked%20the%20base%20sizes%20so%20your%2030oz%20doesn%27t%20wobble%20on%20the%20commute.%20Water%20bottle%2C%20tumbler%2C%20cup%20with%20straw%2C%20car%20cup%2C%20travel%20tumbler%2C%20Stanley%20dupe%2C%20Owala%2C%20hydration%2C%20aesthetic%20water%20bottle%2C%20amazon%20best%20seller.
- Status: QUEUED

### The 24oz bottle that makes you drink more water
- Board: Water Bottles & Tumblers
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-viral-water-bottles-tumblers.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fq11-water-drinkmore.png&description=The%2024oz%20Owala%20FreeSip%20people%20say%20doubled%20their%20daily%20water%20intake%20%E2%80%94%20leak-proof%2C%20gym-bag%20and%20car-cup%20friendly%2C%20Amazon%27s%20%231%20best-selling%20water%20bottle.%20Water%20bottle%2C%20hydration%2C%20gym%20bottle%2C%20cup%20with%20straw%2C%20tumbler%2C%20aesthetic%20water%20bottle%2C%20drink%20more%20water%2C%20amazon%20finds.
- Status: QUEUED

### Aesthetic tumblers ice retention test
- Board: Water Bottles & Tumblers
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-viral-water-bottles-tumblers.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fq12-water-icetest.png&description=Aesthetic%20tumblers%20that%20still%20have%20ice%2024%20hours%20later%20%E2%80%94%20Stanley%20vs%20Owala%20vs%20HydroJug%20on%20real%20ice%20retention%2C%20ranked%20by%20Amazon%20sales%20data.%20Tumbler%2C%20insulated%20water%20bottle%2C%20iced%20coffee%20cup%2C%20cup%20with%20straw%2C%2030oz%2C%2040oz%2C%20aesthetic%20hydration%2C%20amazon%20best%20seller.
- Status: QUEUED

### Vtopmart drawer organizers spotlight
- Board: Home Organization & Restock Finds
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-home-organization.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fq1-homeorg-spotlight.png&description=The%20%2420%20Vtopmart%20clear%20drawer%20organizers%20behind%20every%20TikTok%20restock%20video%20%E2%80%94%20Amazon%27s%20%231%20in%20Home%20Storage%2C%20keeps%20bathroom%2C%20vanity%20and%20kitchen%20drawers%20sorted.%20Home%20organization%2C%20drawer%20organizer%2C%20restock%2C%20pantry%20organization%2C%20bathroom%20organizer%2C%20closet%2C%20aesthetic%20home%2C%20amazon%20finds%2C%20renter%20friendly.
- Status: PARKED 2026-07-29 (trimmed — home org deprioritized; kitchen+water are the proven winners)

### Renter-friendly organization under $30
- Board: Home Organization & Restock Finds
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-home-organization.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fq2-homeorg-under30.png&description=Renter-friendly%20home%20organization%20under%20%2430%20%E2%80%94%20no-drill%20shower%20caddies%2C%20sink%20organizers%20and%20drawer%20bins%20that%20leave%20zero%20holes.%20Small%20apartment%20organization%2C%20dorm%20room%2C%20no%20drill%2C%20rental%20friendly%2C%20bathroom%20organization%2C%20home%20storage%2C%20amazon%20must%20haves%2C%20restock%20finds.
- Status: PARKED 2026-07-29 (trimmed — home org deprioritized; kitchen+water are the proven winners)

### Small bathroom space-doubling organizers
- Board: Home Organization & Restock Finds
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-home-organization.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fq7-homeorg-smallbath.png&description=Small%20bathroom%3F%205%20space-doubling%20organizers%20under%20%2425%20%E2%80%94%20no-drill%20shelves%2C%20over-the-door%20racks%20and%20drawer%20bins%20that%20turn%20a%20cramped%20rental%20into%20real%20storage.%20Small%20bathroom%20organization%2C%20apartment%2C%20dorm%2C%20no%20drill%2C%20home%20storage%2C%20aesthetic%20organization%2C%20amazon%20finds.
- Status: PARKED 2026-07-29 (trimmed — home org deprioritized; kitchen+water are the proven winners)

### Airtight pantry restock containers
- Board: Home Organization & Restock Finds
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-home-organization.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fq8-homeorg-pantry.png&description=Pantry%20restock%3A%20airtight%20containers%20that%20keep%20food%20fresh%202x%20longer%20%E2%80%94%20the%20Rubbermaid%20Brilliance%20set%20behind%20every%20viral%20restock%20video%2C%20Amazon%20best-seller%20verified.%20Pantry%20organization%2C%20food%20storage%2C%20kitchen%20organization%2C%20restock%2C%20airtight%20containers%2C%20home%20organization%2C%20aesthetic%20pantry%2C%20amazon%20finds.
- Status: PARKED 2026-07-29 (trimmed — home org deprioritized; kitchen+water are the proven winners)

### 5 kitchen gadgets tested only 3 kept
- Board: Kitchen Gadgets & Cooking Tools
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-kitchen-gadgets.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fq3-kitchen-tested.png&description=5%20viral%20kitchen%20gadgets%20tested%20%E2%80%94%20only%203%20earned%20drawer%20space%2C%20cross-checked%20against%20Amazon%20Kitchen%20best-sellers%20so%20you%20skip%20the%20clutter.%20Kitchen%20gadgets%2C%20cooking%20tools%2C%20kitchen%20must%20haves%2C%20meal%20prep%2C%20vegetable%20chopper%2C%20air%20fryer%20accessories%2C%20home%20cook%2C%20amazon%20finds.
- Status: QUEUED

### Fullstar chopper spotlight
- Board: Kitchen Gadgets & Cooking Tools
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-kitchen-gadgets.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fq4-kitchen-chopper.png&description=The%20Fullstar%204-in-1%20vegetable%20chopper%20that%20cuts%20prep%20time%20in%20half%20%E2%80%94%20still%20a%202026%20Amazon%20best-seller%2C%20outselling%20the%20copycats.%20Kitchen%20gadget%2C%20vegetable%20chopper%2C%20veggie%20cutter%2C%20meal%20prep%2C%20cooking%20tools%2C%20kitchen%20must%20haves%2C%20dicer%2C%20amazon%20finds%2C%20time%20saver.
- Status: QUEUED

### Kitchen gadgets under $15
- Board: Kitchen Gadgets & Cooking Tools
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-kitchen-gadgets.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fq9-kitchen-under15.png&description=5%20kitchen%20gadgets%20under%20%2415%20that%20feel%20like%20cheating%20%E2%80%94%20budget%20cooking%20tools%20cross-checked%20against%20Amazon%20Kitchen%20best-sellers.%20Kitchen%20gadgets%2C%20cheap%20kitchen%20tools%2C%20cooking%20hacks%2C%20meal%20prep%2C%20kitchen%20must%20haves%2C%20air%20fryer%2C%20budget%20kitchen%2C%20amazon%20finds%20under%2015.
- Status: QUEUED

### 4-in-1 chopper meal prep hack
- Board: Kitchen Gadgets & Cooking Tools
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-kitchen-gadgets.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fq10-kitchen-mealprep.png&description=The%204-in-1%20chopper%20that%20cuts%2020%20minutes%20off%20dinner%20prep%20%E2%80%94%20the%20viral%20Fullstar%20veggie%20chopper%2C%20top-ranked%20on%20Amazon.%20Meal%20prep%2C%20kitchen%20gadget%2C%20vegetable%20chopper%2C%20cooking%20tools%2C%20dinner%20hacks%2C%20kitchen%20must%20haves%2C%20food%20prep%2C%20amazon%20best%20seller.
- Status: QUEUED

---

## CAR ACCESSORIES — PROBE (added 2026-07-29): TEST whether it pulls its OWN external audience
> Car accessories had strong on-site engagement but ZERO direct external landings — unproven as a
> landing page. Pin these 1-2, then check GA4 Traffic acquisition for `Pinterest` sessions landing
> ON the car-accessories URL. If external landings + good engagement appear over ~2 weeks, promote it
> to a real focus category. If not, leave parked. Board: Car Accessories & Organizers.

### Car organization — trunk & seat-gap finds (PROBE)
- Board: Car Accessories & Organizers (create in-dialog if missing)
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-car-accessories.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fcar1-organizers.png&description=Car%20organization%20ideas%20%E2%80%94%205%20trunk%20organizers%2C%20seat-gap%20fillers%20and%20console%20caddies%20that%20stay%20put%2C%20ranked%20against%20Amazon%20Automotive%20best-sellers.%20Car%20accessories%2C%20car%20organization%2C%20trunk%20organizer%2C%20car%20interior%2C%20road%20trip%20essentials%2C%20car%20must%20haves%2C%20auto%20accessories%2C%20amazon%20car%20finds.
- Status: QUEUED (PROBE)

### Leak-proof car trash can (PROBE)
- Board: Car Accessories & Organizers (create in-dialog if missing)
- Save URL: https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Farticles%2Fbest-tiktok-viral-car-accessories.html&media=https%3A%2F%2Fjcallahan10.github.io%2Ftrendtrackr%2Fimages%2Fcar2-trashcan.png&description=The%20leak-proof%20car%20trash%20can%20everyone%27s%20buying%20%E2%80%94%20HOTOR%20car%20trash%20can%20with%20liner%20and%20lid%2C%20a%20viral%20car-organization%20staple.%20Car%20accessories%2C%20car%20trash%20can%2C%20car%20organization%2C%20car%20interior%2C%20road%20trip%2C%20car%20must%20haves%2C%20auto%20accessories%2C%20amazon%20car%20finds%2C%20car%20cleaning.
- Status: QUEUED (PROBE)

