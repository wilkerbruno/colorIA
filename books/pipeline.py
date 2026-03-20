import os
from books.metadata import generate_amazon_title
from books.covers import generate_cover_svg
from books.zip_export import export_etsy_zip
from engine.kdp_export import export_kdp_book

def generate_full_book_package(theme: str = "Animals", pages: int = 30) -> dict:
    title = generate_amazon_title(theme)

    pdf_path = export_kdp_book(pages)

    cover_svg = generate_cover_svg(title=title, subtitle=f"{pages} fun pages")
    cover_path = "cover.svg"
    with open(cover_path, "w", encoding="utf-8") as f:
        f.write(cover_svg)

    zip_path = "etsy_package.zip"
    export_etsy_zip(
        output_zip=zip_path,
        pdf_path=pdf_path,
        cover_path=cover_path,
        title=title,
        theme=theme,
        pages=pages,
    )

    return {
        "title": title,
        "pdf": pdf_path,
        "cover": cover_path,
        "zip": zip_path,
    }