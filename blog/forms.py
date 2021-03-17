from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp, InputRequired  
from blog.models import User 

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
    firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=30)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Regexp('^.{6,8}$', message='Your password should be between 6 and 8 characters long.')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords do not match.')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None: 
            raise ValidationError('Username already exists. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email address is already associated with an account. Please check your email again, and login if you already have an account.')
        
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_login = BooleanField('Remember Me')
    submit = SubmitField('Login')

class CommentForm(FlaskForm):
    comment = StringField('Comment',validators=[InputRequired()])
    submit = SubmitField('Post Comment')


class TagForm(FlaskForm):
    tag = StringField('Tag', validators=[InputRequired()])
    submit = SubmitField('Post Tags')
