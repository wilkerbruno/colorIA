from reportlab.pdfgen import canvas
from engine.generator import generate_svg
import cairosvg
import os

def export_kdp_book(pages=30):

    filename="coloring_book_kdp.pdf"

    pdf=canvas.Canvas(filename)

    for i in range(pages):

        svg=generate_svg()

        png_file=f"page_{i}.png"

        cairosvg.svg2png(bytestring=svg.encode(),write_to=png_file)

        pdf.drawImage(png_file,0,0,width=600,height=600)

        pdf.showPage()

    pdf.save()

    return filename