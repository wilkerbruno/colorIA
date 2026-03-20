import random

DECORATIONS=[
"estrela",
"flor",
"borboleta",
"folha",
"bolha",
"grama"
]

def decoration_svg(dec,cx,cy):

    if dec=="estrela":

        return [f'''
<circle cx="{cx}" cy="{cy}" r="3" fill="black"/>
''']

    if dec=="flor":

        return [f'''
<circle cx="{cx}" cy="{cy}" r="6"
stroke="black"
stroke-width="2"
fill="none"/>
''']

    return []