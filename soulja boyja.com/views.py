from urllib import request
from flask import Blueprint, render_template, jsonify

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/<username>")

def thing(username):
    return render_template("soulja.html", name=username)

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

