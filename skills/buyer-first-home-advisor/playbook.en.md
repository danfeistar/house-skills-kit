# First-Home Buyer Advisor · Playbook (English Edition)

> This playbook is for people buying their **first home** — how to get from "I think I want to buy" to a defensible "buy / don't buy / keep looking" decision. The sales-side counterparties (reception scripts, lead grading, closing pressure) live in the `sales-*` skills; resale brokerage workflow lives in the `broker-*` line.
> Every number in the worked examples is an **illustrative assumption**. Actual policy numbers (rates, tax brackets, down-payment minimums, provident-fund ceilings) differ by city and change over time — always check the current local announcement. Anything that can be calculated should go through `calc-toolkit`, never mental arithmetic.

> **A note for English readers.** This is a Chinese-market playbook by design: it encodes how the transaction actually works in China. China-specific mechanics are kept and explained inline — hukou (户口, household registration), the five certificates (五证) a new development must display, provident-fund loans (公积金, a subsidized housing loan funded by mandatory employer+employee deposits), maintenance fund (维修基金, a one-time common-area repair levy), school-place occupancy (学位占用, whether the previous owner's child has already used the slot tied to the property), and the sales-control board (销控表, the office board showing which units are genuinely still available). One practical warning: the city rule library keys on **Chinese city names** — `--city 昆明` resolves to the Kunming tier, while an unrecognized name such as `--city Kunming` silently falls back to the national default tier. Use the Chinese name (or `--set key=value` overrides) when you want city-specific brackets.

---

## Part 1 Clarify the need: the seven questions

### 1.1 Name the problem before naming a property

When a first-time buyer says "I want to buy a home," the real problem underneath is usually one of five — **and each motive leads to a different correct answer**:

| Real motive | Tell-tale signals | What should dominate the choice |
|---|---|---|
| Live better (upgrade in place) | Current home is cramped / far / noisy, and they can name the pain precisely | Commute, floor plan, daylight, property management |
| School place for a child | A hard enrollment deadline within ~3 years | School-place certainty beats everything; accept a smaller home |
| Marriage / starting a family | A wedding date or a family plan | Delivery date, commute workable for both partners, controllable total price |
| Retirement / aging parents | Focus on hospitals, elevators, floor level, accessibility | Hospital radius, low floor, mature neighborhood |
| Fear of idle cash / everyone else is buying | No specific dissatisfaction, only talk of "prices will rise" | **Pour cold water first**: run holding cost and liquidity math before emotion sets the budget |

**Action:** open with one question — *"In your current home, what bothers you the most?"* It works ten times better than "what are you looking for?"

**Failure warnings:**
- ❌ "Just browsing" is treated as a green light to pitch units — the problem hasn't been named yet, so more pitching only adds noise
- ❌ "Afraid of missing out" is treated as a genuine housing need — these buyers are the most likely to over-leverage

### 1.2 The seven questions (ask them in one pass, not ten rounds)

| # | Question | What the answer must pin down |
|---|---|---|
| 1 | **Who lives here?** How many people, what relationship, and how will that change within 3 years (marriage / a child / parents moving in)? | Hard requirement on bedroom count |
| 2 | **How long will you stay?** Any move likely within 5 years (job change, school progression)? | Whether "good enough" is acceptable, and how liquid the asset must be |
| 3 | **Commute?** Both partners' workplaces, transport mode, tolerable one-way minutes | A hard geographic boundary — draw it *before* viewing, not after falling for a showroom |
| 4 | **Children?** Any now, ages, school-place needed, open to transferring schools? | School districts are where first-time buyers hit their first non-negotiable |
| 5 | **Money?** How much down payment can actually be assembled, what monthly payment is survivable, any existing debt? | Feeds Part 2's three-line budget — do **not** quote a total price here |
| 6 | **The one thing you will not compromise?** Only one allowed | Breaks the deadlock of "we want both projects" |
| 7 | **The one thing you cannot accept at all?** A deal-breaker on sight | Eliminates candidates faster than adding up pros |

**Worked example** (a couple, first purchase):
- Who lives here: the couple + a child planned within a year → at least two bedrooms, ideally a compact three
- How long: ~8 years (no move before primary school) → school-place weight goes up
- Commute: husband's workplace fixed, wife may change jobs → husband's commute becomes the hard constraint
- Non-negotiable: **total price must stay under the ceiling line** (one income could stop)
- Deal-breakers: ground floor, north-facing, no elevator (elderly parents visit)

**Failure warnings:**
- ❌ Seven questions stretch into ten rounds of interrogation and the buyer loses patience — at most 2 questions per round, and every round must end with one useful conclusion
- ❌ Asking "how big?" without asking "who lives here?" — household change over the next 3 years is the biggest hidden risk of a first purchase

### 1.3 Forced-choice exclusion (faster than a questionnaire)

For buyers who "can't say what they want," replace open questions with **either-or eliminations**:

1. "Same budget: a **small home near work**, or **one more bedroom farther out**?"
2. "If you can only keep one: **the school place** or **the commute**?"
3. "A **new home with a two-year wait**, or a **resale you can move into now**?"
4. "A **lower total price but tight space**, or a **higher total price that fits for good** — which squeezes harder?"

Four either-ors later the outline of the need is on the table — **elimination reveals true preference better than description does**.

---

## Part 2 The three-line budget

### 2.1 Three lines, not one number

| Line | Definition | What it is for |
|---|---|---|
| **Comfort line** | Payment ≤ 35% of household monthly income, and an emergency fund ≥ 6 months of expenses | The preferred zone; a genuinely good home inside it deserves a fast decision |
| **Ceiling line** | Payment ≤ 45% of income, emergency fund ≥ 3 months | The hard ceiling. Above it, walk away |
| **Extreme line** | Every lendable yuan used, emergency fund near zero | Exists only to tell you **"never get here"** — it is not a budget |

**Action** — back-solve an affordable total price from real income and debts:

```bash
# Income/debt → max loan → max affordable price (dual bank-style ratios, bottleneck diagnosis)
python3 skills/calc-toolkit/capacity.py --income <income_a>,<income_b> --cash <cash> --debts <monthly_debts> --city <city>
```

The output diagnoses the bottleneck: **is the down payment the binding constraint, or the monthly payment?** The two call for opposite moves — a cash bottleneck means save more or lower the target price; a payment bottleneck means lower the price or stretch the term (with the interest cost made explicit).

Concrete demo (illustrative numbers, verified to run):

```bash
python3 skills/calc-toolkit/capacity.py --income 12000,8000 --cash 400000 --debts 1500 --city 昆明
```

**Worked example (assumptions):** household income 20,000/month, cash 400,000, existing debt payments 1,500/month, under a given city's tiers:
- Comfort line ≈ payment 7,000 → affordable price band A
- Ceiling line ≈ payment 9,000 → band B
- Conclusion: **shop inside band A. Never negotiate against band B as your budget** — closing in A is a win; closing in B is self-inflicted stress

**Failure warnings:**
- ❌ Treating the extreme line as the budget — the classic first-buyer blow-up (one job loss and the loan defaults)
- ❌ Counting the provident-fund loan ceiling as "extra budget" on top of the commercial loan — the two must be computed as one combined structure, not stacked

### 2.2 The down payment is not the whole cash bill

Four items first-time buyers most often miss:

| Item | Order of magnitude | Notes |
|---|---|---|
| **Taxes** | Deed tax dominates; see `tax.py` / `newhome.py` | Resale may add income tax and VAT; new homes add the maintenance fund |
| **Agency / appraisal / guarantee fees** | Common on resale; local rates apply | Who pays which fee is itself a negotiation point |
| **Renovation + appliances** | Universally underestimated | Bare-shell units and compact three-beds are the worst cases — don't hide renovation money inside the down payment |
| **Emergency fund + moving-overlap costs** | ≥ 3–6 months of household expenses | Default-buffer money. Not negotiable, not spendable |

**Action:** `assembled cash − taxes − renovation − emergency fund = money that can actually serve as down payment`, then feed the remainder to `capacity.py`. The tool has a dedicated flag for this — `--reserve` deducts the set-aside before computing the down payment:

```bash
python3 skills/calc-toolkit/capacity.py --income <income_a>,<income_b> --cash <cash> --reserve <taxes_renov_emergency> --debts <monthly_debts> --city <city>
```

**Failure warnings:**
- ❌ Scraping together exactly the minimum down-payment percentage and charging in — not one yuan left for taxes or renovation, borrowing money the month of handover
- ❌ Down payment sourced from personal loans or consumer credit — most banks trace the source of funds, it inflates your measured debt load, and it can sink approval from both directions

---

## Part 3 Eligibility and policy self-check

### 3.1 Three checks before viewing anything

1. **Do you hold purchase eligibility at all?** (purchase restrictions, social-security or income-tax contribution years, hukou requirements) — check the local housing authority's current announcement
2. **First home or second?** — and note that China determines this on **three independent tracks that may disagree**: the commercial-loan test, the provident-fund test, and the deed-tax test. A city may "recognize the home but not the loan" (认房不认贷): a paid-off loan elsewhere doesn't block first-home loan treatment, while a currently-owned home does
3. **How much and how long can you borrow?** (age + term caps, property-age limits, the four provident-fund caps)

```bash
# First/second-home status, three independent tests (incl. sell-one-buy-one chaining)
python3 skills/calc-toolkit/status.py --city 昆明 --local-homes 1 --area 89
# Provident-fund limit = minimum of four caps: ceiling / price ratio / repayment ability / balance × deposit months
python3 skills/calc-toolkit/fund.py --balances 50000 --months 36 --price 1500000 --city 昆明
```

Both flags sets are real: `status.py` also takes `--prior-loans` (lifetime housing-loan records, settled included), `--selling` (units sold simultaneously — the sell-one-buy-one case), and `--price` (to print a down-payment figure). `fund.py` takes `--family couple` (dual-depositor household, the default), `--spouse-months`, and `--boost multi_child,green` for the multi-child / green-building uplifts where local policy allows them.

**Failure warnings:**
- ❌ Building the whole budget on a salesperson's "you count as first home" — the deed-tax track and the loan track can classify you differently
- ❌ Assuming the provident-fund loan at its headline maximum — the limit is the **minimum** of four caps; balance and deposit duration both shave it down

### 3.2 How to check policy (this skill deliberately ships no numbers)

| What to check | Where |
|---|---|
| Purchase/resale restrictions, social-security years | Local housing & urban-rural development bureau / housing administration site, government service portals |
| Loan-to-value and rates | Local central-bank branch guidance + the specific bank's mortgage desk (the bank's answer governs) |
| Deed tax, VAT, income tax | Local tax bureau / 12366 hotline |
| Provident-fund limits and rate | Local provident-fund center site / official account |
| School catchment boundaries | District education bureau, published annually — **the current year's document governs** |

**Iron rule:** every policy number must be traceable to a publishing body and a date. If it can't be traced, it is "unverified" and must not enter a decision.

---

## Part 4 Location and project screening

### 4.1 District first, project second (reverse the order and you will regret it)

Five screening dimensions for the district — one sentence of conclusion each:

| Dimension | The question to answer | How to check |
|---|---|---|
| **Commute** | What is the *real* rush-hour door-to-door time? | Walk it once at the actual hour; never trust off-peak map estimates |
| **Amenities** | Market / hospital / school / metro — **built** or promised? | Only built amenities count; flag planned ones separately as "not delivered" |
| **Supply pipeline** | How much new construction and land in the next 3 years? | Oversupply means thin resale liquidity later |
| **Plan certainty** | Metro / school / hospital: **under construction** or "in the plan"? | Government public notices (公示) > sales-center model > salesperson's word — verify the document, not the slideshow |
| **Resale liquidity** | How long do resales in this district sit before closing? | On resale platforms, look at days-on-market and price-cut counts |

**Failure warnings:**
- ❌ Being wowed by the sales-center model first, then talking yourself into accepting the commute
- ❌ Counting a "planned metro line" as "has metro" when pricing the unit

### 4.2 The 100-point scorecard

Score each candidate 0–10 per item, multiply by weights. **Fix the weights before scoring** — otherwise the weights get reverse-engineered to make the preferred project win.

| Item | Weight (example) | Scoring notes |
|---|---|---|
| Commute | 25 | True door-to-door minutes, transfer walking included |
| Price & value | 20 | Interior-area unit price, vs. district comparables (`efficiency.py` prevents the "cheaper per gross sqm" illusion) |
| Product quality | 15 | Floor-plan regularity, efficiency ratio, elevator-to-unit ratio, orientation, noise |
| School / amenities | 15 | Built amenities only; school place per the current year's document |
| Developer & delivery | 10 | Delivery track record, construction-fund escrow, existing-shell or near-complete preferred |
| Liquidity | 10 | District supply pipeline + resale days-on-market |
| Property management | 5 | Fee level and service reputation |

**Action:** compute weighted totals, then run a **sensitivity check** — double the top weight and see whether the ranking flips. If it flips, you don't actually have a ranking; go back to Part 1's non-negotiable to break the tie.

Concrete demo (interior-area unit-price comparison of two projects):

```bash
python3 skills/calc-toolkit/efficiency.py --mode compare --label-a ProjectA --rate-a 80 --price-a 15000 --label-b ProjectB --rate-b 72 --price-b 13800
```

### 4.3 New home vs. resale

| Dimension | New (off-plan or fresh) | Resale |
|---|---|---|
| Delivery | Off-plan carries delay / abandonment risk — check construction-fund escrow and developer standing | Existing shell; what you see is what you get |
| Price | Published price minus discounts; relatively transparent | One price per unit; negotiated |
| Cash costs | Deed tax + maintenance fund + first-year property fee | Deed tax + income tax/VAT + agency fee + possible re-renovation |
| School place | Promises often not yet landed; verify against education-bureau documents | Place already attached to the unit (verify current-year rules) |
| Negotiation room | Mostly in discounts and parking | In the total price and who bears the taxes |
| Suits | Can wait ~2 years, values newness and estate quality | Needs to move in now, wants school certainty, budget-sensitive |

**Failure warnings:**
- ❌ Imagining the "fully fitted" delivery from the show flat — the contract's fit-out standard and brand list is the only evidence
- ❌ Comparing resale total prices without checking who bears the taxes — the same unit swings tens of thousands of yuan on that single clause

### 4.4 Floor, orientation, efficiency ratio — the three frequent misjudgments

- **Efficiency ratio (得房率):** never compare gross-area unit prices; compare **interior-area unit prices** — `efficiency.py` converts across gross ↔ interior ↔ shared area chains (note `--use-coef` takes a decimal: 0.88 = 88%)
- **Floor pricing:** validate "raise-then-discount" games with `floor.py` — stacked discounts (`--d 98` for a 2% cut, repeatable for discount-on-discount) against the filed baseline; pass `--baseline` to expose a nominal anchor price used for baiting

```bash
python3 skills/calc-toolkit/floor.py --price <base_unit_price> --area <area> --floor <floor_no> --top <total_floors> --d 98
```

- **Orientation:** daylight differs sharply between buildings in the same estate — view the two units **within the same hour** (e.g. both at 4 pm)

---

## Part 5 Viewing and verification

### 5.1 The new-home five checks

| Check | What to land on |
|---|---|
| **Certificates** | All five displayed (五证), above all the **pre-sale permit** — its number must match the exact building being sold |
| **Construction site** | Build progress, materials on site, any sign of a work stoppage |
| **Show flat** | Shrunk furniture, missing doors, removed walls — bring a tape measure; ask outright "is this 1:1?" |
| **Published disclosures** | Price list, sales-control board, discount rules — on display and checkable, not just spoken |
| **Contract annexes** | Fit-out standard, delivery standard, breach clauses, whether parking/storage is force-bundled |

**Failure warnings:**
- ❌ Photographing the pretty bits without checking certificate numbers — the most expensive laziness there is
- ❌ "Only two units left" as a reason to sign — the sales-control board is checkable; never buy off a spoken claim

### 5.2 The resale 15-minute inspection checklist

1. Walls / ceilings: water stains, mold (hot spots: the wall outside the bathroom, balcony ceiling, bay window)
2. Bathroom & kitchen drainage flows freely, no smell backing up
3. Water pressure (two taps at once), water-heater age
4. Electrical: breaker-box circuit count, independent RCD, grounded sockets
5. Doors & windows: swing, seals, double glazing
6. Daylight: view once morning, once afternoon; note the facing building's distance
7. Noise: facing the street / equipment floor / elevator shaft
8. Ceiling height and beam positions (affects suspended ceilings and wardrobes)
9. Area: measure interior dimensions on site, reconcile against the title certificate
10. Title: certificate matches the seller's ID, all co-owners identified, **mortgage / seizure status verified at the real-estate registration center** — this one cannot be skipped or delegated to "the agent says it's clean"
11. Hukou: seller's household registration moved out (write the deadline and penalty into the contract)
12. Property arrears: management fee / utilities / gas / heating settled
13. School place: **has the previous owner's child already consumed the slot?** (ask the school or the district education bureau directly)
14. Alterations: illegal extensions or structural changes (you will be ordered to restore them)
15. Neighbors & building: tenant mix, any group-rental or in-home business

**Failure warnings:**
- ❌ Admiring the renovation and skipping the water-stain hunt — fresh renovation covering seepage is the most common resale trap
- ❌ Trusting verbal "clean title" — mortgage and seizure must be verified by you, at the registry

---

## Part 6 Negotiation and signing

### 6.1 New-home: leverage beats scripts

**Usable leverage**, strongest first: full cash or a high down payment · fast payment schedule · no fuss about floor or orientation · accepting the parking/storage bundle · signing this month.

**Flow and points:**
1. Get the **published price list and written discount rules** (paper or photo) before talking numbers
2. Discounts split into the **public discount** and the **one-off incentive** — write both into the subscription agreement separately
3. The subscription agreement (认购书) must state: **is the deposit refundable, under what conditions, in how long**; delivery date and breach terms
4. Never accept a bundled parking/decoration package "for the discount" — convert everything to one total price and compare

**Failure warnings:**
- ❌ Verbal incentives that never make it into the contract — once signed, they never happened
- ❌ Paying a large deposit to "lock the discount" before the refund clause is written — the money is now locked, the discount is not

### 6.2 Resale: negotiate on three lines

1. **Price line:** anchor on closed deals in the same estate from the last 3 months (closing prices, not asking prices)
2. **Tax-bearing line:** who bears the income tax / VAT / agency fee — often easier to win than a headline price cut, and worth just as much
3. **Handover line:** appliances and furniture staying, maintenance-fund balance, property fees settled, hukou move-out deadline

**Action:** negotiate "total price − who bears taxes − what stays − handover date" as **one package**. Item-by-item concessions get you led by the nose.

### 6.3 Ten clauses to check in every contract

1. Property location, area (gross / interior), title certificate number and registration record all consistent
2. Price, payment schedule with per-installment amounts, and what happens if the loan is not approved
3. Who bears taxes and agency fees
4. Handover date and delivery standard (new home: fit-out and equipment list attached)
5. Hukou move-out deadline and penalty (resale)
6. How a consumed school place / school promises are handled
7. Deadline and responsibility for releasing mortgage / seizure
8. Area-difference treatment (new home: the true-up rule, and the statutory threshold that lets the buyer rescind)
9. Breach clauses — symmetric for both sides, penalty rate stated
10. The legal nature of the deposit (定金, forfeitable) vs. booking money (订金, refundable) and refund conditions

---

## Part 7 Loan and disbursement

### 7.1 Compare structures, not slogans

```bash
python3 skills/calc-toolkit/mortgage.py --price <total_price> --downpay <pct> --years 30 --city <city>   # commercial / provident / combined × installment / principal
```

`mortgage.py` takes `--combo <provident_principal>` to price a combined loan (commercial + provident-fund tranches side by side) and `--mode commercial` or `--mode provident` for single-mode runs. Compare three things: **monthly-payment gap, total-interest gap, prepayment flexibility**. The classic first-buyer mistake is choosing by lowest monthly payment while ignoring total interest and the term being locked.

### 7.2 Statements and credit — prepare 6 months ahead

- **Bank statements:** most banks read the last 6 months; stability beats size, and a sudden large inflow invites questions
- **Credit record:** consumer-loan apps, credit-card installments, guarantees all count as debt; add nothing new in the 3–6 months before applying
- **Source of down payment:** borrowed funds, credit-card cash-out, diverted consumer loans are poison — outright rejection or forced early repayment
- **Co-borrower:** parents co-repaying raises capacity, but check the age-at-maturity term limit it triggers

### 7.3 Early repayment

```bash
python3 skills/calc-toolkit/prepay.py --loan <original_principal> --rate <rate_pct> --years 30 --paid <months_paid> --prepay <amount>
```

Two routes: **shorten the term** (more interest saved) vs. **reduce the payment** (more monthly relief). First confirm any prepayment penalty and minimum-amount rules — `prepay.py` reads them from the city tier and takes `--set penalty_rate=0.01`-style overrides.

**Failure warnings:**
- ❌ Comparing monthly payments while ignoring total interest — over 30 years that gap is six figures of yuan
- ❌ In a combined loan, forgetting the provident-fund tranche has its own term and ceiling limits

---

## Part 8 Handover and taxes

### 8.1 New-home handover inspection

- Bring: tape measure, flashlight, socket tester, phone (photograph everything, continuously)
- Order: entry door → walls & floors → water & electrical → doors & windows → kitchen/bath waterproofing → balcony & envelope
- Every defect goes on the **written handover defect list** with a signature required — never accept "sign first, we'll fix later"
- Area differences follow the contract's true-up rule (refund/charge the difference; beyond the statutory threshold the buyer may rescind)

### 8.2 Taxes and the cost of holding

```bash
python3 skills/calc-toolkit/newhome.py --price <total_price> --area <area> --city <city>   # new: deed tax / maintenance fund / first-year property fee
python3 skills/calc-toolkit/tax.py --price <total_price> --area <area> --city <city> --first 1 --held <years_held> --unique 1   # resale
```

Concrete demo (illustrative numbers, verified to run):

```bash
python3 skills/calc-toolkit/newhome.py --price 1500000 --area 89 --city 昆明
python3 skills/calc-toolkit/tax.py --price 1500000 --area 89 --city 昆明 --first 1 --held 6 --unique 1
```

(`--held` is the *seller's* holding years on a resale — ≥2 years clears VAT, ≥5 and the only home clears income tax; `--unique 1` marks the seller's only home. These are the general national rules' shape; local brackets still govern — read them off the tool output's source line, not from memory.)

**Action:** amortize first-year holding cost (property fee + heating + parking) into the monthly outgo and **re-run the Part 2 stress test**. Many first-time buyers discover at exactly this step that they could afford to buy but not to live.

---

## Part 9 Common traps and red lines

| Trap | The reality | Counter-move |
|---|---|---|
| **定金 vs. 订金** | "定金" (earnest deposit) is forfeitable; "订金" (booking money) is refundable — the contract's wording decides | Get the nature and refund conditions written into the subscription agreement |
| **Group-buy / e-commerce fees** | Often collected off-book, no invoice | Demand it be counted into the total price with an invoice, every time |
| **Bridged down payment** | Non-compliant and high-risk (discovered → loan rejected) | Refuse; sign nothing resembling a bridging agreement |
| **School-place promises** | A salesperson's spoken promise is not a contract obligation | The education authority's current-year document is the only evidence |
| **Rent-back / guaranteed-lease offers** | Low fulfillment rate, dispute-prone | Never count promised rent-back income into repayment ability |
| **Internal sales before the permit** | Selling without the pre-sale permit is non-compliant; funds are unescrowed | Verify the pre-sale permit before any payment |
| **Dual-price contracts ("yin-yang" contracts)** | Illegal; corrupts your future resale and any future loan | Refuse |
| **Bundled decoration packages** | Priced high, quality unspecified | Convert to total price and compare; strip it out if possible |

**Red line:** the moment a proposed scheme requires faked bank statements, evading purchase restrictions, bridged down payments, or dual-price contracts — **stop and change channel**. That is not a "technique"; it is dumping the entire risk onto the buyer.

---

## Part 10 Close: the three-sentence decision

Collapse the whole analysis into a note you could send yourself:

```
1. Within the price band [band], I am buying a [district/type] home, to solve [the first motive].
2. My non-negotiable is [X], my deal-breaker is [Y]; of the candidates only [A/B] satisfies both.
3. Next action: [verify certificates / view / negotiate / wait for policy], at [time Z]; if [condition] fails, I keep looking.
```

**Decision rules:**
- All three sentences write cleanly → proceed to viewing/negotiation
- Sentence 1 won't write → back to Part 1; the need isn't clear yet
- Sentence 2 won't write → too many candidates; back to Part 1.3 for forced-choice elimination
- Sentence 3 won't write → the timing isn't right; name exactly what you're waiting for — never a vague "keep looking"

**Final word:** a first purchase is not an exam you sit once; it is a liability you carry for up to 30 years. **Rather one fewer bedroom than one more risk.**

---

## Companion files

- `SKILL.md` — the always-read-first instruction card (triggers, core insights, calculator map, six-section writing standard)
- `playbook.md` — the Chinese edition of this playbook (same ten Parts; the source the English edition was written from, not translated line-by-line)
- Calculators used above: `capacity.py` `status.py` `fund.py` `mortgage.py` `prepay.py` `newhome.py` `tax.py` `efficiency.py` `floor.py` — all in `skills/calc-toolkit/`, pure standard library, run `--help` on any of them for the full flag list
