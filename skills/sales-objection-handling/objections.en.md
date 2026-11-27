# Objection Handling Playbook · English Edition

> **Scope.** This playbook is the branch logic for the sales floor: what a property consultant does *after* a customer raises an objection — how to receive it, find the real worry behind it, and turn it into a next step. It deliberately does **not** cover what comes before or after:
>
> - First reception and needs discovery → `sales-reception-sop` (answering objections before you know the customer's budget and purpose means answering in the wrong direction)
> - The *wording* a branch resolves into (location, amenities, floor plan, competitor, brand) → `sales-talk-library` (this playbook decides which branch applies; the library supplies the standard script that branch points at)
> - Price calculation, concession ladder, and the closing push → `sales-closing-sop` (when an objection is resolved is the closing *moment*, but the closing move itself lives there)
> - Loan eligibility and approval questions → `sales-mortgage-sop`
> - Price-policy complaints and deposit refunds → `pricing-incentive-release-sop` plus legal — contract disputes are out of scope here
>
> Every objection below follows the same five-piece discipline: **the customer's exact words → the worry branch table → response scripts → banned wording → segment variants**. Read the branch table *before* you answer: the same sentence means three different things from three different customers, and answering the wrong branch is worse than answering slowly.

> **A note for English readers.** Several mechanics of a Chinese new-home sales office have no clean Western equivalent, and this playbook leans on them. They are kept and explained inline: the **escrow supervision account** (预售资金监管 — in China, presale money is paid into a government-supervised escrow account at a named bank and released to the developer by construction milestone; it is the single strongest verifiable fact against delivery-risk fears), **unit-by-unit pricing with approval-controlled discounts** (一房一价 + 折扣审批制 — every unit carries a filed price registered with the housing authority, and any discount requires written approval, so "this is the best price I can give" is a checkable claim, not a negotiating pose), the **subscription form** (认购单 — the pre-contract sheet recording unit, price, discount, and payment plan, signed before the formal contract is filed), the **sales-control board** (销控 — the office board showing sold/reserved units, which customers can cross-check), and the **second visit** (二访 — most new-home deals in China close on the second or third visit, so the real goal of objection handling is *earning the return visit*, not forcing a same-day close). The **50% health line** referenced in Part 1 is the common Chinese mortgage-underwriting guideline that the monthly payment should not exceed half of documented household income. Placeholders in `{{}}` are injected by the project's `brand.yaml` via `render.py`; every number a script quotes must be replaced with the live, verifiable figure — sample numbers demonstrate format only, and any figure about prices, discounts, or inventory you cannot verify gets the honest reply: "let me pull the exact number for you."

> **The red lines, up front.** Every response below is written inside these five constraints; check each response against them *before* it leaves your mouth:
> 1. **No threat-based pressure.** "Sign today or prices rise / the unit is gone" requires a real, documented price-change decision or real absorption data behind it. Without the paper, the sentence is banned.
> 2. **No false guarantees.** Delivery-risk answers use the evidence chain only (escrow account, progress, delivered projects, contract clause). No chest-thumping, no "absolutely cannot fail".
> 3. **Data must be verifiable.** Transaction prices, discounts, remaining inventory — if you don't have the verified figure, say "let me check and give you the exact number", then actually come back with it.
> 4. **No competitor bashing.** When the customer pressures with a competitor, respond with objective differences only — no nicknames, no repeating negative rumours, no attacking their judgement.
> 5. **No debt-minimising framing.** Payment-affordability answers must never nudge the customer past their real capacity. The "it's just bubble-tea money" style of framing is banned outright; the health-ratio arithmetic below is the only permitted form.

---

## Part 1 — "It's too expensive."

> The most common objection and the most wrongly answered. **Too expensive** is a symptom, not a diagnosis: branch A needs arithmetic, branch B needs a value comparison, branch C needs dignity. Answering B's words to an A customer (reciting value points at someone who genuinely cannot stretch) is how visits die.

### 1.1 The worry branch table

| Branch | Real worry | Signals that give it away |
|--------|-----------|--------------------------|
| **A — Over budget** | The monthly payment genuinely strains them | Asks about down payment, asks about monthly payment, does the arithmetic in detail, quotes their own income |
| **B — Fear of overpaying** | Believes this money buys less value elsewhere | Repeatedly asks "why is this pricier than {{competitor}}", brings up specific rivals, compares listing sites |
| **C — Bargaining habit** | An opening move of the negotiation, not a verdict | Conversation was flowing well, then the objection drops abruptly; watches your reaction more than the price |

### 1.2 Branch A — over budget → reframe total price into payment health

> "Let's not argue about the total — let's look at the monthly payment, because that's the number you'll actually live with. Your household income is about {{X}} a month; this unit runs about {{Y}} a month. That's {{Z}}% of your income, and the underwriting guideline sits at 50% — you're inside the healthy range. And if it *were* tight, the fix isn't a discount I can't give — it's a different floor or layout that pulls the payment back into the comfortable zone. Let me run the numbers for both and show you."

**Tool hook — the payment figure comes from the calculator, never from memory or mental arithmetic; the rate must come from the rules library, not from a slogan:**

```bash
# Monthly payment, 30% down, 30 years, commercial loan (verified command):
python3 skills/calc-toolkit/mortgage.py --price 1500000 --downpay 30 --years 30
```

The tool prints both repayment structures with the rules-library rate and its version date — in this exact case: loan principal 1,050,000, **equal (annuity) payment 4,484/month** (total interest 564,122), **equal-principal 5,629 in month one** declining monthly to about 2,924. Quote the annuity figure for the health-ratio line, and show the declining structure to customers whose income will grow. If the ratio comes out above the line, the honest move is the smaller unit or longer term — not a promised discount.

**Banned wording:**

- ❌ "Buy now or it'll only get more expensive" — threat-based pressure with no documented price-change decision behind it (red line 1).
- ❌ "That's basically a bargain-basement price" — tells the customer their judgement is wrong; the price is *expensive to them*, which is a fact about their budget, not their intelligence.
- ❌ "The manager said this is the floor price, and I'll slip you some of my own commission" — a double violation: unauthorised price commitment plus a sales-floor discipline breach. One customer complaint ends this career path.

**Segment variants:**

- First-time buyer: the payment-health arithmetic with their real documented income — this is the branch they almost always sit in.
- Upgrader: the trade-up total account — what the old home sells for, what the new one costs, the *spread* is the real spend.
- Investor: skip comfort framing entirely; give the rent-to-price and holding-cost account (Part 4's tool hooks) and let the numbers carry it.

### 1.3 Branch B — fear of overpaying → decompose where the premium sits

> "You feel it's pricey — fair, so let's take it apart and see *where* the money goes. At the same price point, {{competitor}} gives you {{their specification}}; we give you {{our specification}}. That's not a gap of {{X}} — that's a gap of {{the concrete difference, named}}. Put the two delivery standards side by side — here, I'll print both — and after you've read them you won't need me to tell you which one you're buying."

**Failure warnings:**

- ❌ Answering "it's expensive" with *feelings* ("our brand is worth it") — value claims without a side-by-side comparison are noise; the customer came to compare, so compare.
- ❌ Dismissing the rival instead of the difference ("they cut corners over there") — competitor bashing (red line 4) collapses your credibility faster than any price objection.
- ✅ The comparison must be *materially specific*: delivery standard, building separation, usable-area ratio, management fee. Pull the competitor's facts from a `competitive-intel-sop` walkthrough report with a collection date — never from folklore or from what the customer claims the rival's salesperson said.

**Segment variants:**

- First-time buyer: translate specifications into daily-life consequences, not spec-sheet rows.
- Upgrader: the premium usually sits in public-realm quality and layout efficiency — walk both, don't tabulate alone.

### 1.4 Branch C — bargaining habit → receive it, don't take the bait

> "Understood — everyone wants the real price. So here's my one sentence on price: this project prices unit by unit, and every discount is written, approved, and on the record — what I'm quoting you *is* the best price that exists for this unit, and I can put that in black and white on the subscription form. Which means the smarter game is this: with the same budget, let me find you the *better unit* — a better floor, a quieter side, a better view. Let me go to work there instead."

**Failure warnings:**

- ❌ Inventing a discount to close the negotiation — under approval-controlled discounting, the paper trail catches up; the refund-and-complaint cycle is worse than losing the deal today.
- ❌ Getting defensive ("this price is already very fair") — the customer isn't attacking the price, they're opening a ritual. Receive it warmly, state the mechanism once, redirect to unit selection.
- ✅ If a genuine promotion window exists, say so precisely: what it is, what it covers, when it ends per the published terms — windows on the record are legitimate urgency; invented windows are red line 1.

---

## Part 2 — "I'll look around / let me think about it."

> The polite exit. **"Let me think"** is rarely about thinking — branch A needs better material, branch B needs the family in the room, branch C needs time and a channel. All three need a *hook that brings them back*, because the deal is won on the second visit, not argued into existence on the first.

### 2.1 The worry branch table

| Branch | Real worry | Signals that give it away |
|--------|-----------|--------------------------|
| **A — Under-informed** | Hasn't seen enough to decide | Cannot name one concrete worry when asked directly |
| **B — No authority** | The family hasn't agreed | "I need to discuss it with my family back home" |
| **C — Not motivated** | The current home still works | "The current place is fine, honestly" |

### 2.2 Branch A — under-informed → arm them, then send them off

> "You *should* look at more projects — nobody should rush a home purchase. Before you go, take this: a comparison sheet of {{this project vs the other developments selling in the district}} with the real numbers filled in, so you're not scribbling notes at every sales office. And when you've seen them, come back — whether or not you buy here, we'll go through whatever you found, point by point, and I'll tell you honestly where they beat us."

**Failure warnings:**

- ❌ Interrogating "so what exactly is your concern?" when they have none yet — pressure produces a fake objection, and you'll spend the rest of the visit answering the wrong one.
- ✅ The take-away comparison sheet is the move: it converts the visit they *will* make to rivals into a visit *back to you* to discuss it. Draft it honestly, including your own weak rows — the customer will verify anyway (see `sales-talk-library` Part 4.2 for the table's construction).

### 2.3 Branch B — no authority → book the family second visit now

> "This is a family decision, absolutely right. How about this weekend you bring everyone along? I'll prepare the part your family will care about most — {{school route for the child / hospital access for the parents}} — as a proper information pack, so you can see everything in one trip instead of relaying my words at the dinner table, where everything gets distorted."

**Failure warnings:**

- ❌ "Your family doesn't get a vote — you're the one who lives here" — pitting the customer against their own household. This is a complaint-grade sentence and a reputation wound that outlives the deal.
- ✅ The second visit with the family present is the highest-value appointment on the sales floor; book it with a date and a prepared agenda, not a vague "come back anytime".

### 2.4 Branch C — not motivated → don't push, plant the hook

> "If the current place still works, keep it working — watch the market at your own pace. Let's stay in touch on WeChat: when something real moves in this district — a good re-sale listing, a policy change that touches buyers — I'll send it over. Think of me as a free pair of eyes on the market, and use me whenever you like."

**Failure warnings:**

- ❌ Manufacturing urgency at a customer who has just told you they feel none ("this really is the last chance") — red line 1, and self-defeating: they'll discount everything else you said.
- ❌ Letting them walk out with *no* channel open. This is not a wording problem — it is an execution failure. No WeChat, no second visit, no deal, ever. The hook is mandatory even when the customer seems furthest away; unmotivated today means the district's next price move brings them back, *if* you are the one who tells them about it.

**Segment variants:**

- First-time buyer: hand them the comparison sheet *plus* how to verify things themselves (filing records, catchment announcements) — being armed builds the trust that returns.
- Upgrader: schedule the family visit around the upgrade point that actually hurts today (the school run, the ageing bathroom, the parking queue).
- Investor: send the district's monthly market brief (the `competitive-intel-sop` monthly report output) and nurture on a quarterly rhythm — investors move on numbers, and the numbers arrive monthly.

---

## Part 3 — "What if the project stalls / fails to deliver?"

> A **trust problem wearing a price costume** — no price argument touches it, and any verbal guarantee makes it worse. The only path through is the evidence chain: show documents, invite verification, and let the customer check rather than believe. The Chinese presale system gives you four verifiable layers; use the ones this project genuinely has, in this order, and stop claiming beyond them.

### 3.1 The four-layer evidence chain

> "That worry is completely reasonable — everyone buying today should ask it. I'm not going to pound my chest at you; I'm going to show you things you can check.
> **① The escrow account.** Your money goes into the presale-funds supervision account at {{supervising bank}} — {{the local regulatory rule, cited}}. Funds are released to the developer by construction milestone, not on request; that's the government's framework, not our policy.
> **② The actual progress.** Here is last month's site photo set (show it), and the site perimeter is open for you to walk any time — count the cranes yourself.
> **③ Our delivery record.** {{Developer}} has delivered {{delivered projects}} locally. Walk into those estates and ask the owners — that beats anything I can say.
> **④ The contract.** The delivery date and the delay-liability clause are written into the contract — {{article reference}} — black on white, enforceable.
> Check all four layers. When you're satisfied, *then* we talk about the next step."

**Banned wording:**

- ❌ "This project absolutely cannot stall" — any absolute guarantee (red line 2). The moment a customer repeats your guarantee to a lawyer or on social media, you own it.
- ❌ "The escrow account is a safe deposit box" — overstates what supervision covers; describe the milestone-release mechanism accurately and let its real strength do the work.
- ❌ Deflecting ("let's talk about the floor plans instead") — the customer reads evasion as confession, and the objection walks out the door with them, stronger than it came in.

**Segment variants:**

- First-time buyer: walk the whole chain — delivery risk is their single largest fear and they have usually read the horror stories.
- Upgrader: the delivered-project site visit is the decisive layer — arrange it, don't just mention it.
- Investor: frame delivery certainty as the precondition of the asset's liquidity — an undeliverable project has no rental income and no exit; then the developer's local delivery record is the data point.

---

## Part 4 — "Will prices drop further? Am I buying at the top?"

> The fear of buying-then-watching-it-fall. The answer core: **facts and mechanisms only, predictions never.** You do not know where the market goes, and saying so honestly is the only position that survives being checked later.

### 4.1 The facts layer — the price record is public

> "I understand — nobody wants to buy and watch the price fall. So let's look at facts, not feelings: this project launched at {{X}} in {{year}}, and the price today is {{Y}}. The filed price list and the transaction record are public and checkable — I'll pull them up right now, and whether that trajectory comforts you or worries you, you judge it on the data, not on my assurances."

### 4.2 The mechanism layer — how pricing actually works here

> "Here's how our pricing mechanically behaves: unit-by-unit filed prices, and every discount approved in writing — the price I'm quoting you goes on the subscription form, black on white. If there's a promotion window, its terms and dates are on the published terms, not whispered. If pricing genuinely adjusts later, it follows the published filing and contract terms. I won't paint you a picture of guaranteed rises, and I won't scare you either — the mechanism is the message."

### 4.3 The owner-occupier reframe (owner-occupiers only)

> "One honest sentence, and it only applies if you're living in it: you're buying a home for ten years. In ten years the curve will have gone up and down, and none of it will touch your life — what touches your life is whether the light in the living room is good, whether the school run works, whether the neighbours are decent. Investors stare at the curve; residents live in the floor plan. If you're buying the curve, you should price it like an investment and read the numbers below. If you're buying the decade, the curve was never the product."

### 4.4 The trade-up double edge (trade-up buyers only)

> "And if you're trading up, the fear mostly cancels itself: if prices fall, your old home falls with them — you sell in the same market you buy in. What you actually gain or lose is the *spread* between the two, and the spread is far more stable than either price alone. The move that loses money is waiting for a perfect bottom on the sale while the purchase target drifts out of reach — timing two markets at once is harder than timing one."

**Banned wording:**

- ❌ "Prices rise next month — buy now or you're standing on the high platform" — market prediction *plus* threat pressure, a double red-line breach in one sentence.
- ❌ "It won't fall — we guarantee the value" — false guarantee (red line 2); no developer can underwrite a market.
- ❌ "If it falls we'll refund you the difference" — a verbal promise no approval process will ever honour; when it isn't, the refund demand lands on you personally.

**Tool hook — for the investor who *is* buying the curve, don't argue; hand over the actual returns arithmetic and let the verdict land:**

```bash
# Rent-to-price: gross and net yield, payback horizon, against benchmark lines (verified command):
python3 skills/calc-toolkit/rent.py --price 1500000 --rent 4500 --net
```

Real output for this case: price-to-rent ratio 1:333, gross yield **3.60%/year**, net yield **2.75%/year** after vacancy, tax, and maintenance — below the 3% rent-payback line, above the deposit benchmark, and the tool's own verdict prints as "owner-occupancy first, rent as a supplement". That is exactly the honest answer an investor objection needs, computed rather than asserted.

```bash
# Full annual holding cost incl. the invisible opportunity cost of the capital (verified command):
python3 skills/calc-toolkit/holding.py --area 100 --property 2.5 --price 1500000 --rent 4500
```

Real output for this case: cash costs 3,000/year (management fee), capital-opportunity cost 23,250/year, **full cost 26,250/year ≈ 2,188/month**; on the rental side, net cash flow 46,012/year ≈ 3,834/month after tax and agency. Show investors both lines: the yield they'd earn *and* the all-in cost of holding — then the "risk is yours to weigh" line is not a dodge, it is arithmetic.

**Banned wording (investor track):**

- ❌ Any "guaranteed rental yield / risk-free" framing — red line 2 plus red line 5. Investment answers end with the numbers and the sentence "the risk is yours to weigh", and nothing beyond them.

---

## Part 5 — Second-layer objections (the quick index)

> The four objections above carry most of the traffic; these six arrive steadily and each has a *direction* of handling. The full scripts live in the sibling skills named in the right column — this index only decides where to go.

| Objection | Handling direction | Full script lives in |
|-----------|-------------------|---------------------|
| "It's too far out" | The measured commute account (door-to-door, at the hour they actually travel) + district development facts, three states kept separate | `sales-talk-library` Part 1 |
| "Don't like the floor / orientation" | The alternative-unit method (move them to a concrete alternative) + the price-difference trade method (what the downgrade saves, itemised) | `sales-closing-sop` |
| "The management fee is high" | Fee × service list, item by item; then the delivered-phase property walk to see what the fee buys | `sales-talk-library` Part 5.2 |
| "What school does it feed?" | The promise-nothing formula: historically published catchment + on-site facility progress + "the current year's announcement governs" | `sales-talk-library` Part 1.3 |
| "The other project is cheaper" | Objective difference comparison only, from a dated `competitive-intel-sop` walkthrough — acknowledge their real strength first | `sales-talk-library` Part 4 |
| "My family is against it" | The family decision map — who actually holds which veto, then handle each person's worry separately; family objection is frequently the *real* objection wearing the "too expensive" costume | `sales-reception-sop` (needs map) + family second visit (Part 2.3 above) |

---

## Practice mode (drill with AI as the customer)

For training, run this playbook as a sparring kit: instruct the AI to play a customer — pick a segment (first-time buyer / upgrader / investor), pick one of the four primary objections *or* one from the index, and pick a pressure level. The consultant responds live; the AI then scores the response on three axes: **branch correctness** (did they diagnose A/B/C before answering?), **three-stage completeness** (receive → dissect → redirect-with-evidence-and-next-step), and **red-line audit** (flag verbatim any sentence that threatened, guaranteed, invented data, bashed a competitor, or minimised debt). The AI should also play the *follow-up*: "you said you'd check and get back to me" — because the promise-to-verify is where trust is actually won or lost. One round per objection is enough to expose a new hire's habitual breaches; log the exposed breaches as the trainee's personal banned-wording list for the next round.

## Relationship to the other skills

- **Reception and needs discovery** → `sales-reception-sop` — objections answered before the needs map exists are answered blind.
- **Standard wording for the branches** → `sales-talk-library` (value comparison 1.3, competitor handling Part 4, school formula 1.3, fee walk 5.2).
- **Price calculation and the closing push** → `sales-closing-sop` — when the objection dissolves, the closing moment belongs there, not here; resolving an objection and then going silent is this playbook's definition of a wasted resolution.
- **Competitor facts** → `competitive-intel-sop` walkthrough reports are the only permitted data source; every competitor claim in a response must carry a collection date.
- **Loan structure and approval** → `sales-mortgage-sop` — payment arithmetic comes from `calc-toolkit` (`mortgage.py`, `rent.py`, `holding.py`), never from memory; policy numbers are never stored in this playbook.

No policy numbers and no legal conclusions live in this playbook: anything regulatory — underwriting guidelines, escrow rules, catchment announcements — is checked against the current local announcement on the day it comes up.
