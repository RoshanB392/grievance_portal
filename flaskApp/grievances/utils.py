import os
import secrets
from flaskApp import app


def save_grievance_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/grievance_pic', picture_fn)
    form_picture.save(picture_path)
    
    return picture_fn

