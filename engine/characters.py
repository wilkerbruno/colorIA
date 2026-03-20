import random

HAIR = [
    "curto",
    "longo",
    "cacheado",
    "topete",
    "tranca"
]

HEAD_SIZE = [28,30,32,34]

def character_svg(cx,cy,scale=1):

    head=random.choice(HEAD_SIZE)

    svg=[]

    svg.append(f'''
<circle cx="{cx}" cy="{cy}"
r="{head*scale}"
stroke="black"
stroke-width="3"
fill="none"/>
''')

    svg.append(f'''
<circle cx="{cx-10*scale}" cy="{cy-5*scale}" r="4" fill="black"/>
<circle cx="{cx+10*scale}" cy="{cy-5*scale}" r="4" fill="black"/>
''')

    svg.append(f'''
<path d="M {cx-12} {cy+8} Q {cx} {cy+18} {cx+12} {cy+8}"
stroke="black"
stroke-width="3"
fill="none"/>
''')

    svg.append(f'''
<ellipse cx="{cx}"
cy="{cy+60}"
rx="26"
ry="42"
stroke="black"
stroke-width="3"
fill="none"/>
''')

    return svg