from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flaskApp.models import Grievance





class PostGrievanceForm(FlaskForm):
    category_grievance = StringField('Grievance Category', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    grievance_picture = FileField('Uplaod Image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Post')
