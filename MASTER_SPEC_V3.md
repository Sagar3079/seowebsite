# MASTER SPEC V3 — "Forma" Collection II: +12 business sites (Food, Travel, Retail, Services)

## Mission

Expand the Forma Premium Collection from 12 to **24 templates** by adding 12 brand-new demo
websites for everyday businesses — restaurants, food, travel, retail, services — at the exact
same bar as V2: **$10,000 custom-agency quality with the 3D mandate**.

**ALL hard technical constraints, the 3D MANDATE, and the $10k design bar from
MASTER_SPEC_V2.md apply unchanged to every new site.** Read that file first. Summary of
non-negotiables: fully self-contained (no external anything), system font stacks only
(deliberately paired, different per site), complete standalone HTML docs that also work in
iframe srcdoc, flawless at 390/768/1280px with zero horizontal scroll, 30–75 KB per file,
real specific copy (no lorem ipsum), valid HTML + error-free JS, ≥2 executed 3D techniques
per site at 60fps (transform/opacity only, rAF-throttled), prefers-reduced-motion honored,
graceful no-JS/touch degradation.

Each of the 12 must ALSO look different from the 12 existing V2 sites (deep-ink law firm,
blueprint architecture, seafoam dental, obsidian/gold EV, green-phosphor AI, stratosphere
drone, noir barbershop, travertine spa, velvet-gold jewelry, amber recording studio,
cyan/magenta esports, alpine outfitter). No repeated palettes or hero concepts.

## The 12 NEW businesses

New category strings (exact): `Food`, `Travel`, `Retail`, `Services`.

**Agent A — Food** (category `Food`)
1. `saffron-vine` — "Saffron & Vine", contemporary fine-dining restaurant (Mediterranean).
   Dusk terrace mood: aubergine/olive/saffron on warm stone — NOT the charcoal/ember noir of
   past restaurant looks. 3D: candlelit table composition with mouse-tilt depth; parallax
   course-by-course tasting menu that plates as you scroll. Sections: tasting + à la carte
   menus with prices, chef & sourcing, private dining, reservations.
2. `flour-fold` — "Flour & Fold", French pâtisserie & bakery. Morning light: butter cream,
   flour white, copper, espresso. 3D: layered cake/viennoiserie built from CSS planes or
   stacked SVG layers rotating gently; counter cards tilt. Sections: patisserie case with
   prices, daily bake schedule, wholesale, classes with dates/prices, visit.
3. `koya-ramen` — "Koya Ramen Bar", late-night ramen kitchen. Tokyo alley: lacquer black,
   neon red/persimmon, steam white, paper-lantern warm. 3D: canvas rising-steam scene over a
   3D bowl composition; menu tiles with chopstick-flick hover. Sections: bowls with prices +
   heat levels, broth story (48-hour timeline), sides & drinks, hours/queue policy.

**Agent B — Travel** (category `Travel`)
4. `azure-cove` — "Azure Cove", barefoot-luxury island resort. Lagoon: sea glass, sand,
   coral sunset. 3D: layered ocean parallax (horizon/waves/shore at depths) with slow drift;
   villa cards tilt with light sheen. Sections: villas with nightly rates, island experiences,
   dining, spa, getting there, booking.
5. `terra-fauna` — "Terra & Fauna", safari & wildlife tour operator. Golden hour savanna:
   ochre, acacia green, dusk violet, bone. 3D: multi-layer savanna silhouette parallax with
   drifting sun + wildlife silhouettes; itinerary cards lift/tilt. Sections: signature safaris
   with dates/prices/group sizes, conservation pledge, guides, traveler stories, enquire.
6. `aurora-air` — "Aurora Air", boutique regional airline (fjords & northern routes). Crisp
   arctic: glacier white, deep navy, aurora teal/green ribbon accent. 3D: CSS 3D aircraft
   above parallax cloud deck that banks with cursor; SVG route map with animated arcs.
   Sections: destinations & fares, cabin experience, fleet, schedule, book a seat.

**Agent C — Retail** (category `Retail`)
7. `paper-bloom` — "Paper & Bloom", florist studio. Fresh-cut editorial: leaf greens, petal
   pinks handled maturely, kraft paper, ink. 3D: layered SVG blooms assembling into a bouquet
   with depth parallax; arrangement cards tilt. Sections: signature arrangements with prices,
   weekly subscription tiers, weddings & events, care guide, shop hours.
8. `oakline-studio` — "Oakline", handcrafted furniture studio. Workshop warmth: oak, walnut,
   wool grey, forged black. 3D: CSS-plane 3D lounge chair or credenza rotating on a plinth
   with believable face lighting; material swatches flip in 3D. Sections: collection with
   prices & dimensions, materials & joinery, custom commissions process, showroom.
9. `novel-house` — "The Novel House", independent bookshop & café corner. Library dusk:
   oxblood, forest, brass lamp glow, cream paper. 3D: 3D book stack/opening-cover hero from
   CSS planes; staff-pick shelf cards tilt with page-edge detail. Sections: staff picks with
   prices, events calendar (author nights with dates), book club, café menu, find us.

**Agent D — Services** (category `Services`)
10. `crestview-realty` — "Crestview", modern boutique real-estate agency. Confident daylight:
    slate blue, limestone, brass key accent. 3D: isometric CSS-built house/streetscape that
    tilts with cursor; listing cards with 3D lift + price/beds/baths chips. Sections: featured
    listings with real prices/specs, sold record, agents, sell-with-us pitch, valuation CTA.
11. `hive-workspace` — "Hive", design-led coworking campus. Optimistic utility: honey amber,
    graphite, off-white, signal coral. 3D: exploded isometric floor-plan (layered plans
    separating on scroll/hover); membership cards tilt. Sections: memberships with monthly
    prices, spaces (desks/studios/labs), amenities, community events, tour booking.
12. `velvet-pine` — "Velvet & Pine", wedding & event planning studio. Modern romance without
    cliché: deep pine, champagne, porcelain, a single ribbon red. 3D: parallax layers of
    drifting florals/ribbon light; portfolio cards tilt with soft sheen. Sections: services &
    packages with prices, real weddings portfolio, planning process (a true sequence),
    testimonials, enquiry form (inline validation, non-submitting).

## Metadata (same shape)

Per template: `id`, `name`, `category` (exact string above), `tagline` (≤60 chars),
`description` (one Forma-marketing sentence), `accent` (hex), `file` (absolute path).

## Agent E — Shell v3 (upgrade shell-v2 for 24 templates)

Start from /tmp/claude-0/-home-user-seowebsite/d4ede775-72c4-54d1-9f3e-29d50fbc772a/scratchpad/showcase/shell-v2.html
(read it fully; keep its design language, tokens, 3D card tilt, hero, modal — this is an
upgrade, not a redesign). Write the result to shell-v3.html.

Required changes:
1. **Scale to 24 templates / 8 categories.** Filter bar: All / Professional / Tech /
   Lifestyle / Entertainment / Food / Travel / Retail / Services, with live counts, wrapping
   gracefully on mobile (horizontal scroll-snap chip row is acceptable on small screens —
   inside its own container, never the page).
2. **Search.** A search input in the gallery header filtering live (case-insensitive) against
   name + tagline + category; combines with the active category filter; shows "No matches"
   empty state with a clear-search action; Esc clears when focused. Keyboard accessible.
3. **Performance at 24 live iframes:** keep loading="lazy"; ALSO only set thumbnail srcdoc
   when a card first becomes visible (IntersectionObserver) so initial load stays fast; keep
   scroll/tilt handlers rAF-throttled.
4. Update hero copy/stats for the bigger collection (24 templates · 8 categories); phrase it
   as "Collection II" energy without breaking the existing design voice.
5. Everything else preserved: exact data contract (placeholder string, runtime JSON.parse,
   card order = array order), thumbnail scaling mechanics, preview modal with device toggles,
   focus trap, theme token pattern with data-theme overrides, reduced-motion, ≤90 KB before
   injection, same <title>.
