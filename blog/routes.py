from flask import render_template, url_for, request, redirect, flash 
from blog import app, db
from blog.models import User, Post
from blog.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user 

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
    if form.validate_on_submit():
        user = User(username=form.username.data, firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            flash("Login Successful!")
            return redirect(url_for('home'))
        else:
            flash("Email or password is incorrect. Please try again.")
    return render_template('login.html',title='Login',form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("You have successfully logged out.  You will be redirected to the homepage.")
    return redirect(url_for('home')) 
