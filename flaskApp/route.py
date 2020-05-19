from flask import render_template, flash, redirect, url_for
from flaskApp import app 
from flaskApp.form import RegistrationForm, LoginForm
from flaskApp.models import User, Grievance


@app.route("/")
@app.route("/home")
def home():
    return render_template('layout.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "robinbond2k18@gmail.com" and form.password.data == "robin":
            flash('You have logged in successfully', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful! Please check Username and Password.', 'danger')
    return render_template('login.html', title='Login', form=form)

