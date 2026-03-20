import random

MAIN_KEYWORDS = [
    "Coloring Book for Kids",
    "Cute Animals Coloring Book",
    "Toddlers Coloring Book",
    "Unicorn Coloring Book for Girls",
    "Boys Activity Coloring Book",
]

BENEFITS = [
    "Easy Designs",
    "Fun and Relaxing",
    "Big Simple Pages",
    "Ages 4-8",
    "For Beginners",
]

THEMES = [
    "Animals",
    "Fantasy",
    "Adventure",
    "Nature",
    "Happy Kids",
]

def generate_amazon_title(theme: str = "Animals") -> str:
    base = random.choice(MAIN_KEYWORDS)
    benefit = random.choice(BENEFITS)
    return f"{base}: {theme} with {benefit}"

def generate_amazon_keywords(theme: str = "animals") -> list[str]:
    return [
        f"{theme} coloring book",
        "kids coloring book",
        "easy coloring pages",
        "activity book for kids",
        "cute coloring book",
        "gift for children",
        "preschool coloring",
    ]