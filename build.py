#!/usr/bin/env python3
"""Assemble the Forma showcase: inject the 12 demo templates into the shell.

Usage: python3 build.py  ->  writes index.html
"""
import json
import os

ORDER = [
    'ember-oak', 'daybreak-roasters', 'linden-house',
    'pulse-analytics', 'studio-north', 'meridian-advisory',
    'atelier-noir', 'kickflip-supply', 'hearth-home',
    'mara-voss', 'june-theo', 'forge-fitness',
]
META_FILES = ['meta-hospitality.json', 'meta-business.json', 'meta-commerce.json', 'meta-creative.json']

root = os.path.dirname(os.path.abspath(__file__))
demos = os.path.join(root, 'demos')

meta = {}
for name in META_FILES:
    with open(os.path.join(demos, name)) as f:
        for entry in json.load(f):
            meta[entry['id']] = entry

templates = []
for tid in ORDER:
    entry = meta[tid]
    with open(os.path.join(demos, f'{tid}.html')) as f:
        html = f.read()
    templates.append({
        'id': entry['id'], 'name': entry['name'], 'category': entry['category'],
        'tagline': entry['tagline'], 'description': entry['description'],
        'accent': entry['accent'], 'html': html,
    })

with open(os.path.join(root, 'shell.html')) as f:
    shell = f.read()
assert shell.count('__TEMPLATES_JSON__') == 1

# <\/ keeps the JSON valid while making a literal </script inside template HTML
# impossible, so the application/json block can't be terminated early.
payload = json.dumps(templates, ensure_ascii=False).replace('</', '<\\/')
with open(os.path.join(root, 'index.html'), 'w') as f:
    f.write(shell.replace('__TEMPLATES_JSON__', payload))
print(f'index.html written: {len(templates)} templates')
