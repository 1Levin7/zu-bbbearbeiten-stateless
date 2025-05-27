from flask import Flask, request, redirect, url_for, render_template, Response
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from database import db
import helper

# 🔐 .env einlesen
load_dotenv()

# 🌐 Flask App erstellen
app = Flask(__name__)

# 🔌 DB-Verbindung konfigurieren (PostgreSQL)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}".format(
    dbuser=os.environ["DBUSER"],
    dbpass=os.environ["DBPASS"],
    dbhost=os.environ["DBHOST"],
    dbname=os.environ["DBNAME"]
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 📦 Datenbank initialisieren
db.init_app(app)
with app.app_context():
    db.create_all()

# ✅ Routen
@app.route("/")
def index():
    todos = helper.get_all()
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    helper.add(title)
    return redirect(url_for("index"))

@app.route("/update/<int:index>")
def update(index):
    helper.update(index)
    return redirect(url_for("index"))

@app.route("/secret")
def secret():
    return "42"

@app.route("/download")
def get_csv():
    return Response(
        helper.get_csv(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=zu-bbbearbeiten.csv"},
    )

# ▶️ Start der App
if __name__ == "__main__":
    app.run(host="0.0.0.0")
