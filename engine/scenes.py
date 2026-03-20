import random
from engine.characters import character_svg
from engine.objects import OBJECTS,object_svg
from engine.scenery import sun,cloud
from engine.decorations import DECORATIONS,decoration_svg

def generate_scene():

    els=[]

    els+=sun(420,80)
    els+=cloud(140,100)
    els+=cloud(320,120)

    els+=character_svg(250,220)

    obj=random.choice(OBJECTS)

    els+=object_svg(obj,340,340)

    for i in range(5):

        dec=random.choice(DECORATIONS)

        els+=decoration_svg(dec,random.randint(50,450),random.randint(50,450))

    return els