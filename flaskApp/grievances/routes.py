from flask import render_template, flash, redirect, url_for, request, abort, Blueprint
from flaskApp.models import Grievance
from flaskApp import app, bcrypt , db
from flaskApp.grievances.forms import PostGrievanceForm
from flaskApp.grievances.utils import save_grievance_picture
from flask_login import current_user, login_required


grievances = Blueprint('grievances', __name__)



@grievances.route("/grievance/new", methods=['GET', 'POST'])
@login_required
def new_grievance():
    form = PostGrievanceForm()
    if form.validate_on_submit():
        if form.grievance_picture.data:
            grievance_picture_file = save_grievance_picture(form.grievance_picture.data) 
            current_user.grievance_image_file = grievance_picture_file
        grievance = Grievance(category_grievance=form.category_grievance.data, title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(grievance)
        db.session.commit()
        flash('Your Grievance has been Sumbitted', 'success')
        grievance_image_file = url_for('static', filename='grievance_pic/' + current_user.grievance_image_file)
        return redirect(url_for('main.home'))
    return render_template('create_grievance.html', title='New Grievance', legend='New Grievance', form=form)


@grievances.route("/grievance/<int:grievance_id>")
def grievance(grievance_id):
    grievance = Grievance.query.get_or_404(grievance_id)
    return render_template('grievance.html', title=grievance.title, grievance=grievance)


@grievances.route("/grievance/<int:grievance_id>/update", methods=['GET', 'POST'])
def grievance_update(grievance_id):
    grievance = Grievance.query.get_or_404(grievance_id)
    if grievance.author != current_user:
        abort(403)
    form = PostGrievanceForm()
    if form.validate_on_submit():
        if form.grievance_picture.data:
            grievance_picture_file = save_grievance_picture(form.grievance_picture.data) 
            current_user.grievance_image_file = grievance_picture_file
        grievance.category_grievance = form.category_grievance.data
        grievance.title = form.title.data
        grievance.content = form.content.data
        db.session.commit()
        flash('Your Grievance has been updated!', 'success')
        grievance_image_file = url_for('static', filename='grievance_pic/' + current_user.grievance_image_file)
        return redirect(url_for('grievances.grievance', grievance_id=grievance.id))
    elif request.method == 'GET':
        form.category_grievance.data = grievance.category_grievance
        form.title.data = grievance.title
        form.content.data = grievance.content
    return render_template('create_grievance.html', title='Update Grievance', legend='Update Grievance', form=form)



@grievances.route("/grievance/<int:grievance_id>/delete", methods=['POST'])
def grievance_delete(grievance_id):
    grievance = Grievance.query.get_or_404(grievance_id)
    if grievance.author != current_user:
        abort(403)
    db.session.delete(grievance)
    db.session.commit()
    flash('Your Grievance has been deleted!', 'success')
    return redirect(url_for('main.home'))


