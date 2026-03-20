def generate_amazon_description(title: str, theme: str, pages: int = 30) -> str:
    return f"""
Discover {title}.

This delightful coloring book brings together {pages} fun and engaging pages with a charming {theme.lower()} theme designed for children.

Inside this book you will find:
- {pages} unique coloring pages
- Simple bold outlines
- Kid-friendly illustrations
- Great pages for relaxation and creativity
- A fun gift for birthdays, holidays, and everyday learning

Perfect for young artists who enjoy coloring, imagination, and playful activities.

Grab your copy today and start coloring.
""".strip()