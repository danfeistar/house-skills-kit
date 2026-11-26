# Five-Domain Talk Library · English Edition

> **Scope.** This playbook is the script library for the sales floor: what a property consultant actually *says* when a customer asks about location, amenities, the floor plan, a competitor, or the developer's brand. It deliberately does **not** cover the surrounding mechanics — those live in the sibling skills, and this playbook only decides *which script to pull and when to stop talking*:
>
> - Reception route and needs discovery → `sales-reception-sop`
> - Objection branching ("too expensive", "let me look around", …) → `sales-objection-handling` (this library only supplies the standard wording the objection skill branches into)
> - Price calculation, concession ladder, closing → `sales-closing-sop`
> - Discount release rhythm and price-approval authority → `pricing-incentive-release-sop`
> - Competitor *data* (supply, absorption, listed prices) comes from `competitive-intel-sop` field reports — a script may only quote competitor facts that a walkthrough actually verified.
>
> Every script block follows the same three-piece pattern: **standard script → segment variants → failure warnings**. Read the failure warnings before you say the script, not after.

> **A note for English readers.** This library encodes how a Chinese new-home sales office talks, and several mechanics have no clean Western equivalent. They are kept and explained inline: the **sand table** (沙盘, the scale model of the project and its district that anchors most first-visit conversations), **school places** (学区 — in China, which public school a project feeds into is decided annually by the local education authority's catchment announcement, not by the developer, which is why every school-related script below is written to *promise nothing*), **gift area** (赠送面积 — balconies, bay windows, and equipment platforms that the approved plan counts partially or not at all toward the sold floor area), **shared area** (公摊 — the Chinese convention of selling by gross floor area that includes a share of lobbies, lift cores, and corridors, so "usable area" is materially smaller than the number on the contract), and the **three-state discipline** (现有/在建/规划 — existing / under construction / planned, which every amenity script must keep separate). Placeholders in `{{}}` are injected by the project's `brand.yaml` via `render.py`; every number a script quotes about the project must be replaced with the live, verifiable figure — the sample numbers in this library demonstrate *format only*.

> **The six red lines, up front.** Every script below is written inside these constraints; if your live delivery drifts outside them, stop:
> 1. **No school-place promises.** Catchments are published once a year by the education authority. Say only "the historically published catchment for this parcel, and the current year's announcement governs". "This definitely feeds X School" is banned.
> 2. **No planning inflation.** Planned metro / school / retail must be cited as "publicly announced (document number or link available) — completion per the government's announcement". "Opening next month / definitely going ahead" is banned.
> 3. **Data must be real.** Inventory, transaction prices, commute times — if you don't have the verified number, say "let me pull the exact figure for you". Fabricating is banned.
> 4. **No competitor bashing.** State your own strengths and objective differences; no nicknames, no repeating negative rumours.
> 5. **No threat-based closing.** "Prices rise tomorrow / last unit" requires a real price-change document or real absorption data behind it; otherwise banned.
> 6. **No guarantees.** "Guaranteed to hold value / risk-free returns" is banned; investment topics go back to rent-to-price data plus "the risk is yours to weigh".

---

## Part 1 — Location domain (why this spot is worth it · 4 dimensions)

> Boundary note: location = the value of *where it sits*; amenities (Part 2) = how daily life *runs once you live there*. Park and retail topics belong to Part 2 even when the customer raises them while pointing at the sand table.

### 1.1 Transit (metro / arterial roads / commute)

**Standard script (first visit, at the sand table):**

> "Where do you usually work? … All right — let's not take my word for it. Open your map app right now and measure it: {{project}} to {{nearest metro station / arterial road}} is a {{X}}-minute walk — your phone says it, not me. Two trips a day, that's about {{X}} hours a month back in your life. Over ten years of living here, that time is the most tangible value this location has."

**Failure warnings:**

- ❌ Calling a planned metro line "opening soon" — false-promise red line, the single most-complained-about wording on Chinese sales floors.
- ✅ Correct framing: "The plan for this line has been publicly announced — I'll send you the announcement link; the opening date follows the government's notice."
- ❌ Quoting a commute time in free-flow conditions only. The customer will measure at rush hour; when reality disagrees with you, trust collapses — quote door-to-door at the hour they actually travel, and say which condition you're quoting.

**Segment variants:**

- First-time buyer: turn the commute into a monthly account — transit fare or fuel plus tolls, times working days.
- Upgrader: two-parking-bay arrival flow, and how quickly an ageing parent can reach a hospital from here.
- Investor: how mature the district's connection to the city core is — that determines the tenant pool.

### 1.2 District planning & context (government investment / area positioning)

**Standard script (first visit, at the sand table):**

> "You don't have to take the plan on faith — {{plan name}} was publicly announced by {{issuing authority}} in {{year}}, and I'll send you the link. The {{school / park / road}} items in it are written black-on-white; the {{commercial / industry}} parts are still being pushed forward, and I'll tell you that honestly rather than vouch for the government — but what's already announced is certainty you can actually hold."

**Failure warnings:**

- ❌ Word-of-mouth planning ("I hear they're building X") — without a document number it doesn't exist, and one search by the customer exposes it.
- ✅ Only speak of what is publicly announced with a link you can produce; for everything else: "the moment there's news, you're the first to hear it."
- ❌ Ever speaking *for* the government ("this will definitely be demolished / definitely built").

**Segment variants:**

- First-time buyer: start with what touches daily life directly (market, school bus, bus lines).
- Upgrader: the environmental and urban-fabric upgrade logic for the district.
- Investor: employment-driven population inflow and the land-supply cadence — numbers sourced from a `competitive-intel-sop` walkthrough report, not from memory.

### 1.3 School places & enrolment wording (red-line-specific dimension)

**Standard script (family with children):**

> "How old is your child? … Let me be straight with you: I can't promise you the school placement, and neither can anyone else — the catchment is published once a year by the education authority, and whoever promises it is being irresponsible. What I *can* give you: ① the historically published catchment for this parcel, which I'll pull up for you to read yourself; ② the actual construction progress of the project's own {{kindergarten / on-site school}}, and I'll walk you over to see it. The current year's announcement is what governs — let's lock in what can be locked in."

**Failure warnings:**

- ❌ "This definitely feeds X School" — the epicentre of sales-floor complaints nationally; one sentence can sink a project's reputation.
- ✅ Historical catchment record + the real state of on-site education facilities + "the current announcement governs". Nothing more.
- ❌ Using "X School branch campus" branding while the partnership is not yet executed and documented.

**Segment variants:**

- First-time buyer: separate *enrolment eligibility* (this dimension) from *the walk to school* (amenities 2.1) — customers conflate them; keep them clean.
- Upgrader: education continuity — the primary-middle-high school structure of the district.
- Investor: the market premium that school places carry — quote the real listing-price gap from the walkthrough report, not folklore.

### 1.4 Land scarcity & absorption (data must be real)

**Standard script (closing support):**

> "Let me give you the honest picture: this district sold {{N}} parcels in {{year}} and none since. {{project}} has {{X}} units left across the whole development, and the layout you're looking at has {{X}} left. Check that number any time you like — I will never manufacture scarcity to push a deal, because the day you find out I was wrong, everything else I told you is worthless."

**Failure warnings:**

- ❌ Inventing "only X units left" — the customer checks the public sales-control list the next day, sees the truth, and trust goes to zero across everything.
- ✅ Scarcity wording has a hard precondition: the number is verifiable and you invite the verification.
- ❌ "Prices go back up after today" without a genuine, documented price-change decision behind it (see red line 5).

**Segment variants:**

- First-time buyer: remaining inventory *plus* price stability — "this isn't a project that will dump prices because it can't sell" is a reassurance, and it must be true.
- Upgrader: no future land in the same district = the asset-scarcity argument.
- Investor: land-transaction records set the district's supply ceiling — cite the walkthrough report.

---

## Part 2 — Amenities domain (the daily-life circle · 5 dimensions)

> Script logic spine for this whole part: what exists now → drop the customer into a usage scene → overlap with *their* daily routine (the "your average day" walk-through). Keep the three states separate everywhere: **existing / under construction / planned**.

### 2.1 Education access (the walk to school — enrolment eligibility is 1.3's business)

**Standard script:**

> "Let me map your child's average day: the {{kindergarten / school}} at the project gate is a {{X}}-minute walk — no car queue, leave home at {{time}}, at the gate by {{time}}. Middle and high school sit {{distance / location}} away, {{X}} bus stops. Which school the catchment assigns is the authority's annual call — I said that earlier and I won't repeat it as if it were new. What I'm describing here is simply the road between your door and the gate."

**Failure warnings:**

- ❌ Using "education amenities" as a back door into a school-place promise — that's the 1.3 red line wearing a disguise.
- ✅ Physical distance and the walking route only; eligibility never.

### 2.2 Healthcare

**Standard script:**

> "Are there older family members at home? {{nearest general hospital}} is a {{X}}-minute drive, and the community clinic is at {{location}} — prescriptions and blood-pressure checks without a hospital trip. And for a genuine emergency, {{nearest emergency department / ambulance response as officially described}} — I hope you never use that sentence, but a home purchase should price this in before you need it."

**Failure warnings:**

- ❌ "The hospital is right at your doorstep" when it is under construction or only planned.
- ✅ Three states, said separately: existing / under construction / planned — and the planned one gets red-line-2 wording.

### 2.3 Retail & commercial maturity

**Standard script:**

> "Your daily life is three things: buying groceries, eating out, shopping. Existing today: {{market / supermarket / restaurants, by name}}, {{X}} minutes out of the gate. New districts earn their retail over time — this one is {{X}} years old, which makes it one of the rare 'convenient from the day you move in' districts in {{city}}; come tonight, eat nearby, walk the block, and see for yourself. Under construction: {{named commercial complex}} — {{if an opening date is officially published, quote it; if not, say 'under construction' and stop}}. I separate them precisely so you know what you can use tonight versus what is an expectation."

**Failure warnings:**

- ❌ Drawing under-construction or planned retail into the "existing life circle" on the sand table.
- ✅ The three-state discipline *builds* trust when volunteered — customers are used to being blurred at, not separated for.

**Segment variants:**

- First-time buyer: tonight-verifiable convenience — existing amenities only.
- Upgrader: quality of the commercial core and the spending radius.
- Retiree household: the market and the hospital, on foot.

### 2.4 Parks, waterfront & leisure

**Standard script:**

> "Look at this stretch of the sand table — {{park / waterfront name}}, {{X}} metres in a straight line. Weekends with the kids, evenings for a walk: that's your back garden. Go at dusk and stand in it — more customers than I can count went once and came back to sign. A place like that doesn't photograph; you have to stand in it. {{Specific facilities — trails / pitches / playground equipment — per what the park actually has, nothing invented}}."

**Failure warnings:**

- ❌ Straight-line distance quoted as walking distance (800 m as-the-crow-flies is not "right downstairs").
- ✅ Report straight-line / walking / driving separately, and round the distance *down* when unsure — under-promise on geography because it is checkable in one map query.

### 2.5 Neighbourhood (the soft amenity)

**Standard script:**

> "There's an amenity you can't see on the sand table: the neighbours. This development is {{real owner profile — e.g. mostly local professionals / teachers and medical staff}}, and the first delivered phase already runs {{real community group / activity, described as it truly is}}. A house is ten years of the faces you greet on the way out — that part of the purchase doesn't show up on a floor plan."

**Failure warnings:**

- ❌ Inventing a lively owner community — the customer delivers into silence and your name pays for it.
- ✅ If it exists, say it; if it doesn't, don't raise it — or better, walk them through a delivered phase and let them feel it themselves.

---

## Part 3 — Floor-plan domain (7 dimensions)

> Script logic spine: tour sequencing → plan-vs-plan comparison → real area arithmetic (gift / usable) → daylight and circulation → the show-flat boundary, said out loud.

### 3.1 Tour sequencing (what you show first is a decision)

**Decision tree:**

```
What does this customer care about most? (already mapped during reception)
├─ Daylight / orientation → show the weakest view of the same layout first (usually low floor or
│   road-facing), then the target unit — the contrast becomes the pitch
├─ Space scale → small to large, ending inside the target layout (anchoring)
└─ Budget-sensitive → one step above budget first (a reason to stretch), then the affordable
    one (the landing zone)
```

**Standard script (weakest-first example):**

> "Let me start you in a {{lower-floor / road-facing}} unit first — walk through it… Now, this is why {{target unit}} carries a {{X}}-premium over it: {{what exactly is different}}. The difference between two homes lands harder standing inside them than staring at two floor plans."

**Failure warnings:**

- ❌ Showing the worst unit and losing the customer in it — "weakest first" only works when the weak unit *teaches something*, and you watch the customer's mood inside it; if they sour, flip the order immediately. The purpose of the weak unit is contrast, not discouragement.

### 3.2 Plan-vs-plan comparison

**Standard script:**

> "Two plans, side by side, same {{X}} m²: in {{competitor / our other layout}} the corridor eats {{X}} m² right here; in ours it's {{X}} m². The difference is floor you actually stand on. When you buy {{X}} m², ask what you can *use*."

**Tool hook — area chains and efficiency numbers come from the calculator, never mental arithmetic:**

```bash
# Compare real "cost per usable square metre" across two projects (verified command):
python3 skills/calc-toolkit/efficiency.py --mode compare --label-a ProjectA --rate-a 80 --price-a 15000 --label-b ProjectB --rate-b 72 --price-b 13800
```

The tool's verdict in this exact case: Project B's cheaper gross price is an illusion — at 72% efficiency its per-inner-m² price (≈19,167) beats Project A's (≈18,750). Same lesson every time: quote inner-area unit prices when comparing, and let the tool print it.

### 3.3 Gift space (balcony / bay window / equipment platform — lawful wording only)

**Standard script:**

> "This layout carries a {{balcony / bay window / equipment platform}}, which the approved plan counts partially — or not at all — toward the sold area. Strictly speaking that's not 'free space'; it is {{a lawful design under the approved planning documents}}. Here are the {{approval documents and the stamped floor plan}} — let's go through which parts are counted, which are gifted, line by line. I don't fudge gift numbers: every figure I quote is findable on the drawings."

**Failure warnings:**

- ❌ "Buy 89, get 20 free" style slogans — when the numbers don't match the approved documents, that's a refund-and-complaint generator.
- ✅ Gift wording must match the approved drawings exactly: balconies count at half, bay windows not at all, equipment platforms per the planning file's classification.
- ❌ Hinting that illegal enclosures ("close in the platform") can add area — that's an unlicensed-construction red line; what was added gets demolished at delivery.
- ✅ Also state *what may lawfully be altered and what may not* — the reform boundary belongs in the same conversation.

**Segment variants:**

- First-time buyer: gift space = usable-area value ("the extra room").
- Upgrader: the balcony / terrace as a living scene (tea table, garden).

### 3.4 Usable area (efficiency / shared area / real interior — numbers do the talking)

**Standard script:**

> "Let's do the area account properly: gross floor area {{X}} m², shared area {{Y}}%, interior {{Z}} m²; add the gifted parts and you actually live on {{W}} m² — a usable-area ratio of {{P}}%. In the same district, {{competitor}} shares {{Q}}%; buy the same {{X}} m² there and you end up {{difference}} m² short. You're not buying contract area — you're buying the floor you stand on."

**Tool hook — the efficiency chain runs on the calculator, and the numbers must match the survey report eventually:**

```bash
# Gross → interior → usable chain, with the shared-area split (verified command):
python3 skills/calc-toolkit/efficiency.py --gross 89 --type plate
```

**Failure warnings:**

- ❌ Wielding "high gift + low share" as a pure win — a suspiciously high usable ratio can mean the developer shaved the lobby, lift lobbies, and corridors instead; public quality is the hidden cost.
- ✅ Explain *where* the shared area goes (lobby / lifts / corridors) and pair the usable ratio with the public-realm quality.
- ❌ Promising a post-delivery re-measurement will favour the buyer — delivery measurement follows the licensed survey report; say so in advance.

### 3.5 Daylight & spacing (building separation / floor level / orientation)

**Standard script:**

> "On the winter solstice — the day shadows are longest all year — this layout gets {{X}} hours of direct sun from {{time}}. That's {{the daylight-analysis basis}}, not my opinion. Building separation is {{X}} metres against a {{N}}-storey block in front; go stand at the {{floor}}-floor window and feel it."

**Tool hook — separation and shading run on the calculator; quote its floor-level verdict, not your impression:**

```bash
# Winter-solstice noon shading check: 26-storey block in front, 45 m actual gap,
# does floor 12 get noon sun? (verified command)
python3 skills/calc-toolkit/spacing.py --floors 26 --actual 45 --floor 12 --city {{city}}
```

The tool prints the theoretical minimum separation, which floors are shaded at noon, and a verdict for the floor you name. If the verdict is "shaded", say it before the customer discovers it — a shaded floor sold as sunny is a refund case, not a sale.

**Failure warnings:**

- ❌ Quoting summer sun angles as if they were the yearly standard — the solstice-noon worst case is the honest baseline and the only one a surveyor will back.
- ✅ Where the tool's verdict is unfavourable, pivot honestly: lower floors trade daylight for price; the customer decides with both numbers on the table.

### 3.6 Storage & circulation

**Standard script:**

> "Notice the entry alcove — {{storage detail}}. The kitchen runs a {{U-shape / L-shape}}: wash, chop, cook, one line, no backtracking. Living and sleeping zones are split, so guests never cut through the bedroom wing. Whether a home *works* hides exactly here, in the walking lines."

*(No tool hook — this dimension is about demonstrating the plan on foot.)*

### 3.7 The show-flat boundary (always say it — it prevents the complaints)

**Standard script (volunteered, and that's the point):**

> "One thing before you fall in love with this room: the show flat is dressed. {{List the non-delivery items — soft furnishing / furniture dimensions / some cabinetry / wall alterations}} are not part of delivery; the delivery standard is annex {{X}} of the contract. Read that list *before* you buy, and there will be no surprise on handover day."

**Failure warnings:**

- ❌ Letting the customer treat the show flat as the delivery standard — the delivery gap is the single largest complaint source at handover.
- ✅ Volunteering the "not included" list is a credibility *plus*; hiding it is the mine.

---

## Part 4 — Competitors (3 scenes)

> Iron rule: your own strengths and objective differences only. No nicknames, no bashing, no repeating negative rumours.
> Data source: `competitive-intel-sop` walkthrough reports — every competitor fact in a script must come from a field visit, never from hearsay or the customer's own account.

### 4.1 The customer raises a competitor ("they're cheaper than you")

**Standard script:**

> "I've walked {{competitor}} myself, so objectively: they {{real strength — say it, and say it fully}}. Where we differ is {{two or three objective differences}} — and here's what each of those means for *you*, {{framed around what they said they care about most}}. The {{price}} gap is exactly those items. Put our {{delivery standard / building separation / management fee}} side by side in a list and judge the value yourself — you're buying a home, I can't stop you from looking around, and I'd only ask that you compare *completely*."

**Failure warnings:**

- ❌ Bashing the competitor the instant they're named — the customer reads your anxiety, and your credibility drops with it.
- ✅ Acknowledge the competitor's real strength *first*, then differentiate — the objective posture is itself persuasive.
- ❌ Quoting stale or wrong competitor facts — the customer has just come from there; one wrong detail and everything you said about your own project is suspect too.

### 4.2 You run the comparison (pre-emptive interception)

**Standard script:**

> "There are {{N}} developments selling in this district. I've put the {{key indicators}} of all three into one table for you — including our own weak rows, honestly filled in ({{the real weakness}}). Rank the rows by what matters to you and you won't need to walk all three sites."

**Failure warnings:**

- ❌ A comparison table that only flatters you — spotted instantly, and the whole table dies with it.
- ✅ A table that dares to list your own weakness is the only kind that earns trust — but prepare the *explanation* for each weakness in advance (weakness + the compensating value that pairs with it).

### 4.3 The customer returns from the competitor (post-comparison revisit)

**Standard script:**

> "So how did it feel? … *(listen to the whole account first — do not interrupt)* — now let me take your points one by one: {{for each: concede what is genuinely stronger there; clarify our actual difference; correct misconceptions with facts}}. You now hold complete information on both. If you're ready to decide, rank your {{decisive factors — from the needs mapped at reception}} and see which project actually tops your own list."

**Failure warnings:**

- ❌ Pouring cold water on the competitor the moment they walk back in — they have just formed their own judgement there, and your attack lands on *their* judgement, not on the competitor.
- ✅ First listen, then concede what's true, then correct what's wrong, then re-rank their criteria. In that order.

---

## Part 5 — Brand (5 dimensions)

> Script logic spine: evidence that can be checked → places that can be visited → promises that only exist in the contract.

### 5.1 Developer strength

**Standard script:**

> "I won't describe strength with adjectives — here are three things you can check: ① delivered projects {{list}} totalling {{units}} homes in {{region}}; go ask the owners, they'll talk. ② {{credentials / rankings / credit ratings — real ones only}}. ③ our local construction site is in active build and open to visits any time. Strength you cannot check doesn't count."

**Failure warnings:**

- ❌ Using group-level honours or distant-city performance as a promise about *this* project.
- ✅ The three-piece evidence set: a delivered project (visitable) + credentials (checkable) + active local progress (verifiable on site).

### 5.2 Property management reputation

**Standard script:**

> "The management fee is {{X}} — here is what it buys, item by item: {{service list}}. Words are cheap, so: {{invitation wording to visit the delivered phase's management on site}} — watch how the guards handle you, the state of the cleaning, how often the lifts get serviced. You'll live with the property manager for ten years; that line item outlasts the mortgage."

### 5.3 Construction quality

**Standard script:**

> "Judge quality by three things you can verify: ① the main contractor, {{name and real credentials}}; ② materials and workmanship {{where named in the contract annexes}}; ③ the open-site days and progress photos — {{this project's real arrangement}}. We let you look; come any time."

### 5.4 Delivery assurance (the certainty evidence chain)

**Standard script:**

> "I won't thump my chest about delivery — here are four things you can check instead. ① Your purchase money goes into the **escrow supervision account** at {{supervising bank}} and is released by construction milestone — that's {{the local regulatory rule}}, not our policy. ② We have delivered {{X}} projects locally, {{on-time record — real}}, and you can visit the active site today. ③ Post-delivery rectification runs through {{the real mechanism — rapid-repair team / handover inspection process}}, itemised on the acceptance checklist. ④ The delay-liability clause is written into contract article {{X}}. Four items — check each one, and then decide whether to feel secure."

**Failure warnings:**

- ❌ "Absolutely on time / absolutely no problem" — any absolute promise is a false promise; the evidence chain is the only sellable form of assurance.
- ✅ Supervised escrow + delivery history + rectification mechanism + contract clause. That's the whole toolkit.
- ❌ Tying delivery assurance into a discount promotion ("guarantee-style discount") — that reads as an implied promise and recreates the risk you just avoided.

**Segment variants:**

- First-time buyer: escrow supervision + the contract clause — that's where their fear actually lives.
- Upgrader: visit the delivered phase and talk to an owner — experiential evidence.
- Investor: delivery certainty is the precondition for the asset's liquidity.

### 5.5 Owner community & word of mouth

**Standard script:**

> "The best advertisement is a current owner. {{A real word-of-mouth case from the delivered phase — it must be real, and arranging a face-to-face with an owner is the strongest move}}. And if you end up recommending a friend, the referral terms are {{real referral-program terms — cross-referenced with the resident-referral campaign policy, quoted as published}}."

**Failure warnings:**

- ❌ Manufactured or bought testimonials — two sentences of chat with a real owner and it unravels.
- ✅ Word of mouth must be real and reachable — a genuine owner conversation is the single strongest brand script there is.

---

## Practice mode (drill with AI as the customer)

For training, run this library as a sparring kit: tell the AI to play a customer — pick a segment (first-time buyer / upgrader / investor), an emotional state (impatient / comparison-shopping / worried about delivery), and one hard question per domain. The consultant answers using the Part that matches; the AI scores the reply against that Part's failure warnings and the six red lines, and flags any sentence that promised, inflated, invented, bashed, threatened, or guaranteed. One drill round per domain is enough to expose a new hire's habitual red-line breaches.

## Relationship to the other skills

- **Reception flow, needs discovery, matching, hand-off** → `sales-reception-sop` (this library starts where reception needs a *thing to say*).
- **Objection branching and second-layer objections** → `sales-objection-handling` (it consumes this library's standard wording and adds the branch logic).
- **Price calculation, concession ladder, closing rhythm** → `sales-closing-sop` — this library deliberately excludes price negotiation; the only pricing-adjacent block here (1.4) is the *scarcity framing*, which must obey red line 5.
- **Competitor data** → `competitive-intel-sop` reports are the only permitted source for Part 4 facts.
- **All policy, tax, and loan figures** → computed via `calc-toolkit`; nothing in this library computes or quotes policy numbers from memory.

No policy numbers and no legal conclusions live in this library: anything regulatory is checked against the current local announcement on the day it comes up.
