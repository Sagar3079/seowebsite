# Forma — Website Builder Template Showcase

A single self-contained showcase site for a fictional website builder called **Forma**,
featuring **12 fully working demo websites** across 4 categories, browsable in a gallery
with live scaled-down previews, category filters, and a fullscreen preview modal with
desktop / tablet / mobile device toggles.

## Templates

| Category | Templates |
|---|---|
| Hospitality | Ember & Oak (restaurant) · Daybreak Roasters (coffee) · The Linden House (hotel) |
| Business | Pulse (SaaS analytics) · Studio North (agency) · Meridian Advisory (financial) |
| Commerce | Atelier Noir (fashion) · Kickflip Supply (skate shop) · Hearth & Haven (ceramics) |
| Creative | Mara Voss (photography) · June & Theo (wedding) · Forge Fitness (training) |

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
