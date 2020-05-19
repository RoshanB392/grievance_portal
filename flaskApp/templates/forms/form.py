from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitFiled
from wtforms.validators import DataRequired, Length, Email, EqualTo

# Registration Form
class RegistrationForm(FlaskForm):
    username = StringField('Username',
     validators=[DataRequired(), length(min=5, max=20)])

    email = StringField('Email',
     validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password', 
     validators=[DataRequired(), EqualTo('password')])

    submit = SubmitFiled('Sign Up')

# Login Form
class LoginForm(FlaskForm):
    email = StringField('Email',
     validators=[DataRequired(), Email()])

    password = PasswordField('Password', 
     validators=[DataRequired()])
    
    remember = BooleanFiled('Remember Me')

    submit = SubmitFiled('Login')