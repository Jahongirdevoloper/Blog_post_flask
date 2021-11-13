import flask
from flask import Blueprint
from .post import post

main = Blueprint('main', __name__)


@main.route("/")
def index_page():
    return flask.redirect(flask.url_for("post.posts_page"))
