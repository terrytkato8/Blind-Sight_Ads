title: Executive Readiness Plan
section: Program
order: 2
---
# Executive Readiness Plan

What each executive role has to take care of for the sponsorship program to work.

## Bottom line

Steam allows product placement only if it is "not disruptive and appropriate within the context of the game." It does not support advertising as a business model, or rewarding players for engaging with ads ([Steamworks](https://partner.steamgames.com/doc/marketing/advertising)). Our placements fit that rule. Programmatic ad-network slots should be dropped for the Steam build, and the loading-screen title sponsor needs a policy check.

**Must-dos before the first signature**

1. Every rev-share contributor signs an IP assignment. **Drafted:** [Contributor IP Term Sheet](contributor-ip-term-sheet.html). Next: counsel review, then signatures.
2. ~~Publisher and investor carve-outs.~~ **Not applicable:** no publisher or investor is involved in Blind Sight.
3. A sponsorship agreement template reviewed by counsel. **Drafted:** [MSA](master-sponsorship-agreement.html), [Order Form & SOW](order-form-sow.html), [SLA](sla.html), [Sponsor Term Sheet](sponsor-term-sheet.html), [RFP](rfp-brand-brief.html).
4. The sponsor-slot system in Unreal. **Drafted:** [Tech Spec](sponsor-slot-tech-spec.html). Next: engineering build.
5. Branded items have exactly the same stats as unbranded ones. **Covered** in MSA 5.2, Creative Guidelines rule 2 and the CI parity test.
6. A gameplay clip of a branded can being thrown in the vertical slice. **Pending:** waiting on the build.
7. Streamer commitments in writing. **Drafted:** [Creator LOI](creator-loi.html).
8. Invoicing, deferred revenue and a contract tracker. **Drafted:** [Finance Operations](finance-operations.html) + [contract tracker](downloads.html).

## CEO — strategy and guardrails

| Item | Why it matters | When |
| --- | --- | --- |
| Set the purpose and a revenue target | Bridge funding or long-term revenue? It sets how hard we push, how much art time it gets and which discounts are acceptable. Target: [$__] signed before launch | Now |
| Give the creative director a veto | A sponsor can never change gameplay, balance or tone | Now |
| Decide how the rev-share team shares in it | Rev-share pool, bonus provision, or both, in writing | Before first payment |
| Set pricing authority | Who approves discounts below rate card; the floor is 2.5× production cost | Now |
| Map the categories | Which categories we sell and which we refuse (alcohol, gambling, vaping, political); track exclusivity | Before outreach |
| Set go / no-go criteria | E.g. if [__] founding partners aren't signed by [date], pause outreach | Now |
| Own the top relationships | The CEO runs the first 3–5 founding-partner deals | Ongoing |

## CTO — build it so brands can come and go

| Item | Why it matters | When |
| --- | --- | --- |
| Sponsor-slot system | `SponsorSlot` actor and Data Assets per placement; level designers place slots, deals fill them | Before first signature |
| Branded items are skins only | One base throwable class; an automated test fails the build if a branded item's physics, noise radius or GAS values differ | Before first branded build |
| Removable content packaging | Sponsor assets in their own pak chunks; permanent placements in the main chunk | Before launch |
| Remote kill switch | A flag fetched at startup (EOS Title Storage) hides a placement immediately | Before launch |
| Audio rules for brand stings | MetaSound presets within the GDD loudness range, distinct from footsteps and gunshots | Before first hero-prop deal |
| Asset intake spec | One page of formats and budgets for brands | Before outreach |
| Performance budget | Per-map cap on sponsor draw calls and texture memory | Before first branded build |
| Measuring impressions | Privacy-safe telemetry following IAB/MRC intrinsic in-game guidelines | Before launch |
| No ad-network SDKs on Steam | Steam doesn't support ad-based business models | Decision now |
| Mods and UGC policy | Block sponsor assets from texture replacement before any Workshop support | Before any UGC |
| Capture tools | In-engine screenshot and replay camera for approvals and reports | Before first approval |
| Protect the core roadmap | Cap sponsor work at ~40 hrs/week, tracked as its own epic | Ongoing |

## CMO — sell it, prove it, keep players happy

| Item | Why it matters | When |
| --- | --- | --- |
| Proof asset: a branded gameplay clip | 20–30 seconds of a branded can thrown as a decoy | Before outreach |
| Audience proof points | Steam wishlists, playtest sign-ups, Discord members | Before outreach |
| Creator commitments in writing | A letter of intent from each streamer the deck cites | Before outreach |
| Target list and pipeline | 15–20 brands in priority order with a CRM stage per deal | Before outreach |
| Channels | Brand gaming teams, gaming agencies (~15%), brand creator programs | Ongoing |
| Player sentiment | Sponsors keep the price low, never affect gameplay, and are credited openly | Before announcement |
| Creator + sponsor disclosure | #ad and platform paid-promotion tags; check creator sponsor conflicts | Before launch streams |
| Sponsor reporting | Launch and quarterly reports: impressions, interactions, stream hours, clips | Before launch |
| Co-marketing terms | Ask brands to promote too | Each deal |
| Brand-safety briefing | One page on the stylized gun, tone, rating and no gore | Before outreach |

## COO — make it a repeatable operation

Every deal follows one path: **lead → proposal → contract → invoice → asset intake → build → brand approval → live in build → report → renewal or removal.**

| Item | Why it matters | When |
| --- | --- | --- |
| Deal workflow and owners | An owner and turnaround for each step | Before first signature |
| Tools | CRM, contract folder, ClickUp list per deal | Before outreach |
| Invoicing and collections | Implementation fee + 50% at signing, 50% at go-live, Net 30 | Before first signature |
| Revenue recognition | Deferred revenue spread over the term; CPA guidance | Before first payment |
| Tax | CPA on California sales tax for advertising services; W-9s; 1099s | Before first payment |
| Rev-share accounting | Sponsorship revenue in its own account | Before first payment |
| Capacity planning | Art-hour forecast under the 40 hrs/week cap; backup artists | Before third deal |
| Term and renewal calendar | End dates, renewal outreach 60 days before, removal patch dates | Before first go-live |
| Insurance | Media liability (E&O), general liability, cyber | Before first enterprise brand |
| KPIs | Pipeline value, close rate, deal size, on-time delivery, margin, renewals | Ongoing |

## Head Legal Counsel — contracts, rights and rules

*A checklist to work through with a licensed attorney, not legal advice.*

| Item | Why it matters | When |
| --- | --- | --- |
| Team IP assignment | Without it we may not own the branded assets we license | Before first signature |
| Master sponsorship agreement + order forms | Fees, term, limited approvals, deemed approval, make-goods, termination, liability, indemnities | Before first signature |
| Trademark license from the brand | Limited and non-exclusive; perpetual for permanent placements | Before first signature |
| Footage that lives forever | No obligation to take down streams, clips or archives after the term | Before first signature |
| Our license to the brand | Brand may use Blind Sight's name and footage, with approval | Before first signature |
| Morals clause, both ways | Removal via kill switch plus a refund rule | Before first signature |
| Exclusivity definitions | Precise categories | Before first exclusive deal |
| Steam policy check | Confirm the title sponsor and video screens fit; never reward players for branded interactions | Before first signature |
| Advertising law | FTC disclosure, children's advertising rules, UK/EU recognizability | Before outreach |
| Rating impact | ESRB/PEGI/IARC effects of brands and the stylized gun | Before rating submission |
| Privacy | Anonymous, aggregated telemetry; CCPA/GDPR | Before launch |
| Our own trademarks | Clearance and USPTO filing for "Blind Sight" and Kato.8 marks | Now |
| Comparisons in sales materials | Name Meccha Chameleon factually; never imply affiliation | Ongoing |

## Decisions needed this month

- [ ] Pre-launch sponsorship revenue target and go / no-go date
- [ ] Sponsor revenue split between the rev-share pool and the bonus provision
- [ ] Categories we sell and categories we refuse
- [ ] Drop programmatic ad-network slots from the Steam plan (recommended)
- [ ] Keep or rework the loading-screen title sponsor after the Steam check
- [ ] Target Steam launch window

## Sequence

1. **Foundation (weeks 1–4):** IP assignments, contract template, trademark filing, Steam check, invoicing setup, sponsor-slot spec.
2. **Proof (weeks 3–8):** branded-can gameplay clip, Steam page and wishlists, creator LOIs, asset intake spec, brand-safety one-pager.
3. **Outreach (weeks 6–12):** 15–20 target brands, CEO-led founding-partner pitches, first signed deal.
4. **Delivery (from first signature):** build, approvals, sponsor-slot QA, telemetry live before launch.
5. **Launch and after:** sponsor reports, renewals and removals on the term calendar.
