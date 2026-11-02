title: Creative & Asset Guidelines
section: Sales
order: 2
---
# Brand Asset & Creative Guidelines (Schedule C)

Schedule C to the [Master Sponsorship Agreement](master-sponsorship-agreement.html). The rules every Placement follows and the files we need from the brand.

## Creative rules

1. **The game's style comes first.** Brand assets are restyled into Blind Sight's stylized horror-comedy look. Brands approve the result but can't require photoreal art.
2. **No gameplay advantage, ever.** A branded item behaves exactly like its unbranded version: same physics, weight, throw arc, noise radius, impact loudness, spawn rate and availability. An automated test enforces this in every build.
3. **No forced engagement.** Players never have to watch, use or interact with a Placement, and are never rewarded for doing so (Steam advertising policy).
4. **Comedic treatment.** Products can be thrown, dropped, dented, knocked over, hidden behind and used as decoys.
5. **Off-limits:** the Hunter's weapon, elimination effects, gore, disparaging contexts, and any combination with alcohol, gambling, tobacco, vaping or political messaging.
6. **One brand per category per map**, unless exclusivity across all maps is purchased.
7. **Audio stings** fit inside the GDD's loudness range, are distinct from footsteps, doors and the Hunter's gunshot, and never mask gameplay-critical sounds.
8. **No product claims in game** ("#1", "healthiest", prices, promotions). Logos, product shapes and brand colors only.

## Asset intake spec (from the brand)

| Asset | Format | Notes |
| --- | --- | --- |
| Primary logo | SVG or AI (vector), plus PNG at 4096 px with transparency | Full-color, single-color and reversed |
| Brand colors | HEX/RGB values | Primary and secondary |
| Product photos | JPG/PNG, 2048 px or larger, front, side, back and top | For 3D modeling |
| Product dimensions | mm or inches | Real-world scale |
| Packaging dielines | PDF/AI | Optional; speeds up texturing |
| Video (video screens only) | MP4 H.264, 1920×1080, 15–30 seconds | Looping, no on-screen URLs or prices |
| Audio sting (interactive props only) | WAV, 48 kHz, 24-bit, 1–3 seconds | May be re-pitched or mixed to fit |
| Brand guidelines | PDF | Including clear space and misuse rules |
| Mandatory legal lines | Text | E.g. trademark notices for the credits |

## Studio technical budgets

| Placement | Triangle budget | Textures | Audio |
| --- | --- | --- | --- |
| Throwable | 1.5k–3k tris, 3 LODs | 1× 1024 set | Impact set inherited from the base class |
| Set-dressing prop | 2k–8k tris, 3 LODs | 1× 1024–2048 set | None |
| Interactive prop | 8k–20k tris, 3 LODs | Up to 2× 2048 sets | Brand sting + interaction sounds |
| Poster / decal | Decal or plane | 1× 2048 | None |
| Video screen | Existing screen mesh | Media texture, 1080p | Optional, attenuated |
| Title sponsor | UI (UMG) | Logo at 1024 px | None |

## Approval submissions (from the studio)

Each round: three rendered stills (hero, in-context, gameplay angle) and a 10–20 second in-engine capture. Feedback is consolidated by the named approver, one list per round.
