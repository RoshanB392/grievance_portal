from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm, LoginForm
from models imoport User, Grievance

app = Flask(__name__)
app.config['SECRET_KEY'] = '30aafab764c6161f72402799774df65e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template('layout.html')


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


if __name__ == "__main__":
    app.run(debug=True)