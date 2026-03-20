import random

COVER_COLORS = [
    ("#111", "#ffffff"),
    ("#222", "#fefefe"),
]

COVER_TITLES = [
    "Cute Animals Coloring Book",
    "Magical Kids Coloring Book",
    "Fun Adventures Coloring Book",
    "Happy Children Coloring Book",
]

SUBTITLES = [
    "30 fun pages for kids",
    "Easy and adorable illustrations",
    "Perfect for ages 4 to 8",
]

def generate_cover_svg(title: str | None = None, subtitle: str | None = None) -> str:
    bg, fg = random.choice(COVER_COLORS)
    title = title or random.choice(COVER_TITLES)
    subtitle = subtitle or random.choice(SUBTITLES)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 2560">
<rect width="1600" height="2560" fill="{bg}"/>
<rect x="70" y="70" width="1460" height="2420" rx="40" fill="none" stroke="{fg}" stroke-width="8"/>
<text x="800" y="350" text-anchor="middle" font-family="Arial" font-size="110" font-weight="700" fill="{fg}">{title}</text>
<text x="800" y="470" text-anchor="middle" font-family="Arial" font-size="52" fill="{fg}">{subtitle}</text>
<circle cx="800" cy="1250" r="290" fill="none" stroke="{fg}" stroke-width="10"/>
<circle cx="720" cy="1180" r="20" fill="{fg}"/>
<circle cx="880" cy="1180" r="20" fill="{fg}"/>
<path d="M 700 1330 Q 800 1420 900 1330" fill="none" stroke="{fg}" stroke-width="10" stroke-linecap="round"/>
<text x="800" y="2270" text-anchor="middle" font-family="Arial" font-size="48" fill="{fg}">ColorIA Studio</text>
</svg>'''