# Closing Playbook · English Edition

> **Scope.** This playbook is the endgame discipline of the sales office: the customer has toured, sat down, and asked for the numbers. It covers the whole chain from the pricing sheet through the concession ladder, the buying-signal read, the five levels of closing scripts, and the subscription hand-off — plus the team choreography (consultant × consultant, consultant × supervisor/manager) when one person alone cannot carry the deal. It deliberately does **not** cover what sits before or after:
>
> - First reception and needs discovery → `sales-reception-sop` (a pricing sheet built on an unclear profile is a sheet for the wrong buyer)
> - The wording that answers *value* objections → `sales-talk-library`; the objection branches themselves → `sales-objection-handling` (an objection that surfaces mid-closing is handled there, then you return here)
> - Loan eligibility, income documents, credit questions → `sales-mortgage-sop`
> - How discount schemes are *designed* and who may break price → `pricing-incentive-release-sop` (this playbook only spends what that skill budgets)
> - The formal contract, title transfer, escrow → `resale-transaction-sop`
> - Registration and long-cycle follow-up after the customer leaves without buying → `sales-lead-grading`

> **A note for English readers.** The mechanics below come from the Chinese new-home sales office and have no clean Western equivalent; they are kept and explained inline. **Unit-by-unit filed pricing with approval-controlled discounts** (一房一价 + 折扣审批制)： every unit carries a price registered with the local housing authority, and any discount — even a small one — requires a written approval from someone who actually holds that authority. This is why the concession ladder in Part 2 is an *organisational* structure, not a negotiating pose: "let me check with my supervisor" is a real workflow with real limits, and customers can verify the filed price themselves. The **sales-control board** (销控) is the office board tracking sold and reserved units; scarcity claims must match it, because customers can and do ask to see it. The **subscription form** (认购单) is the pre-contract sheet — unit, price, discount, payment plan, deposit — signed before the formal contract is filed. The **deposit** (定金) is legally distinct from a mere booking fee (订金/诚意金)： under the Civil Code's deposit penalty rules (Articles 586–588), a *deposit* actually paid is forfeited if the buyer walks away — which is exactly why Part 5 makes honest disclosure of deposit terms a red line. The **red-face / white-face pairing** (红白脸) is two consultants playing firm and friendly in a rehearsed, disclosed-to-the-team way; and the **second visit** (二访) economy means many deals close on a later visit, so a closed-but-unconverted pricing session is a *follow-up asset*, not a failure. Placeholders in `{{}}` are injected by the project's `brand.yaml` via `render.py`; every number a script quotes must be replaced with the live, verifiable figure for that unit and that day.

> **The red lines, up front.** Everything below is written inside these five constraints; check each move against them *before* you make it:
> 1. **Every discount must be genuinely approvable.** Whatever you promise must clear a real approval chain — the supervisor really holds that authority, the amount really is within it. Under-the-table top-ups from commission, invented "special applications", promised-but-unapprovable discounts: all banned.
> 2. **Scarcity must be real.** "Last unit", "only {{X}} left" must be backed by the sales-control board's actual figures. The board is checkable; a fake scarcity claim dies the moment the customer walks past it.
> 3. **No threats, no family wedge.** No "prices rise tomorrow" without a documented price-change decision; no "you decide, don't listen to your family" — that line is complaint-grade.
> 4. **Never soften the debt.** Payment figures come from the calculator, never mental arithmetic, and must never be framed to push the customer past real capacity.
> 5. **Deposit terms stated honestly.** The subscription form's deposit amount and refund conditions are read out loud, as written. "You can always get it back" is a banned sentence.

---

## Part 1 — The pricing-sheet action chain

> The pricing session is not "quoting a price" — it is the first gate of the deal. How you lay the sheet out, what you concede early, and what you hold back decide how much room the negotiation has. A sheet laid out wrong hands the customer the knife before the conversation starts.

### 1.1 The five elements (all five, or the sheet is not ready)

| Element | Content | Point |
|---------|---------|-------|
| **Unit details** | Building / floor / layout / orientation / area | Lock the unit first, then price it — a sheet that drifts between units prices nothing |
| **Price structure** | Unit price × area = total, before and after discount listed separately | Write unit price and total on separate lines; customers accept unit-price logic far more easily than a bare total |
| **Cost sheet** | Down payment / loan amount / deed tax / maintenance fund / misc fees | Tax and fund figures come from the calculator with city rules — never recited from memory |
| **Payment trial** | Loan × rate × term = monthly payment | Trial at the customer's *real* down-payment capacity, not the plan you wish they'd take |
| **Discount record** | Conceded / available / needs-approval, three tiers | Left visible for Part 2's negotiation; the approval tier must be genuinely approvable |

### 1.2 The laying order (the order *is* the psychology)

**Standard flow:** unit details first → unit price × area (so the customer sees the unit price is fair) → total (face the big number squarely) → cost sheet (answers "can we afford to buy" first) → monthly payment (then answers "can we afford to hold") → **discount last** — the discount is the door-kick, not the opening line.

**Standard script:**

> "Let's put the whole account on paper — (write each line) — this is before discount; the discount comes separately, because first I want to know you agree with *this* account. Down payment {{X}}, monthly payment {{Y}} — is that inside your household budget? If yes, I'll arrange the discount on top. If not, we change floor or layout until it fits — we don't force a buy."

**Tool hooks — every figure on the sheet comes from the calculator with the city rules, never from memory:**

```bash
# Full first-purchase cost sheet for a 1.5M / 100 sqm unit, 1.05M loan, Kunming tiers (verified command):
python3 skills/calc-toolkit/newhome.py --price 1500000 --area 100 --first 1 --loan 1050000 --city 昆明
```

The tool prints the whole closing-cost block with per-item sourcing and a rules version date — in this exact case: deed tax 1% = 15,000, registration 80, maintenance fund 90/sqm (Kunming tier) = 9,000, property-fee prepayment 3,000, gas connection 2,800, loan appraisal 1,050, mortgage registration 80 — **mandatory total ≈ 31,010 (2.07% of price)**. Laying this block on the sheet does two things: the customer sees the *real* cash-to-close number, and nobody later argues "you said buying cost nothing extra".

```bash
# Monthly payment, 30% down, 30 years, commercial loan (verified command):
python3 skills/calc-toolkit/mortgage.py --price 1500000 --downpay 30 --years 30
```

The tool prints both repayment structures with the rules-library rate and version date — in this exact case: loan principal 1,050,000, **equal (annuity) payment 4,484/month** (total interest 564,122), **equal-principal 5,629 in month one** declining about 8/month to roughly 2,924 at the end; the annuity-vs-principal interest gap is ≈ 74,516. Quote the annuity figure as the budget-fit number; show the declining structure to customers whose income will grow. If the monthly payment strains the household budget, the honest fix is a different floor or layout — not a discount you cannot approve.

**Failure warnings:**

- ❌ Opening with the discount (the customer's first thought becomes "so there's more room")
- ❌ Quoting only the total with no unit-price line (a bare total has no anchor; the reflex reply is "too expensive")
- ❌ Trialling the payment at minimum down payment (they sign, then discover they can't carry it — the buyback bites later)

### 1.3 Sheet discipline (anti-price-shopping)

- The filled sheet **stays in the sales office** (a sheet in the customer's hand is a price quote touring the whole city): "I'll photograph the sheet for you / copy the numbers down — the original stays with me for the file. One layout, one price: ask anyone on this project, it's the same number."
- Two consultants pricing the same layout must produce **the same number** — one office-wide pricing standard. This is the precondition for every piece of team play in Part 6.
- Any change to a discount tier is written to the shared ledger the same day — two consultants each approving their own version is how price systems leak.

---

## Part 2 — The negotiation ladder

### 2.1 The concession ladder (how much, who grants it, when)

```
Tier 0 (consultant's own authority): gifts / payment-method incentives    — first-round defence, may offer proactively
Tier 1 (consultant's own authority): small cash discount                   — granted when the customer first asks
Tier 2 (supervisor approval):       medium cash discount                  — "let me check with my supervisor" exit
Tier 3 (manager approval):          large discount / special approval      — the endgame for a hesitating customer
```

**Discipline: release tier by tier, one step at a time, and every step is exchanged for a commitment** ("I fought for this step — sign today and it's locked in"). Concede everything at once and the customer concludes there's still more, walks, and comes back to cut again.

### 2.2 What to concede, and in what order

- **First payment-method incentives** (the one-off vs instalment incentive wording — per the real policy) → **then gifts** (parking vouchers, appliances, property-fee credits — real inventory only) → **cash discount last** (real money moves last, through the approval chain).
- **Failure warning:** ❌ leading with cash burns the whole hand in one card; ✅ cash stays at the final step, behind an approval.

**Standard script (first price push):**

> "You've just sat down and you're asking me to move the price — at my level I genuinely can't move it much. What I *can* do right now is {{gift/payment incentive}}, and that's real value. If you're serious about a cash discount, I'll take the sheet upstairs to my supervisor — but let me ask one thing first: if it gets approved, can you sign today? If yes, I'll take it up. If no, I won't — because upstairs won't sign off on a maybe." (**Lock the commitment first, then walk the approval.**)

### 2.3 The approval chain (a real process, not theatre)

**Standard flow:** customer asks beyond your authority → consultant confirms verbally "if approved, today" → exit (no more than {{X}} minutes) → real check with the supervisor (the supervisor confirms what they can actually approve) → return with the result, supervisor joins if needed → state exactly what was approved, reveal nothing about the ceiling.

**Standard script:**

> "That's beyond my authority — let me take it to my supervisor. Give me {{X}} minutes." (Exit.) Returning: "Your sheet went through — approved {{X}} off. That's the number on his desk; anything lower means a company special-approval process that won't clear today."

**Failure warnings:**

- ❌ The fake approval call (pretend phone calls, a supervisor pretending to be "out") — customers have seen it a hundred times; one detected performance and every number you've quoted is worthless.
- ❌ Coming back from the approval and conceding everything (the customer learns the ceiling is higher)
- ❌ Over-running the exit time (silence lets the customer cool and reconsider; cooled customers rarely sign)

---

## Part 3 — Reading the buying signals

### 3.1 Eight buying signals (2–3 stacked = the closing window is open)

| # | Signal | What it means |
|---|--------|---------------|
| 1 | Asks how payment works / minimum down payment | Final confirmation of "can we afford it" |
| 2 | Asks whether the price can still move / the real bottom | Moved from "whether to buy" to "how to buy" |
| 3 | Asks how many units remain on this floor / orientation | Locking onto a specific unit |
| 4 | Calls family / asks what family would think | The decision has entered the household process (work *with* the family voice, not against it) |
| 5 | Recalculates repeatedly (payment / renovation / taxes) | Building a paper case *for* buying |
| 6 | Asks delivery date / property management / parking | Already assuming the move-in |
| 7 | Goes quiet, keeps returning to the same unit | Decided internally, resolving to commit |
| 8 | Asks for contact details / when to come back | Hesitant but unwilling to let go (a follow-up hook) |

### 3.2 Signal discipline

- **One signal alone is not a trigger** (a single question can be politeness); act at **2–3 stacked**.
- Confirm need-fit *before* pushing: "This layout works for your family of three, right?" — then close.
- If a cash discount has already gone to approval, **you opened the closing window yourself** — on return you must close it: "Approved. Today's signature, today's discount."

---

## Part 4 — Five levels of closing scripts

### 4.1 Level 1 — Soft close (the trial close)

> "You've seen the unit, you've seen the account — this floor is still available today. Lock {{floor}} now and you can discuss it at home with peace of mind: sign today, the discount lands today; come back tomorrow thinking it over, and this floor may not be here."

### 4.2 Level 2 — Direct close (the customer has already chosen)

> "Honestly, you've already picked — everything you've asked me today is about *how* to buy this unit, not *whether* to. Let's finish it today; I'll walk you through every step and you can stop carrying it around."

### 4.3 Level 3 — Alternative close (removes "whether", offers "A or B")

> "Of the two units, which do you lean toward? {{A}} is {{X}} cheaper; {{B}} has the better floor. Whichever you name, I put the full discount on *that* one."

### 4.4 Level 4 — Scarcity close (must be backed by real data)

> "This layout has {{X}} units left in the whole project — and that's not my claim, that's the sales-control board; you can look at it yourself. Whether today's available unit is here tomorrow, I genuinely can't promise."

### 4.5 Level 5 — Authority close (the manager's final push; pairs with Part 6.2)

> "Here's what I'll do — I'll bring my manager over and see whether he can give a special approval today. But let me be upfront: if it's approved, it's approved *for today's signature*. If it isn't, I've done what I can."

**Banned wording (all levels, all times):**

- ❌ "Buy now or prices go up" — threat pressure with no documented price-change decision behind it
- ❌ "After today this price is gone" — a false deadline
- ❌ "You decide — don't worry about what your family thinks" — driving a wedge inside the household; complaint-grade
- ❌ "I've decided for you — this unit" — deciding *for* the customer plants the buyback seed

---

## Part 5 — Deal completion and risk points

### 5.1 The completion chain

```
Confirm unit → re-read the pricing sheet aloud, line by line → fill the subscription form →
collect the deposit (POS / transfer, per procedure) → read the contract clauses aloud
(delivery date / area-difference handling / deposit-refund terms, exactly as written) →
agree the contract-signing date → manage the leave-taking mood
```

**Standard script (at signature):**

> "Let's go through the subscription form together: which unit, what price, how much discount, how much deposit — black on white, identical to the account we just ran. The delivery date and the deposit-refund terms I'll read out from the contract, nothing skipped. If you're good, sign here."

### 5.2 Leave-taking emotion management (preventing post-deposit regret)

- After signing, **restate their own buying reasons**: "The unit you chose today — good floor, total inside your budget, discount secured — every point your family cared about, {{point}}, is covered."
- Give a **concrete next step** ("Contract signing {{date}}, bring ID and the down payment") — a definite next appointment cuts regret sharply.
- **No follow-up nudge within 24 hours.** A customer who just signed and immediately gets chased starts re-litigating the decision.

### 5.3 Risk points

- Deposit / refund terms **disclosed exactly as written** — "it's refundable anyway" is how deposit disputes and complaints are born.
- Verbal discount promises must be **written into the subscription form** — an unwritten discount is a hand-over dispute waiting to detonate.
- When the customer hesitates, **do not decide for them**: "Take your time — I'll hold the unit until {{date}}." gives a graceful exit and keeps the honesty.

**Tool hook — when the customer asks "what happens if I walk away", quote the real rule, not a comfort line:**

```bash
# Deposit penalty, buyer breach, 50,000 deposit on a 1.5M contract (verified command):
python3 skills/calc-toolkit/deposit.py --mode penalty --price 1500000 --deposit 50000 --breach buyer
```

The tool applies the Civil Code deposit penalty articles (586/587/588) — in this exact case: a 50,000 deposit (3.3% of price) paid by a buyer who breaches is **forfeited: the loss is the full 50,000**. It also prints the disclosure that matters: only money actually delivered and *written as "deposit" (定金)* carries the penalty — booking fees (订金)， intent money (诚意金) and subscription-pool money (认筹金) do not. Use this to be precise at the table: the honest sentence is "if you sign the subscription and don't proceed, the deposit as written is at risk — that's exactly why we read every clause aloud before you sign." That sentence closes more deals than "don't worry, you can always get it back" — and unlike the latter, it survives contact with a lawyer.

---

## Part 6 — Team-assisted closing

> **Master discipline: one voice.** Two consultants, one price. Every concession a supervisor surfaces must be genuinely approvable. The choreography is *playmaking*, not deception — a customer who later learns the numbers never matched torches the office's whole trust base.

### 6.1 Consultant × consultant (the red face / white face pairing)

**Scenarios and division of labour:**

| Scenario | Lead consultant (A) | Support consultant (B) |
|----------|--------------------|------------------------|
| Customer pushes price | Holds the line: "That really is my best number" | Reinforces naturally: "I've sold {{X}} units in this project — what A quoted is the returning-client price" |
| Customer stuck on an objection | Continues building value | B unblocks it (per `sales-objection-handling`): "The {{Y}} issue you raised — the actual situation is {{the real wording}}" |
| Customer says "let me look around" | Doesn't block | B bridges naturally: "You should compare — though we walked their site recently, and {{the objective difference}}. Compare properly, then come talk to us" |
| A gets asked something he can't answer | Admits it, holds the room | B supplies the technical depth (pricing detail / construction detail) |
| The closing window opens | A runs the close | B stays quiet and lets the silence work (or tidies the subscription form — the visible *preparation to transact*) |

**Standard script (B re-engaging a drifting customer):**

> "(B joins naturally, with a reason — passing by, bringing documents, refilling water.) A, your customer has a good eye — this floor shows {{X}} units left on the board. (To the customer.) Compare as long as you like and come back to either of us — A's number *is* this project's number; whoever you talk to, it's the same figure. Compare with confidence."

**Pairing discipline:**

- Agree the signals in advance (a glance, a gesture, a set phrase as the opener); B always enters *with a reason* — documents, water, passing — never materialising from nowhere.
- **B never quotes or concedes a price** (the price has exactly one mouth: the lead consultant).
- Two consultants crowding one customer reads as pressure; B makes the point and withdraws, leaving A to close.

### 6.2 Consultant × supervisor / manager (the approval chain and the endgame)

**Levels and division of labour:**

| Level | Role | Does what | Enters when |
|-------|------|-----------|-------------|
| Consultant | Lead | Pricing / negotiation / pushing to the Tier-2 boundary | Throughout |
| Supervisor | Approval + second attacker | Approves Tier 2, runs the second close, re-tests the hesitation points | Customer asks beyond authority, or hesitation becomes visible |
| Manager | Endgame | Approves Tier 3 specials, the final push, sets the closing atmosphere | Large-amount ditherers / the last moment before signature |

**Standard supervisor flow (the consultant sets it up; the supervisor never drops in cold):**

1. Consultant sets the stage: "This situation deserves my supervisor — he can decide things I can't. Let me get him."
2. Supervisor arrives: confirms the customer's situation ("A has briefed me on your family's case") → credits the customer ("You read this floor exactly right — it *is* tight on the board") → **gives a genuinely approvable concession** → hangs the close on it ("Approved today means signed today").
3. Supervisor exits; the consultant re-takes the room and walks the completion chain (Part 5).

**Standard manager endgame script:**

> (Manager.) "I've heard the full picture. Sign today and I'll approve {{X}} — the most this office can put on the table today. But I owe you clarity: what I'm approving is *today's* sheet." (Nail "today" down explicitly.)

**Pairing discipline:**

- Approvals must be **real** — the supervisor is genuinely reviewing the sheet, genuinely holds that authority. The staged double-act approval is banned.
- Every condition a supervisor or manager states must be **deliverable** and must not contradict the consultant's numbers (same price, same discount).
- The approval exit stays within {{X}} minutes — silence bleeds emotion.
- The manager endgame is **rationed**: every appearance teaches the customer that the consultant's price is never the real price, and they start waiting for the manager every time.

---

## Appendix — One-page flow: pricing → negotiation → closing → completion

```
Customer sits down
  ↓
[Part 1] Five-element pricing sheet → lay it out (unit price → total → costs → payment → discount held back)
  ↓
[Part 2] Ladder: Tier 0 gifts → Tier 1 small cash → Tier 2 supervisor approval → Tier 3 manager special
  ↓  (every step exchanged for a commitment)
[Part 3] Signal read: 2–3 stacked = closing window open
  ↓
[Part 4] Five levels: soft → direct → alternative → scarcity → authority
  ↓  (triggered when the push stalls)
[Part 6] Team play: consultant × consultant (red face/white face, re-engagement)
         → consultant × supervisor (approval, second attack) → manager endgame
  ↓
[Part 5] Completion chain: subscription form → deposit → clauses read aloud → leave-taking mood managed
  ↓
No signature today → `sales-lead-grading`: register, grade, follow up (the sheet is the follow-up asset)
```
