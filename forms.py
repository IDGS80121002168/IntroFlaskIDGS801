from wtforms import form
from wtforms import StringField, TelField

class UserForm(Form):
    nombre=StringField('nombre')
    email=StringField('email')
    apaterno=TelField('apaterno')