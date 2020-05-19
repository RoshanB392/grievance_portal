from flask import Flask, render_template
from form import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SERECT_KEY'] = '30aafab764c6161f72402799774df65e'

@app.route("/")
@app.route("/home")
def home():
    return render_template('layout.html')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)