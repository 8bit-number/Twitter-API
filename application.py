from flask import Flask, render_template, request, redirect, url_for
from map_creator import map
from parse_tw import get_users

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/users", methods=["POST", "GET"])
def users():
    if request.method == "GET":
        return render_template("users.html")

    name = request.form.get("name")
    resp = get_users(name, 100)

    if resp:
        return render_template(map(resp, name)[-len(name+".html"):])
    else:
        return render_template("users.html", **{"error": "you entered invalid username"})

