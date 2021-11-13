import flask
from flask import request, redirect, url_for, render_template

from root import db
from root.database import Post
from root.forms import PostCreate
from root.utils import UPLOAD_PATH, join_path
from root.utils import new_name

post = flask.Blueprint('post', __name__, url_prefix="/posts")


@post.route("/", methods=['GET'])
def posts_page():
    posts = Post.query.all()
    return flask.render_template("post/list.html", posts=posts)


@post.route('/add', methods=['GET', 'POST'])
def post_save():
    form = PostCreate()
    if request.method == 'POST':
        if form.validate_on_submit():
            picture = form.picture.data
            path = new_name(picture.filename)
            picture.save(join_path(UPLOAD_PATH, path))
            Post(title=form.title.data, body=form.body.data, pic=path)
            flask.flash('Successfully saved', category='info')
            return redirect(url_for('post.posts_page'))
        else:
            flask.flash('Form Not Valid', category='error')
            return render_template('post/add.html')

    return render_template('post/add.html', form=form)


@post.route('/<int:pk>', methods=['GET'])
def post_get(pk):
    post = Post.query.get(pk)
    return render_template('post/get.html', post=post)


@post.route('/delete/<int:pk>', methods=['GET', 'POST'])
def post_delete(pk):
    if request.method == 'POST':
        post = Post.query.get(pk)
        post.delete()
        return redirect(url_for('post.posts_page'))
    post = Post.query.get(pk)
    return render_template('post/delete.html', post=post)
