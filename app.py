from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_file
import os
import uuid
import time
from functools import wraps


# motor antigo
from engine.generator import generate_svg
from engine.kdp_export import export_kdp_book
from books.pipeline import generate_full_book_package

app = Flask(__name__)
app.secret_key = "coloria-secret-key"

GENERATED_FOLDER = "generated"
os.makedirs(GENERATED_FOLDER, exist_ok=True)


# ==============================
# LOGIN SIMPLES
# ==============================

USERS = {
    "admin": "admin123"
}


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        if "user" not in session:
            return redirect(url_for("login"))

        return f(*args, **kwargs)

    return decorated


# ==============================
# PÁGINAS
# ==============================

@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        user = request.form.get("user")
        password = request.form.get("password")

        if USERS.get(user) == password:

            session["user"] = user
            return redirect(url_for("index"))

        return render_template("login.html", error="Login inválido")

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()
    return redirect(url_for("login"))


# ==============================
# GERAR DESENHO SVG
# ==============================

@app.route("/api/generate", methods=["POST"])
@login_required
def generate():

    data = request.get_json()

    prompt = data.get("prompt", "")
    style = data.get("style", "modern")
    category = data.get("category", "")

    try:

        # motor novo
        svg_data = generate_svg(prompt)

        filename = f"{uuid.uuid4().hex}.svg"
        filepath = os.path.join(GENERATED_FOLDER, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_data)

        return jsonify({
            "success": True,
            "file": filename
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        })


# ==============================
# DOWNLOAD SVG
# ==============================

@app.route("/download/<filename>")
@login_required
def download(filename):

    path = os.path.join(GENERATED_FOLDER, filename)

    if not os.path.exists(path):
        return "Arquivo não encontrado", 404

    return send_file(path, as_attachment=True)


# ==============================
# GERAR LIVRO KDP
# ==============================

@app.route("/api/generate-book", methods=["POST"])
@login_required
def generate_book():

    data = request.get_json()

    pages = int(data.get("pages", 30))

    try:

        filename = export_kdp_book(pages)

        return send_file(
            filename,
            as_attachment=True,
            download_name="coloring_book_kdp.pdf"
        )

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        })


# ==============================
# LIMPAR ARQUIVOS ANTIGOS
# ==============================

def cleanup_generated():

    now = time.time()

    for f in os.listdir(GENERATED_FOLDER):

        path = os.path.join(GENERATED_FOLDER, f)

        if os.path.isfile(path):

            if now - os.path.getmtime(path) > 3600:
                os.remove(path)




@app.route('/api/generate-etsy-package', methods=['POST'])
@login_required
def generate_etsy_package():
    data = request.get_json()
    theme = data.get("theme", "Animals")
    pages = int(data.get("pages", 30))

    package = generate_full_book_package(theme=theme, pages=pages)

    return jsonify({
        "success": True,
        "title": package["title"],
        "pdf": package["pdf"],
        "cover": package["cover"],
        "zip": package["zip"],
    })


# ==============================
# START
# ==============================

if __name__ == "__main__":

    app.run(debug=True)