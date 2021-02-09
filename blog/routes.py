from flask import render_template, url_for, request, redirect 
from blog import app, db
from blog.models import User, Post
from blog.forms import RegistrationForm 

@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About Me')

@app.route("/thankyou")
def thankyou():
    return render_template('thankyou.html', title='Thank You!')

@app.route("/cv")
def cv():
    return render_template('cv.html', title='My Work Experience')

@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('thankyou'))
    return render_template('register.html', title='Register', form=form)
