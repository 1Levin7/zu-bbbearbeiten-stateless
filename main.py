from flask import Flask, request, redirect, url_for, render_template
import helper

app = Flask(__name__)

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
