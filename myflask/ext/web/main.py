from flask import Blueprint, current_app, render_template, url_for


bp = Blueprint("web", __name__)

@bp.route("/")
def index():
    return render_template("index.html")
    