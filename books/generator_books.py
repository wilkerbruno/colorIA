import random
import os
from engine.generator import generate_svg
from engine.kdp_export import export_kdp_book
from books.prompts import BOOK_TOPICS


OUTPUT_DIR="output/books"

os.makedirs(OUTPUT_DIR,exist_ok=True)


def generate_book(topic,pages=30):

    prompts = BOOK_TOPICS[topic]

    filename=f"{topic}_{random.randint(1000,9999)}.pdf"

    export_kdp_book(pages)

    return filename


def generate_many_books(qty=10):

    books=[]

    for i in range(qty):

        topic=random.choice(list(BOOK_TOPICS.keys()))

        book=generate_book(topic)

        books.append(book)

    return books