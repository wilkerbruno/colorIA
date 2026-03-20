import os
import zipfile
from books.metadata import generate_amazon_keywords
from books.descriptions import generate_amazon_description
from books.etsy_description import generate_etsy_description

def export_etsy_zip(
    output_zip: str,
    pdf_path: str,
    cover_path: str,
    title: str,
    theme: str,
    pages: int = 30
) -> str:
    temp_meta = "metadata.txt"
    temp_desc = "description.txt"
    temp_keywords = "keywords.txt"
    temp_etsy = "etsy_description.txt"

    with open(temp_meta, "w", encoding="utf-8") as f:
        f.write(title)

    with open(temp_desc, "w", encoding="utf-8") as f:
        f.write(generate_amazon_description(title, theme, pages))

    with open(temp_keywords, "w", encoding="utf-8") as f:
        f.write(", ".join(generate_amazon_keywords(theme)))

    with open(temp_etsy, "w", encoding="utf-8") as f:
        f.write(generate_etsy_description(title, theme, pages))

    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(pdf_path, arcname=os.path.basename(pdf_path))
        z.write(cover_path, arcname=os.path.basename(cover_path))
        z.write(temp_meta, arcname="metadata.txt")
        z.write(temp_desc, arcname="description.txt")
        z.write(temp_keywords, arcname="keywords.txt")
        z.write(temp_etsy, arcname="etsy_description.txt")

    for f in [temp_meta, temp_desc, temp_keywords, temp_etsy]:
        if os.path.exists(f):
            os.remove(f)

    return output_zip