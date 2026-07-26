# MASTER SPEC V2 — "Forma" Premium Collection (12 new $10k-grade 3D websites)

## Mission

Replace the previous template set with **12 brand-new demo websites for different businesses**,
each built to the standard of a **$10,000 custom agency site**: distinctive art direction,
layered 3D depth, orchestrated motion, and obsessive detail. A visitor should open any one and
think "a real studio charged real money for this."

The shell (gallery site) is also rebuilt to the same bar. The data contract with the build step
is UNCHANGED from v1.

## Hard technical constraints (unchanged, non-negotiable)

1. Fully self-contained per file — a strict CSP blocks ALL external requests. No CDNs, no
   Google Fonts, no remote images, no three.js — every byte inline.
2. System font stacks only, deliberately paired, different per site:
   - Humanist: `Seravek, 'Gill Sans Nova', Ubuntu, Calibri, 'DejaVu Sans', source-sans-pro, sans-serif`
   - Neo-grotesque: `Inter, Roboto, 'Helvetica Neue', 'Arial Nova', 'Nimbus Sans', Arial, sans-serif`
   - Transitional serif: `Charter, 'Bitstream Charter', 'Sitka Text', Cambria, serif`
   - Didone: `Didot, 'Bodoni MT', 'Noto Serif Display', 'URW Palladio L', P052, serif`
   - Old-style serif: `'Iowan Old Style', 'Palatino Linotype', 'URW Palladio L', P052, serif`
   - Slab: `Rockwell, 'Rockwell Nova', 'Roboto Slab', 'DejaVu Serif', 'Sitka Small', serif`
   - Mono: `ui-monospace, 'Cascadia Code', 'Source Code Pro', Menlo, Consolas, 'DejaVu Sans Mono', monospace`
   - Geometric: `Avenir, Montserrat, Corbel, 'URW Gothic', source-sans-pro, sans-serif`
   - Rounded: `ui-rounded, 'Hiragino Maru Gothic ProN', Quicksand, Comfortaa, Manjari, 'Arial Rounded MT', 'Arial Rounded MT Bold', Calibri, source-sans-pro, sans-serif`
3. Visuals from CSS gradients/patterns, inline SVG, and `<canvas>` (2D or hand-written WebGL).
   No external images.
4. Each demo: complete standalone HTML document (doctype, head with charset/viewport/title,
   inline style, inline script). Must work standalone AND inside iframe `srcdoc`.
5. Responsive and flawless at 390 / 768 / 1280 px. No horizontal page scroll anywhere.
6. Size budget per demo: 30–75 KB. Shell ≤ 80 KB before JSON injection.
7. Real, specific copy everywhere — names, prices, addresses, dates. Zero lorem ipsum.
8. Valid HTML, error-free JS, visible focus states, legible contrast, graceful no-JS fallback
   (content must be readable with JS off even if effects are gone).

## THE 3D MANDATE (what makes this set different)

Every site must feel dimensional, not flat. Each demo must include **at least TWO** of these,
executed smoothly:

- **Mouse-tilt hero scene**: a composition in a `perspective` container that tilts with cursor
  position (rotateX/rotateY, throttled via requestAnimationFrame; max ~8deg; disabled on touch).
- **Scroll parallax depth**: 3+ layers moving at different rates (translateZ/translate3d based,
  rAF-driven or CSS-only), creating real depth in hero or section transitions.
- **3D object built from CSS**: an actual composed 3D form — a product box, card stack, cube,
  ring, device mock — made of transformed planes with consistent lighting (gradient faces,
  believable shadows), idle-rotating or interaction-driven.
- **Canvas scene**: particle field, 3D-projected wireframe, starfield, flowing mesh, or
  generative ambient animation reacting subtly to pointer.
- **Hand-written WebGL shader background** (only if you can make it flawless): fragment-shader
  gradient flow/noise. Must feature-detect and fall back to CSS.
- **3D hover cards**: content cards that lift, tilt toward the cursor, and cast layered soft
  shadows with a specular sheen sweep.

Rules: 60fps feel — transform/opacity only, no layout thrash, all pointer handlers rAF-throttled.
Everything honors `prefers-reduced-motion: reduce` (freeze idle motion, keep a beautiful static
composition). Touch devices get the static composition, not broken tilt.

## The $10k design bar

- One committed art direction per site, grounded in the business — palette (5–7 values), type
  pairing, layout geometry, motion personality. The 12 must look like 12 different studios.
- A signature hero set-piece: the 3D moment lives here. No generic "headline + two buttons on
  a gradient".
- Orchestrated entrance: staged reveal on load (150–600ms stagger), scroll-triggered section
  reveals via IntersectionObserver (subtle: 12–24px translate + fade, once).
- Micro-interactions on every interactive element: buttons with press states, links with
  animated underlines/sweeps, inputs with focus glow.
- Depth system: consistent elevation language (shadow ramp), glass/blur layers where they fit
  the direction (`backdrop-filter` with solid fallback).
- Banned: the v1 look repeated, purple-blue gradient on white, cream+terracotta+serif default,
  emoji as section markers, identical card grids across sites, Bootstrap-feeling layouts.

## The 12 NEW businesses (all different from v1)

Category strings (exact): `Professional`, `Tech`, `Lifestyle`, `Entertainment`.

**Agent 1 — Professional**
1. `vantage-law` — "Vantage & Rowe", modern litigation law firm. Monolithic confidence: deep
   ink/graphite, marble-vein neutrals, one authority accent (oxblood or imperial blue). Didone
   display. 3D: mouse-tilt hero of layered typographic slabs like stacked case files; practice
   areas as 3D hover cards. Sections: results (real verdict figures), practice areas, partners,
   consultation CTA.
2. `axiom-architecture` — "Axiom Atelier", architecture studio. Blueprint-meets-gallery: bone
   white, graphite, cyan blueprint accent. 3D: CSS-built rotating building massing model
   (extruded planes) in hero; project cards with parallax depth. Sections: selected works,
   process, studio, awards, contact.
3. `northgate-dental` — "Northgate Smile Studio", boutique dental clinic. Calm clinical warmth:
   porcelain, seafoam, soft coral accent. Rounded geometry. 3D: floating glass panels with
   parallax + canvas particle "clean air" ambient; service cards tilt. Sections: services with
   prices, doctors, technology, booking, insurance.

**Agent 2 — Tech**
4. `helios-ev` — "Helios Motors", electric performance car brand. Cinematic dark: obsidian,
   solar gold, white. 3D: CSS 3D car silhouette/stage with rotating light sweep OR WebGL glow
   backdrop; spec counters animate; scroll parallax stage. Sections: model lineup with specs +
   prices, range/charging, design story, reserve CTA.
5. `neuraflow-ai` — "Neuraflow", AI infrastructure startup. Not the clichéd purple: pick e.g.
   deep green-black + phosphor + silver. 3D: canvas neural particle mesh reacting to cursor;
   3D code-terminal mock built from planes. Sections: product, how it works (pipeline diagram
   in SVG), benchmarks table, pricing, docs CTA.
6. `orbital-imaging` — "Orbital", drone survey & aerial imaging co. Atmosphere: stratosphere
   blues, horizon amber. 3D: parallax cloud/terrain layers with a CSS 3D drone that tilts with
   cursor; altitude-styled stats. Sections: services, industries, flight log case studies,
   certifications, quote CTA.

**Agent 3 — Lifestyle**
7. `onyx-grooming` — "Onyx Chair Co.", premium barbershop. Noir editorial: near-black, smoke,
   brass razor accent. Slab or mono details. 3D: hero with 3D rotating clipper/razor built from
   CSS planes or layered SVG with tilt; price list as engraved card stack. Sections: services +
   prices, barbers, the ritual, booking, house rules.
8. `solstice-spa` — "Solstice Bathhouse", wellness spa & sauna. Mineral serenity: travertine,
   eucalyptus, dusk lavender-grey (not purple-gradient). 3D: slow parallax steam/light layers,
   canvas ambient mist; ritual cards float gently. Sections: rituals with durations/prices,
   circuits, gift cards, membership, visit.
9. `aurea-jewelry` — "Aurea", fine jewelry house. Dark velvet + candlelight gold. Didone
   display. 3D: CSS 3D rotating ring/gem built from faceted planes with specular sweep;
   product cards with tilt + sheen. Sections: collections with prices, craftsmanship, bespoke
   process, boutique visits.

**Agent 4 — Entertainment**
10. `resonance-studios` — "Resonance", recording studio. Analog warmth in the dark: charcoal,
    VU-meter amber, cable red. Mono + grotesque. 3D: canvas waveform/frequency visualizer as
    living hero; 3D console fader panel from CSS planes. Sections: rooms & gear with day rates,
    engineers, notable sessions, booking.
11. `nova-esports` — "Nova Esports", pro gaming organization. Electric contrast: void black,
    plasma cyan, signal magenta — handled with restraint, not vaporwave soup. 3D: WebGL/canvas
    starfield warp + 3D jersey/logo card tilt; stats HUD styling. Sections: teams & rosters,
    trophy record, upcoming matches, sponsors as typographic marks, shop teaser.
12. `alta-basecamp` — "Alta Basecamp", adventure travel outfitter. Alpine dawn: glacier blues,
    granite, ember orange. 3D: layered mountain parallax (SVG ridgelines at depths) with slow
    cloud drift; expedition cards tilt. Sections: expeditions with dates/prices/difficulty,
    guides, gear included, booking, safety record.

## Metadata (same shape as v1)

Per template: `id`, `name`, `category` (exact string above), `tagline` (≤60 chars),
`description` (one Forma-marketing sentence), `accent` (hex), `file` (absolute path).

## Agent 5 — Shell v2 ("Forma — Premium Collection")

Rebuild the shell to the same $10k bar. Everything from v1's contract holds:

- Exact placeholder: `<script id="templates-data" type="application/json">__TEMPLATES_JSON__</script>`,
  runtime JSON.parse with try/catch empty state, cards built from the array in order,
  fields {id, name, category, tagline, description, accent, html}.
- Live scaled iframe thumbnails (srcdoc, 1280px virtual width, transform scale, clipped,
  pointer-events none, lazy). Fullscreen modal with Desktop/Tablet(768)/Mobile(390) toggles,
  Esc close, focus trap, scroll lock, animated width transitions.
- Filter bar with counts — categories now: All / Professional / Tech / Lifestyle / Entertainment.
- Theme-aware token pattern (:root vars, prefers-color-scheme dark, then
  :root[data-theme="dark"] / :root[data-theme="light"] winning overrides). Both themes superb.
- `<title>Forma — Website Builder Template Showcase</title>`.

**New for v2:** the shell itself gets the 3D treatment — template cards tilt toward the cursor
with layered shadows and a sheen sweep; hero has a dimensional set-piece (e.g. a fanned 3D
stack of the templates, or type set in perspective) with staged entrance; a quiet ambient
background (canvas grain/particles or layered gradients) that never fights the thumbnails.
Copy updated to sell the premium collection ("Twelve businesses. Twelve one-off builds.").
Keep it fast: transform/opacity only, rAF-throttled pointer work, reduced-motion respected.
