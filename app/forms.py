from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Regexp

class Emailform(FlaskForm):
    email = StringField('',render_kw={"placeholder": "Correo electronico o telefono"} ,validators= [DataRequired(), Regexp(r".+@.+\.com$", message="El correo debe terminar en .com")])
    submit = SubmitField('siguiente')
    
class Passform(FlaskForm):
    password = PasswordField('', render_kw={"placeholder":"ingresa tu contraseña"}, validators= [DataRequired()])
    submit = SubmitField('siguiente')