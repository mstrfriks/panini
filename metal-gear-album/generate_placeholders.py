#!/usr/bin/env python3
"""
Genere des images placeholder 300x450 (ratio 2/3) pour chaque jeu.
Remplacez chaque fichier covers/XXX.jpg par la vraie cover du jeu.
"""
import struct, zlib, os

GAMES = [
    ('001', 'Metal Gear', 1987),
    ('002', 'Metal Gear 2: Solid Snake', 1990),
    ('003', 'Metal Gear Solid', 1998),
    ('004', 'Metal Gear Solid 2: Sons of Liberty', 2001),
    ('005', 'MGS: The Twin Snakes', 2004),
    ('006', 'MGS4: Guns of the Patriots', 2008),
    ('007', 'Metal Gear Solid 3: Snake Eater', 2004),
    ('008', 'MGS: Portable Ops', 2006),
    ('009', 'MGS: Peace Walker', 2010),
    ('010', 'MGSV: Ground Zeroes', 2014),
    ('011', 'MGSV: The Phantom Pain', 2015),
    ('012', 'Metal Gear Rising: Revengeance', 2013),
    ('013', 'Metal Gear Survive', 2018),
]

W, H = 300, 450

COLORS = [
    (40,80,55),(55,70,40),(30,65,65),(65,50,35),(40,55,75),(70,40,50),
    (35,75,45),(60,60,30),(45,40,80),(50,70,55),(75,45,40),(35,65,55),(55,55,45),
]

def png_chunk(name, data):
    crc = zlib.crc32(name + data) & 0xffffffff
    return struct.pack('>I', len(data)) + name + data + struct.pack('>I', crc)

def make_png(filepath, r, g, b):
    raw = b''.join(b'\x00' + bytes([r, g, b] * W) for _ in range(H))
    ihdr = struct.pack('>IIBBBBB', W, H, 8, 2, 0, 0, 0)
    idat = zlib.compress(raw)
    with open(filepath, 'wb') as f:
        f.write(b'\x89PNG\r\n\x1a\n')
        f.write(png_chunk(b'IHDR', ihdr))
        f.write(png_chunk(b'IDAT', idat))
        f.write(png_chunk(b'IEND', b''))

os.makedirs('covers', exist_ok=True)
for i, (gid, title, year) in enumerate(GAMES):
    path = f'covers/{gid}.jpg'
    col = COLORS[i % len(COLORS)]
    make_png(path, col[0], col[1], col[2])
    print(f'  {path}  ({title})')

print(f'\n{len(GAMES)} placeholders crees dans covers/')
