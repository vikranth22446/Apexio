from flask import render_template, request, jsonify

from app.main import main
from app.models import Rules
from app import db


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


@main.route("/create_rule", mode=["POST"])
def create_rule():
    """
    Catch all home view used to render the react code. This is rendered server side to allow
    for other configurations such as csrf tokens, etc.
    :return: the rendered template
    """
    # - Has
    # - equals
    # - Begins with
    # - Extension
    # - Regex
    # - Delete
    # - Move to

    data = request.get_json()
    has = data.get("has", "")
    equals = data.get("equals", "")
    begins_with = data.get("begins_with", "")
    extension = data.get("extension", "")
    regex = data.get("regex", "")
    delete_after = data.get("delete")
    move_to = data.get("move_to", "")

    rule = Rules(has=has, equals=equals, begins_with=begins_with, extension=extension, regex=regex,
                 delete_file=delete_after, move_to=move_to)
    db.session.add(rule)
    db.session.commit()
    return jsonify({"status": 200}), 200


@main.route("/get_all_rules", mode=["POST"])
def get_all_rules():
    """
    Catch all home view used to render the react code. This is rendered server side to allow
    for other configurations such as csrf tokens, etc.
    :return: the rendered template
    """
    # - Has
    # - Is
    # - Begins with
    # - Extension
    # - Regex
    # - Delete After
    # - Move to

    rules = Rules.query.all()
    rules_dic = []
    for rule in rules:
        data = rule.get_json()
        rules_dic.append(data)

    # data = request.get_json()
    # rule_type = data.get("RuleType", "")
    # content = data.get("Content")
    # rule = Rules(rule_type=rule_type, content=content)
    # db.session.add(rule)
    # db.session.commit()
    # return jsonify({"status": 200}), 200
    return jsonify({"rules": rules_dic})

