title: Rate Card
section: Program
order: 1
---
# In-Game Advertising & Product Placement Rate Card

## Overview

Blind Sight sells placements as **flat-fee, fixed-term sponsorships** priced by tier, from $1,500 for a poster to $40,000 for an interactive hero prop, plus a small one-time implementation fee per placement. Flat fee is the standard model for static in-game placements, and the price follows how prominent the placement is and how big the game's audience is expected to be ([RapidFire](https://rapidfire.com/blog/in-game-advertising-pricing-and-costs)).

What Blind Sight can sell that other games can't: **sound is a placement surface.** Hiders throw branded cans, branded jukeboxes act as noise lures, and the Hunter learns to recognize a brand's audio sting by ear. In most games a logo is set dressing. Here it can be part of the gameplay.

Price = **base tier rate × term × reach (maps) × exclusivity × audience index**, minus a founding-partner discount before launch, plus the flat implementation fee.

## Placement inventory & tiers

| Tier | Placement | What the player experiences | Gameplay link |
| --- | --- | --- | --- |
| 1 | Poster / decal | Brand art on walls, signs and billboards, restyled to the game's horror-comedy look | Visual only. The Hunter's impaired vision barely sees it, so value comes from Hiders and spectators |
| 2 | Video screen | A looping 15–30s brand video on an in-world TV, arcade cabinet or billboard screen | Optional audio. If it plays sound, it emits a quiet sound event the Hunter can hear |
| 3 | Branded set-dressing prop | Branded products scattered around the map: soda cans, snack boxes, a delivery van | Static. It can occlude sound (e.g. hiding behind the branded van) |
| 4 | Branded throwable | One of the throwables Hiders pick up, carry and throw (GDD §6.3), with its own impact sound | Core loop. Handled every round. Highest-value placement for its cost |
| 5 | Interactive hero prop | A branded vending machine that gives out throwables, or a jukebox or radio Hiders can switch on as a noise lure | Core loop. Plays the brand's audio sting, which the Hunter learns to read |
| 6 | Title sponsor | The brand's logo on the opening loading screen ("Presented by Brand"), seen by every player each time the game starts | None. One sponsor per term |

We don't sell placements on the Hunter's weapon or on the elimination effect.

**Prop ideas:** soda can and energy drink (throwables, from $12K); foam dart blaster, Bluetooth speaker and ringing phone (noise-makers, from $20K; the blaster is a Hider toy, never the Hunter's weapon); snack bag, gaming headset and pizza box (set dressing, from $5K).

## Base rates

Base rates are for **one map, a 12-month term and non-exclusive placement**, assuming an audience of 25,000–100,000 players in year one. The low end of each range is a back room; the high end is the spawn area or main sightline.

| Tier | Placement | Base rate (USD, 12 mo, 1 map) | Implementation fee (one-time) | Included |
| --- | --- | --- | --- | --- |
| 1 | Poster / decal | $1,500 – $3,000 | $350 | Up to 3 instances, 1 art adaptation, 2 approval rounds |
| 2 | Video screen | $3,000 – $6,000 | $500 | 1 screen location, 1 video loop, 1 creative swap per term |
| 3 | Branded set-dressing prop | $5,000 – $10,000 | $750 | 1 product modeled, up to 10 instances |
| 4 | Branded throwable | $12,000 – $25,000 | $1,500 | Model, physics, custom impact sound, spawns on every map |
| 5 | Interactive hero prop | $20,000 – $40,000 | $2,500 | 1 interactive object, 3–5 placements, brand audio sting |
| 6 | Title sponsor (opening loading screen) | $5,000 – $12,000 (whole game) | $250 | Logo + "Presented by" line, 1 logo swap per term, only sponsor in the slot |

**Implementation fee.** Billed in full at signing. Never multiplied or discounted. Covers 50–80% of our build cost, so the sponsorship fee itself is almost all margin.

## Multipliers

| Lever | Option | Multiplier |
| --- | --- | --- |
| Term | 6 months | 0.6× |
| Term | 12 months (base) | 1.0× |
| Term | 24 months | 1.7× |
| Term | Permanent: stays in the game for good. Available before launch, tiers 1–5 | 2.5× |
| Reach | Each additional map (tiers 1–3, 5) | +0.6× per map |
| Exclusivity | Category exclusive, e.g. the only soda brand (tiers 1–5) | 1.35× |
| Placement | Premium spot: spawn, main sightline, results screen (tiers 1–5) | 1.25× |
| Audience index | Under 25k players | 0.7× |
| Audience index | 25k – 100k players (base) | 1.0× |
| Audience index | 100k – 500k players | 2.0× |
| Audience index | 500k+ players | Custom pricing |
| Pre-launch | Founding partner (signed before Steam launch) | 0.7× |

**Permanent placements before launch** stack the 2.5× term with the 0.7× founding discount, for **1.75× the base rate**. Each category gets at most one permanent slot.

**Worked examples**

- Soda brand, branded throwable, all maps, 24 months, category exclusive, signed before launch: $18,000 × 1.7 × 1.35 × 0.7 = $28,900, plus $1,500 implementation = **$30,400**.
- Same throwable as a permanent placement, signed before launch, non-exclusive: $18,000 × 2.5 × 0.7 = $31,500, plus $1,500 = **$33,000**.

**Performance kicker (pre-launch deals).** The brand pays an extra 25% of the fee if peak concurrent players or units sold pass an agreed number within 90 days of launch.

## Packages

| Package | Contents | Price + implementation fee |
| --- | --- | --- |
| Starter | 3 posters + 1 video screen, 1 map, 12 months | $6,000 + $850 |
| Snack Pack | Set-dressing prop + branded throwable, all maps, 12 months | $25,000 + $2,250 |
| Sound Sponsor | Hero jukebox/radio + brand audio sting + throwable, all maps, 12 months | $45,000 + $4,000 |
| Founding Partner | Title sponsor (12 months) + permanent, category-exclusive throwable, signed before launch | From $48,000 + $1,750 |

> **Under review: ad-network (CPM) slots.** An earlier version proposed switching posters and screens to programmatic ad-network slots after launch. Steam does not support advertising as a business model ([Steamworks](https://partner.steamgames.com/doc/marketing/advertising)), so this is recommended to be dropped for the Steam build. See the [Readiness Plan](readiness-plan.html).

## 3D / art production time

Estimates assume the brand supplies logos, vector art, product photos and video, and that we restyle everything. Dollar figures use a **notional $50/hr blended rate**; the team is on revenue share, so this is a planning figure.

| Tier | Work breakdown (hours) | Total hours | Calendar time | Cost @ $50/hr |
| --- | --- | --- | --- | --- |
| 1 Poster / decal | Art adaptation 4–6 · material + placement 1–2 · approvals + QA 2–3 · account mgmt 2 | 9 – 13 | 1–2 weeks | $450 – $650 |
| 2 Video screen | Reformat + compress video 4–8 · media material + screen setup 4–6 · audio event 0–2 · approvals + QA 3 · account mgmt 2 | 13 – 21 | 2–3 weeks | $650 – $1,050 |
| 3 Set-dressing prop | Model + UV + texture 12–20 · LODs 2–4 · placement 2 · approvals 4 · account mgmt 3 | 23 – 33 | 3–4 weeks | $1,150 – $1,650 |
| 4 Branded throwable | Model + texture 14–22 · Chaos physics 4–6 · impact sound + tuning 6–10 · Blueprint/GAS hooks 4–6 · playtest + QA 6–8 · approvals 4 · account mgmt 4 | 42 – 60 | 4–6 weeks | $2,100 – $3,000 |
| 5 Interactive hero prop | Model + texture 30–45 · rig + animation 10–20 · interaction Blueprint 12–20 · audio sting + MetaSound 8–12 · playtest + QA 10–14 · approvals 6 · account mgmt 6 | 82 – 123 | 6–8 weeks | $4,100 – $6,150 |
| 6 Title sponsor | Logo adaptation 2–3 · loading-screen UI (UMG) 1–2 · approvals 2 · account mgmt 2 | 7 – 9 | 1–2 weeks | $350 – $450 |

## Margin check

| Tier | Midpoint price | Implementation fee | Midpoint production cost | Margin (price only) | Margin (with fee) |
| --- | --- | --- | --- | --- | --- |
| 1 Poster / decal | $2,250 | $350 | $550 | 76% | 79% |
| 2 Video screen | $4,500 | $500 | $850 | 81% | 83% |
| 3 Set-dressing prop | $7,500 | $750 | $1,400 | 81% | 83% |
| 4 Branded throwable | $18,500 | $1,500 | $2,550 | 86% | 87% |
| 5 Interactive hero prop | $30,000 | $2,500 | $5,125 | 83% | 84% |
| 6 Title sponsor | $8,500 | $250 | $400 | 95% | 95% |

**Quoting guardrails**

- **Price floor:** never quote a sponsorship fee below 2.5× production cost after every discount. The implementation fee doesn't count toward the floor.
- **Agency commission:** expect about 15% if a media agency brings the deal. Quote gross.
- **Team bonus:** artists are paid for sponsor work through the bonus provision in the revenue-share agreement.

## Pipeline capacity and signing deadlines

Cap sponsor work at **about 40 art hours a week** (two artists at 20 hrs/week).

| Tier | Sign at least this far before build lock |
| --- | --- |
| 6 Title sponsor | 3 weeks |
| 1–2 Poster, video screen | 4 weeks |
| 3–4 Set-dressing prop, throwable | 8 weeks |
| 5 Interactive hero prop | 10 weeks |

Later deals go into the first post-launch content update, and their term starts on that date.

## Sources

- [In-game advertising pricing and costs — RapidFire](https://rapidfire.com/blog/in-game-advertising-pricing-and-costs)
- [Intrinsic In-Game Advertising Key Trends Report — Anzu](https://www.anzu.io/news/trends-report)
- [Steamworks — Advertising on Steam](https://partner.steamgames.com/doc/marketing/advertising)
