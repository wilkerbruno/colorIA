def add_pose_running(cx: int, cy: int, s: float = 1.0) -> list[str]:
    return [
        f'<line x1="{cx-24*s}" y1="{cy+52*s}" x2="{cx-58*s}" y2="{cy+72*s}" stroke="#111" stroke-width="3" stroke-linecap="round"/>',
        f'<line x1="{cx+24*s}" y1="{cy+52*s}" x2="{cx+60*s}" y2="{cy+28*s}" stroke="#111" stroke-width="3" stroke-linecap="round"/>',
        f'<line x1="{cx-10*s}" y1="{cy+98*s}" x2="{cx-40*s}" y2="{cy+128*s}" stroke="#111" stroke-width="3" stroke-linecap="round"/>',
        f'<line x1="{cx+10*s}" y1="{cy+98*s}" x2="{cx+44*s}" y2="{cy+136*s}" stroke="#111" stroke-width="3" stroke-linecap="round"/>',
        f'<ellipse cx="{cx-42*s}" cy="{cy+130*s}" rx="{10*s}" ry="{4*s}" stroke="#111" stroke-width="3" fill="none"/>',
        f'<ellipse cx="{cx+46*s}" cy="{cy+138*s}" rx="{10*s}" ry="{4*s}" stroke="#111" stroke-width="3" fill="none"/>',
    ]

def add_pose_jump(cx: int, cy: int, s: float = 1.0) -> list[str]:
    return [
        f'<line x1="{cx-24*s}" y1="{cy+52*s}" x2="{cx-62*s}" y2="{cy+42*s}" stroke="#111" stroke-width="3" stroke-linecap="round"/>',
        f'<line x1="{cx+24*s}" y1="{cy+52*s}" x2="{cx+62*s}" y2="{cy+42*s}" stroke="#111" stroke-width="3" stroke-linecap="round"/>',
        f'<line x1="{cx-10*s}" y1="{cy+98*s}" x2="{cx-36*s}" y2="{cy+132*s}" stroke="#111" stroke-width="3" stroke-linecap="round"/>',
        f'<line x1="{cx+10*s}" y1="{cy+98*s}" x2="{cx+36*s}" y2="{cy+132*s}" stroke="#111" stroke-width="3" stroke-linecap="round"/>',
        f'<ellipse cx="{cx-38*s}" cy="{cy+134*s}" rx="{10*s}" ry="{4*s}" stroke="#111" stroke-width="3" fill="none"/>',
        f'<ellipse cx="{cx+38*s}" cy="{cy+134*s}" rx="{10*s}" ry="{4*s}" stroke="#111" stroke-width="3" fill="none"/>',
    ]

def add_pose_standing(cx: int, cy: int, s: float = 1.0) -> list[str]:
    return [
        f'<line x1="{cx-24*s}" y1="{cy+52*s}" x2="{cx-54*s}" y2="{cy+70*s}" stroke="#111" stroke-width="3" stroke-linecap="round"/>',
        f'<line x1="{cx+24*s}" y1="{cy+52*s}" x2="{cx+54*s}" y2="{cy+70*s}" stroke="#111" stroke-width="3" stroke-linecap="round"/>',
        f'<line x1="{cx-10*s}" y1="{cy+98*s}" x2="{cx-16*s}" y2="{cy+142*s}" stroke="#111" stroke-width="3" stroke-linecap="round"/>',
        f'<line x1="{cx+10*s}" y1="{cy+98*s}" x2="{cx+16*s}" y2="{cy+142*s}" stroke="#111" stroke-width="3" stroke-linecap="round"/>',
        f'<ellipse cx="{cx-16*s}" cy="{cy+146*s}" rx="{10*s}" ry="{4*s}" stroke="#111" stroke-width="3" fill="none"/>',
        f'<ellipse cx="{cx+16*s}" cy="{cy+146*s}" rx="{10*s}" ry="{4*s}" stroke="#111" stroke-width="3" fill="none"/>',
    ]