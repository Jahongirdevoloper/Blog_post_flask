from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
db = SQLAlchemy()
ckeditor = CKEditor()

def process_app():
    app = Flask(__name__)

    from .routers import post, main
    app.register_blueprint(post)
    app.register_blueprint(main)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'HELLO_WORLD'
    db.init_app(app)
    create_table(app)
    return app


def create_table(app):
    db.create_all(app=app)
