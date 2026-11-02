title: Sponsor-Slot Tech Spec
section: Build & Operations
order: 1
---
# Sponsor-Slot System — Technical Spec & Build Instructions

**Goal:** brand content lives in data, never in gameplay code. A deal is filled, swapped, region-gated or removed by changing data, and the no-advantage rule is enforced by tests, not by trust.

## 1. Architecture

| Piece | Type | Responsibility |
| --- | --- | --- |
| `USponsorPlacementData` | Primary Data Asset | One per deal Placement: deal ID, brand ID, category, mesh/material overrides, decal or media texture, audio sting (MetaSound preset), allowed regions, start/end dates, Permanent flag |
| `ASponsorSlot` | Actor placed in levels | A typed slot (Poster, VideoScreen, SetDressing, InteractiveProp, TitleScreen) that resolves which data fills it, or falls back to an unbranded look |
| `USponsorSkinComponent` | Actor component | On the base throwable and interactive-prop classes. Applies cosmetic overrides only and never touches gameplay properties |
| `USponsorSubsystem` | Game instance subsystem | Loads the placement manifest, applies remote flags (kill switch, regions, dates), answers "what fills this slot?" |
| Placement manifest | Data table / JSON | Active placements per build, generated from the contract tracker's deal IDs |
| Remote flags | EOS Title Storage file (`sponsor_flags.json`) | Fetched at startup and on return to lobby; disables any deal ID with no patch |

## 2. Build steps

1. Create a `Sponsor` plugin module and keep all sponsor code and assets in it. Core gameplay modules never depend on it.
2. Add `ASponsorSlot` types and place default (unbranded) slots in each map. Level design owns slot placement.
3. Add `USponsorSkinComponent` to `BP_ThrowableBase` and the interactive-prop base, exposing only cosmetic fields.
4. Implement `USponsorSubsystem`: manifest loading, date and region checks, remote-flag override, and an unbranded fallback on any error.
5. Put sponsor assets in their own pak chunks (Asset Manager + Primary Asset Labels, one chunk per deal). Permanent placements go in the main chunk.
6. Wire the title-sponsor slot into the opening loading screen (UMG), hidden until the Steam policy check is cleared.
7. Add the telemetry events (section 4) and the parity test (section 3) to the automation suite and CI.
8. Add console commands `sponsor.list` and `sponsor.disable <dealId>` for QA.

## 3. Gameplay parity test (required in CI)

An automation test spawns every branded variant next to its base class and asserts these are equal. A failure blocks the build.

- mass, collision profile and physics material
- throw impulse, arc and bounce
- noise-event radius and intensity on throw and impact
- GAS attributes, tags and cooldowns
- spawn weight and inventory stack size

```cpp
// Pseudocode
for (auto* Variant : SponsorSubsystem->GetAllThrowableVariants()) {
  TestEqual("Mass", Variant->GetMass(), Base->GetMass());
  TestEqual("NoiseRadius", Variant->ImpactNoise.Radius, Base->ImpactNoise.Radius);
  TestEqual("GameplayTags", Variant->Tags, Base->Tags);
  // ...every gameplay-relevant property
}
```

## 4. Telemetry (for SLA reports)

| Event | Fired when | Fields |
| --- | --- | --- |
| `sponsor_impression` | The Placement covers ≥10% of the screen, unobstructed, for ≥1 continuous second | dealId, mapId, duration, screenShare |
| `sponsor_interaction` | Pickup, throw or activation | dealId, mapId, type |
| `sponsor_render_ok` | Slot resolved and rendered at match start | dealId, mapId |
| `sponsor_render_fail` | Slot fell back or the asset failed to load | dealId, mapId, reason |

All events are anonymous: session IDs are hashed, no player IDs leave the client, and data is aggregated server-side before reporting. Availability = `render_ok` / (`render_ok` + `render_fail`) for eligible matches.

## 5. Kill switch and removal

- **Emergency:** add the deal to `disabled` in `sponsor_flags.json`. Clients fall back to unbranded within one match. Target: 24 hours from request.
- **Term end:** remove the deal from the manifest and its chunk from the next patch, within 30 days.
- **Permanent:** flagged in data; never removed by automation. Removal needs a manual override and sign-off.

## 6. Mods and capture

- Sponsor assets ship in signed, encrypted pak chunks. If UGC or Workshop is ever added, sponsor materials and textures are excluded from overrides.
- A photo-mode camera and an approval capture preset (fixed angles and lighting) produce consistent approval stills.

## 7. QA checklist for each Placement

- [ ] Parity test passes
- [ ] Renders on all listed maps, at all quality settings, with LODs checked
- [ ] Within the per-map sponsor performance budget
- [ ] Audio sting within loudness limits and distinct from gameplay cues
- [ ] Kill switch tested: disable, then confirm the fallback
- [ ] Telemetry events fire and appear in the dashboard
- [ ] Region and date gating works
- [ ] Approval stills and capture exported
