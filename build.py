#!/usr/bin/env python3
"""Assemble the Forma showcase: inject the 12 demo templates into the shell.

Usage: python3 build.py  ->  writes index.html
"""
import json
import os

ORDER = [
    'vantage-law', 'axiom-architecture', 'northgate-dental',
    'helios-ev', 'neuraflow-ai', 'orbital-imaging',
    'onyx-grooming', 'solstice-spa', 'aurea-jewelry',
    'resonance-studios', 'nova-esports', 'alta-basecamp',
    'saffron-vine', 'flour-fold', 'koya-ramen',
    'azure-cove', 'terra-fauna', 'aurora-air',
    'paper-bloom', 'oakline-studio', 'novel-house',
    'crestview-realty', 'hive-workspace', 'velvet-pine',
]
META_FILES = [
    'meta-professional.json', 'meta-tech.json', 'meta-lifestyle.json', 'meta-entertainment.json',
    'meta-food.json', 'meta-travel.json', 'meta-retail.json', 'meta-services.json',
]

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
