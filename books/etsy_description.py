def generate_etsy_description(title: str, theme: str, pages: int = 30) -> str:
    return f"""
{title}

Digital download coloring book featuring {pages} printable pages in a {theme.lower()} theme.

What you receive:
- 1 PDF file
- {pages} pages
- High-resolution printable interiors
- Great for home, school, and gifts

Perfect for:
- Kids activities
- Classrooms
- Party printables
- Creative fun at home

This is a digital product. No physical item will be shipped.
""".strip()