# Forma — Website Builder Template Showcase

A single self-contained showcase site for a fictional website builder called **Forma** —
the **Premium Collection**: 12 fully working, agency-grade demo business websites, each with
real 3D design work (mouse-tilt perspective heroes, scroll parallax depth, CSS-built 3D
objects, canvas/particle scenes), browsable in a gallery with live scaled-down previews,
category filters, and a fullscreen preview modal with desktop / tablet / mobile toggles.

## Templates

| Category | Templates |
|---|---|
| Professional | Vantage & Rowe (law firm) · Axiom Atelier (architecture) · Northgate Smile Studio (dental) |
| Tech | Helios Motors (electric cars) · Neuraflow (AI infrastructure) · Orbital (drone imaging) |
| Lifestyle | Onyx Chair Co. (barbershop) · Solstice Bathhouse (spa) · Aurea (jewelry) |
| Entertainment | Resonance (recording studio) · Nova Esports (gaming org) · Alta Basecamp (adventure travel) |

## Structure

- `index.html` — the final assembled site (open this in a browser; no server needed)
- `shell.html` — the Forma showcase shell with a `__TEMPLATES_JSON__` placeholder
- `demos/*.html` — the 12 standalone demo sites (each works on its own)
- `demos/meta-*.json` — per-category template metadata
- `MASTER_SPEC.md` — the design/build spec the site was generated from
- `build.py` — injects the demos into the shell to produce `index.html`

## Build

```sh
python3 build.py
```

Everything is fully self-contained: no external fonts, scripts, or images —
system font stacks, CSS/SVG art, and inline JS only.
