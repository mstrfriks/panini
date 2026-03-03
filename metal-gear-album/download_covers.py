#!/usr/bin/env python3
"""
Télécharge les jaquettes Metal Gear depuis RAWG.io
et les place dans le dossier covers/

Usage : python download_covers.py VOTRE_CLE_API
Clé gratuite sur : https://rawg.io/apidocs
"""

import urllib.request
import urllib.parse
import json
import os
import sys
import time

# ── Clé API ────────────────────────────────────────────────────────────────
if len(sys.argv) < 2:
    print('Usage : python download_covers.py VOTRE_CLE_API')
    print('Clé gratuite sur : https://rawg.io/apidocs')
    sys.exit(1)

API_KEY = sys.argv[1]

# ── Liste des jeux : (id_fichier, titre_de_recherche) ─────────────────────
GAMES = [
    ('001', 'Metal Gear 1987'),
    ('002', 'Metal Gear 2 Solid Snake'),
    ('003', 'Metal Gear Solid 1998'),
    ('004', 'Metal Gear Solid 2 Sons of Liberty'),
    ('005', 'Metal Gear Solid The Twin Snakes'),
    ('006', 'Metal Gear Solid 4 Guns of the Patriots'),
    ('007', 'Metal Gear Solid 3 Snake Eater'),
    ('008', 'Metal Gear Solid Portable Ops'),
    ('009', 'Metal Gear Solid Peace Walker'),
    ('010', 'Metal Gear Solid V Ground Zeroes'),
    ('011', 'Metal Gear Solid V The Phantom Pain'),
    ('012', 'Metal Gear Rising Revengeance'),
    ('013', 'Metal Gear Survive'),
]

COVERS_DIR = 'covers'
os.makedirs(COVERS_DIR, exist_ok=True)


def search_rawg(title):
    """Cherche un jeu sur RAWG et renvoie l'URL de l'image."""
    query = urllib.parse.urlencode({'search': title, 'page_size': 3, 'key': API_KEY})
    url = f'https://api.rawg.io/api/games?{query}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        results = data.get('results', [])
        for game in results:
            img = game.get('background_image')
            if img:
                return img, game.get('name', '?')
    except Exception as e:
        print(f'  Erreur RAWG: {e}')
    return None, None


def download_image(url, dest_path):
    """Télécharge une image vers dest_path."""
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=15) as r:
        data = r.read()
    with open(dest_path, 'wb') as f:
        f.write(data)
    return len(data)


# ── Téléchargement ─────────────────────────────────────────────────────────
print('=' * 55)
print('  Metal Gear — Téléchargement des jaquettes')
print('=' * 55)

for gid, title in GAMES:
    dest = os.path.join(COVERS_DIR, f'{gid}.jpg')

    # Sauter si déjà téléchargé (et pas un placeholder minuscule)
    if os.path.exists(dest) and os.path.getsize(dest) > 10_000:
        print(f'  ✓ {gid}.jpg  déjà présent, ignoré')
        continue

    print(f'  → {gid}  {title}')
    img_url, found_name = search_rawg(title)

    if img_url:
        try:
            size = download_image(img_url, dest)
            print(f'     ✓  "{found_name}"  ({size//1024} ko)')
        except Exception as e:
            print(f'     ✗  Échec téléchargement : {e}')
    else:
        print(f'     ✗  Aucun résultat trouvé')

    time.sleep(0.5)  # pause pour ne pas spammer l'API

print()
print('Terminé ! Ouvrez index.html dans votre navigateur.')
