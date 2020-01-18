from flask import render_template

from app.main import main


@main.route("/")
@main.route("/<path:path>")
def home(path=None):
    """
    Catch all home view used to render the react code. This is rendered server side to allow
    for other configurations such as csrf tokens, etc.
    :param path: the optional path to react view
    :return: the rendered template
    """
    return render_template('index.html')
