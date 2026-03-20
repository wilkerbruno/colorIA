import random

POSES=[
"correndo",
"pulando",
"chutando",
"acenar",
"andando",
"brincando",
"dançando",
"sentado"
]

def random_pose():
    return random.choice(POSES)