from flask import render_template, request, Blueprint
from flaskApp.models import User, Grievance


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    grievances = Grievance.query.order_by(Grievance.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('home.html', grievances=grievances)

@main.route("/about")
def about():
    return render_template('about.html', title='About')
