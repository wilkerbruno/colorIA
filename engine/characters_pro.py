import random

FACE_TYPES = ["round", "soft_oval"]
HAIR_TYPES = ["short", "bob", "curly", "spiky", "pigtails"]
OUTFITS = ["tshirt", "dress", "overalls", "hoodie"]

def draw_head(cx: int, cy: int, s: float = 1.0) -> list[str]:
    return [
        f'<circle cx="{cx}" cy="{cy}" r="{34*s}" stroke="#111" stroke-width="3" fill="none"/>',
        f'<circle cx="{cx-10*s}" cy="{cy-4*s}" r="{4*s}" fill="#111"/>',
        f'<circle cx="{cx+10*s}" cy="{cy-4*s}" r="{4*s}" fill="#111"/>',
        f'<circle cx="{cx-8*s}" cy="{cy-6*s}" r="{1.2*s}" fill="white"/>',
        f'<circle cx="{cx+12*s}" cy="{cy-6*s}" r="{1.2*s}" fill="white"/>',
        f'<path d="M {cx-11*s} {cy+9*s} Q {cx} {cy+18*s} {cx+11*s} {cy+9*s}" stroke="#111" stroke-width="3" fill="none" stroke-linecap="round"/>'
    ]

def draw_hair(cx: int, cy: int, hair: str = "short", s: float = 1.0) -> list[str]:
    if hair == "bob":
        return [f'''
<path d="
M {cx-28*s} {cy-18*s}
Q {cx-14*s} {cy-48*s} {cx} {cy-30*s}
Q {cx+15*s} {cy-52*s} {cx+30*s} {cy-18*s}
M {cx-27*s} {cy-16*s} Q {cx-34*s} {cy+18*s} {cx-18*s} {cy+42*s}
M {cx+27*s} {cy-16*s} Q {cx+34*s} {cy+18*s} {cx+18*s} {cy+42*s}
" stroke="#111" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
''']
    if hair == "curly":
        parts = []
        for dx in [-22, -10, 0, 10, 22]:
            parts.append(f'<circle cx="{cx+dx*s}" cy="{cy-28*s}" r="{7*s}" stroke="#111" stroke-width="2.4" fill="none"/>')
        return parts
    if hair == "spiky":
        return [f'''
<path d="
M {cx-28*s} {cy-18*s}
L {cx-18*s} {cy-42*s}
L {cx-8*s} {cy-26*s}
L {cx+2*s} {cy-48*s}
L {cx+12*s} {cy-26*s}
L {cx+24*s} {cy-40*s}
L {cx+30*s} {cy-18*s}
" stroke="#111" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
''']
    if hair == "pigtails":
        return [f'''
<path d="
M {cx-28*s} {cy-18*s}
Q {cx-14*s} {cy-48*s} {cx} {cy-30*s}
Q {cx+15*s} {cy-52*s} {cx+30*s} {cy-18*s}
M {cx-27*s} {cy-12*s} Q {cx-44*s} {cy+2*s} {cx-34*s} {cy+24*s}
M {cx+27*s} {cy-12*s} Q {cx+44*s} {cy+2*s} {cx+34*s} {cy+24*s}
" stroke="#111" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
''']
    return [f'''
<path d="
M {cx-28*s} {cy-18*s}
Q {cx-12*s} {cy-48*s} {cx} {cy-30*s}
Q {cx+14*s} {cy-52*s} {cx+30*s} {cy-18*s}
" stroke="#111" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
''']

def draw_body(cx: int, cy: int, outfit: str = "tshirt", s: float = 1.0) -> list[str]:
    if outfit == "dress":
        return [f'''
<path d="
M {cx-18*s} {cy+40*s}
Q {cx-22*s} {cy+78*s} {cx-36*s} {cy+112*s}
L {cx+36*s} {cy+112*s}
Q {cx+22*s} {cy+78*s} {cx+18*s} {cy+40*s}
Q {cx} {cy+28*s} {cx-18*s} {cy+40*s}
" stroke="#111" stroke-width="3" fill="none" stroke-linejoin="round"/>
''']
    if outfit == "overalls":
        return [f'''
<ellipse cx="{cx}" cy="{cy+62*s}" rx="{26*s}" ry="{38*s}" stroke="#111" stroke-width="3" fill="none"/>
<line x1="{cx-12*s}" y1="{cy+34*s}" x2="{cx-6*s}" y2="{cy+55*s}" stroke="#111" stroke-width="2.2"/>
<line x1="{cx+12*s}" y1="{cy+34*s}" x2="{cx+6*s}" y2="{cy+55*s}" stroke="#111" stroke-width="2.2"/>
<rect x="{cx-12*s}" y="{cy+54*s}" width="{24*s}" height="{16*s}" rx="{3*s}" stroke="#111" stroke-width="2.2" fill="none"/>
''']
    return [f'<ellipse cx="{cx}" cy="{cy+62*s}" rx="{26*s}" ry="{38*s}" stroke="#111" stroke-width="3" fill="none"/>']

def draw_character(cx: int, cy: int, s: float = 1.0) -> list[str]:
    hair = random.choice(HAIR_TYPES)
    outfit = random.choice(OUTFITS)
    svg = []
    svg += draw_head(cx, cy, s)
    svg += draw_hair(cx, cy, hair, s)
    svg += draw_body(cx, cy, outfit, s)
    return svg