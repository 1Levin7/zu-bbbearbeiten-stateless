from flask import Flask, request, redirect, url_for, render_template
import helper
from flask import Response 

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


@app.route("/download")
def get_csv():
    return Response(
        helper.get_csv(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=zu-bbbearbeiten.csv"},
    )
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
