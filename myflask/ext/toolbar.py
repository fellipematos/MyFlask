from flask_debugtoolbar import DebugToolbarExtension


def init_app(app):
    if app.debug:
        app.config["SECRET_KEY"] = "myflask-corrigir"
        DebugToolbarExtension(app)
