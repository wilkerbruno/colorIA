import random
from engine.characters_pro import draw_character
from engine.poses_pro import add_pose_running, add_pose_jump, add_pose_standing

POSE_FUNCS = [add_pose_running, add_pose_jump, add_pose_standing]

def generate_svg_pro(prompt: str = "coloring page") -> str:
    cx, cy = 250, 170
    pose = random.choice(POSE_FUNCS)

    parts = []
    parts += draw_character(cx, cy, 1.0)
    parts += pose(cx, cy, 1.0)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
viewBox="0 0 500 500"
stroke-linecap="round"
stroke-linejoin="round">
<rect width="500" height="500" fill="white"/>
{"".join(parts)}
</svg>'''
    return svg