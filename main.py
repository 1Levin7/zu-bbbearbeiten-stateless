import helper
from flask import Flask, request, Response, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    todos = helper.todos
    return render_template('index.html', todos=todos)


@app.route('/create/')
def add():
    title = request.args.get("title")
    print(title)
    helper.add(title)
    return redirect(url_for("index"))


@app.route('/update/<int:index>')
def update(index):
    helper.update(index)
    return redirect(url_for("index"))

@app.route('/secret')
def secret():
    return 42