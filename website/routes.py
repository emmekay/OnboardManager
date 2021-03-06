from flask import render_template, url_for, request, redirect, flash, Blueprint 
from blog import app, db
from blog.models import User, Post, Comment
from blog.forms import RegistrationForm, LoginForm, CommentForm
from flask_login import login_user, logout_user, login_required, current_user  
from sqlalchemy import desc, asc 

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/faq")
def sops():
    posts = Post.query.order_by(asc(Post.date)).all()
    return render_template('faq.html', posts=posts, title='Frequently Asked Questions')

@app.route("/clientportal")
def about():
    return render_template('clientportal.html', title='Client Portal')

@app.route("/workoutlibrary")
def about():
    return render_template('workoutlibrary.html', title='Workout Library')

@app.route("/myprofile")
def about():
    return render_template('myprofile.html', title='My Profile')

@app.route("/purchase")
def about():
    return render_template('purchase.html', title='Purchase')

@app.route("/mydiet")
def about():
    return render_template('mydiet.html', title='My Diet')

@app.route("/descposts")
def descposts():
    posts = Post.query.order_by(desc(Post.date)).all()
    return render_template('blogs.html', posts=posts, title='Blogs')

@app.route("/ascposts")
def ascposts():
    posts = Post.query.order_by(asc(Post.date)).all()
    return render_template('blogs.html', posts=posts, title='Blogs')

@app.route("/about")
def about():
    return render_template('about.html', title='About Me')

@app.route("/projects")
def projects():
    return render_template('projects.html', title='Projects')

@app.route("/privacy")
def privacy():
    return render_template('privacy.html', title='Privacy Policy')

@app.route("/terms")
def terms():
    return render_template('terms.html', title='Terms of Use')

@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter(Comment.post_id == post.id)
    form = CommentForm()
  
    return render_template('post.html', title=post.title, post=post, comments=comments, form=form) # removed tags = tags 

@app.route('/post/<int:post_id>/comment', methods=['GET', 'POST'])
@login_required
def post_comment(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        db.session.add(Comment(content=form.comment.data, post_id=post.id, author_id=current_user.id))
        db.session.commit()
        flash("Your comment has been added to the post.", "Success")
        return redirect(f'/post/{post.id}')
    comments = Comment.query.filter(Comment.post_id == post.id)
    return render_template('post.html', post=post, comments=comments, form=form)
           

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

            return render_template('login.html',form=form)
            
    return render_template('login.html',title='Login',form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("You have successfully logged out.  You will be redirected to the homepage.")
    return redirect(url_for('home')) 
