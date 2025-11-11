from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class Emailform(FlaskForm):
    email = StringField('Correo electronico o telefono', [DataRequired()])

"""class Password(FlaskForm):
    Password = StringField('', [DataRequired()])"""