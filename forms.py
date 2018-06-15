from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, BooleanField

from wtforms import validators, ValidationError
from wtforms.validators import DataRequired

class Registro(FlaskForm):
    name = TextField('Name', [validators.Required('Name required')])
    last_name = TextField('Last Name', [validators.Required('Last name required')])
    email = TextField('Email', [validators.Required('Email required'), validators.Email('Email not valid')])
    submit = SubmitField('Guardar')
