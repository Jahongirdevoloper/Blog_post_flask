import wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField


class PostCreate(FlaskForm):
    title = StringField('name', validators=None)
    picture = FileField('picture', validators=None)
    body = TextAreaField('name', validators=None)
