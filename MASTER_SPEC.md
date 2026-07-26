# MASTER SPEC — "Forma" Website-Builder Template Showcase

## What we are building

A single, self-contained showcase website for a fictional website builder called **Forma**.
The showcase presents **12 fully working demo websites** ("templates") that Forma can supposedly
produce. Visitors browse a gallery of live template thumbnails, filter by category, and open any
template in a fullscreen preview with desktop / tablet / mobile device toggles.

The final deliverable is ONE self-contained HTML page (the shell) with all 12 demo sites embedded
as JSON and rendered in sandboxed iframes via `srcdoc`.

## Hard technical constraints (apply to EVERY file)

1. **Fully self-contained.** A strict CSP blocks ALL external requests. No CDN scripts, no Google
   Fonts, no remote images, no fetch/XHR. Everything inline in one HTML file per site.
2. **Fonts:** system font stacks ONLY. Use them deliberately — e.g.
   - Humanist sans: `Seravek, 'Gill Sans Nova', Ubuntu, Calibri, 'DejaVu Sans', source-sans-pro, sans-serif`
   - Neo-grotesque: `Inter, Roboto, 'Helvetica Neue', 'Arial Nova', 'Nimbus Sans', Arial, sans-serif`
   - Transitional serif: `Charter, 'Bitstream Charter', 'Sitka Text', Cambria, serif`
   - Didone: `Didot, 'Bodoni MT', 'Noto Serif Display', 'URW Palladio L', P052, serif`
   - Old-style serif: `'Iowan Old Style', 'Palatino Linotype', 'URW Palladio L', P052, serif`
   - Slab: `Rockwell, 'Rockwell Nova', 'Roboto Slab', 'DejaVu Serif', 'Sitka Small', serif`
   - Monospace: `ui-monospace, 'Cascadia Code', 'Source Code Pro', Menlo, Consolas, 'DejaVu Sans Mono', monospace`
   - Geometric sans: `Avenir, Montserrat, Corbel, 'URW Gothic', source-sans-pro, sans-serif`
   Different demos MUST use different stacks so each feels distinct.
3. **Images:** none from network. Build visuals from CSS gradients, patterns, inline SVG, and
   canvas. No `<img src="http...">`. Emoji allowed sparingly where it fits the brand (not as
   section markers).
4. **Each demo site is a complete standalone HTML document**: `<!DOCTYPE html>`, `<html>`, `<head>`
   with `<meta charset>` + `<meta name="viewport">` + `<title>`, inline `<style>`, body content,
   optional inline `<script>` at the end. It must render perfectly when loaded alone in a browser
   AND inside an iframe via `srcdoc`.
5. **Responsive:** every demo must look right at 390px, 768px, and 1280px wide. The shell's device
   toggle will show all three. No horizontal page scroll at any width.
6. **Size budget:** 15–45 KB per demo file. Lean, hand-tuned CSS. No frameworks.
7. **JS is optional per demo** — small touches only (mobile nav toggle, scroll reveal, tab switch,
   simple counters). Everything must degrade gracefully without JS. Respect
   `prefers-reduced-motion`.
8. **Quality bar:** close every tag, double-quote attributes, visible keyboard focus states,
   WCAG-legible contrast. No lorem ipsum anywhere — write real, specific copy with names, prices,
   dates, menus, testimonials.

## Design direction (applies to every demo)

Each demo is a *portfolio piece* for the fictional builder — it must look like a real small
business paid a good studio for it. Every demo needs:

- A distinct palette (4–6 values) grounded in its subject. Neutrals with a hue bias toward the
  accent, never pure mid-grey.
- A deliberate typeface pairing from the stacks above — display + body, different per demo.
- A real layout idea, not just centered stacks: asymmetric grids, editorial columns, split
  screens, sticky sidebars, overlapping cards — pick what the subject calls for.
- Complete IA: nav (with mobile behavior), hero, 3–5 content sections, footer with real details.
- **Banned clichés:** purple-blue gradient hero on white; warm-cream + terracotta + serif combo
  used twice; emoji section markers; numbered 01/02/03 markers unless content is truly sequential;
  everything-centered layouts; identical rounded-card grids across demos.

## The 12 demos, their agents, categories, and IDs

Category filter values (exact strings): `Hospitality`, `Business`, `Commerce`, `Creative`.

**Agent 1 — Hospitality**
1. `ember-oak` — "Ember & Oak", wood-fire fine-dining restaurant. Moody, candlelit: deep charcoal,
   ember orange, brass. Didone or old-style serif display. Tasting menu with prices, chef bio,
   reservations CTA, hours/location footer.
2. `daybreak-roasters` — "Daybreak Roasters", specialty coffee roastery + café. Warm daylight
   palette (bone, roast brown, sunrise yellow accent). Menu board, bean subscription cards with
   prices, brew guide section, two locations.
3. `linden-house` — "The Linden House", 9-room boutique countryside hotel. Calm, botanical:
   sage/moss, linen, ink. Serif display. Room types with nightly rates, seasonal offers,
   breakfast/garden story section, booking CTA.

**Agent 2 — Business**
4. `pulse-analytics` — "Pulse", SaaS product analytics tool. Dark UI-chrome aesthetic OR crisp
   light data aesthetic (pick one, commit). Product hero with a believable dashboard mock built in
   pure CSS/SVG (charts, sparklines, metric tiles), feature grid, 3-tier pricing, customer quote.
5. `studio-north` — "Studio North", 8-person brand & web design agency. Confident editorial
   layout, oversized type, selected-work case grid with CSS-art thumbnails, services list,
   client logos as typographic wordmarks, contact section.
6. `meridian-advisory` — "Meridian Advisory", boutique financial planning firm. Trustworthy,
   quiet luxury: deep navy or forest, warm paper, one metallic-feel accent. Serif + humanist
   sans. Services, 3 advisors with initials-monogram avatars (CSS), fee philosophy, compliance
   footer.

**Agent 3 — Commerce**
7. `atelier-noir` — "Atelier Noir", minimal fashion boutique. Near-monochrome with one accent;
   high fashion editorial feel, generous whitespace, product grid (6+ garments, names + prices)
   with CSS-art product cards, lookbook strip, newsletter signup.
8. `kickflip-supply` — "Kickflip Supply", skate shop + limited sneaker drops. Loud, energetic:
   poster-like type collisions, sticker/stamp motifs in CSS, drop countdown (JS), product cards
   with prices, crew/community section.
9. `hearth-home` — "Hearth & Haven", handmade ceramics and home goods. Soft clay tones,
   craft-market warmth. Product bestsellers grid with prices, maker story with process steps,
   markets calendar, gift-card CTA.

**Agent 4 — Creative**
10. `mara-voss` — "Mara Voss — Photographer". Gallery-first portfolio: full-bleed CSS/SVG
    "photograph" compositions (abstract gradient-scapes standing in for photos), project index
    list, about + awards, booking contact. Typography-forward, quiet chrome.
11. `june-theo` — "June & Theo", wedding website. Romantic but modern (not cream+terracotta):
    e.g. ink + blush + garden green. Date/venue hero, love-story timeline (genuinely sequential),
    schedule, RSVP form (non-submitting, validates inline), registry links, FAQ.
12. `forge-fitness` — "Forge Fitness", personal training studio. High-contrast athletic feel,
    condensed/heavy type treatment, class schedule table, coach cards, transformation stats,
    membership pricing, free-trial CTA.

## Metadata each agent must return (structured output)

For every demo built, return: `id` (exact ID above), `name`, `category` (exact string),
`tagline` (≤60 chars, the business's own tagline), `description` (one sentence about the
template, written as Forma marketing copy, e.g. "A moody, reservation-driven template for
restaurants that take their fire seriously."), `accent` (one hex color representing the demo,
used by the shell for chips/hover), `file` (absolute path of the written HTML file).

## Agent 5 — The shell ("Forma" showcase site itself)

One HTML file: the marketing/showcase site for Forma. It is the artifact users see first —
it must be the best-designed page of all 13.

**Brand:** Forma — tagline direction: "Websites that feel designed." Voice: confident, craft-led,
zero corporate filler.

**Required structure:**
1. Slim sticky nav: Forma wordmark (typographic, no image), links: Templates, Why Forma, CTA
   button "Start building" (scrolls to gallery).
2. Hero: strong typographic thesis + one-line subhead + small stat row (12 templates ·
   4 categories · 100% yours). No giant empty hero; get to the gallery fast.
3. **Template gallery (the core):**
   - Filter bar: All / Hospitality / Business / Commerce / Creative (exact category strings),
     with counts. Filtering is instant (JS show/hide), keyboard accessible.
   - Grid of 12 template cards. Each card shows a **live scaled-down preview**: an
     `<iframe loading="lazy">` whose `srcdoc` is the demo's full HTML, rendered at 1280px
     virtual width and scaled with `transform: scale()` inside a fixed-ratio clipped container
     (pointer-events: none on the thumbnail iframe). Below: template name, category chip
     (tinted with the template's accent), tagline, "Preview" button.
4. **Fullscreen preview modal:** opens on card click/Enter. Contains: top bar with template name,
   device toggles — Desktop (100%), Tablet (768px), Mobile (390px) — an "Open in new tab" note is
   NOT needed, and a close button (Esc works, focus is trapped, background scroll locked). Body:
   the demo in an iframe (`srcdoc`), centered, device-width applied with a smooth transition,
   subtle device frame at tablet/mobile widths.
5. "Why Forma" strip: 3 short, concrete value props (own your code, real typography, ships
   fast — write them properly).
6. Footer: Forma wordmark, small print, "Built with Forma" wink.

**Data contract:** the shell must NOT hardcode the 12 demos. It must contain exactly:
```html
<script id="templates-data" type="application/json">__TEMPLATES_JSON__</script>
```
and at runtime `JSON.parse(document.getElementById('templates-data').textContent)` — an array of
objects `{id, name, category, tagline, description, accent, html}` where `html` is the complete
demo document. Build cards and modal from this array in JS. Cards render in the array order.
The build step replaces `__TEMPLATES_JSON__` with real JSON (it will never contain a literal
`</script`). Handle the placeholder gracefully during development (try/catch → show a "templates
loading" empty state if parse fails).

**Shell theming:** theme-aware. Define palette as CSS custom properties on `:root`; redefine
tokens under `@media (prefers-color-scheme: dark)`, then again under `:root[data-theme="dark"]`
and `:root[data-theme="light"]` so the host's theme toggle wins in both directions. Both themes
fully designed. Demo iframes keep their own internal look — only the shell chrome adapts.

**Shell design bar:** must not look templated. Avoid the banned clichés above. Pick a
characterful display stack + quiet body stack from the approved list. One deliberate signature
moment (e.g. the hero wordmark set huge with tight tracking, or template cards that tilt subtly
on hover) — spend boldness once, keep the rest quiet.

**Shell title:** `<title>Forma — Website Builder Template Showcase</title>`.
Size budget for the shell alone (without injected JSON): ≤ 60 KB.
