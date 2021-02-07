from flask import render_template, url_for
from blog import app
from blog.models import User, Post

@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About Me')


@app.route("/cv")
def cv():
    return render_template('cv.html', title='My Work Experience')

