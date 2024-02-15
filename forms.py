from wtforms import Form
from wtforms import StringField,TelField,IntegerField
from flask_wtf import FlaskForm
from wtforms import EmailField
from wtforms import validators


class UserForm(Form):
    nombre= StringField('nombre', [
        validators.DataRequired(menssage='El campo es requerido'),
        validators.length(min=4, max=10, menssage='Ingresa nombre valido')
        ])
    apaterno= StringField('apaterno', [
        validators.DataRequired(menssage='El campo es requerido'),
        validators.length(min=4, max=10, menssage='Ingresa apellido parterno valido')
        ])
    amaterno= StringField('amaterno', [
        validators.DataRequired(menssage='El campo es requerido'),
        validators.length(min=4, max=10, menssage='Ingresa apellido materno valido')
        ])

    email= EmailField('email', [validators.Email(menssage='Ingrese correo valido')])
    edad= StringField('edad', [
        validators.DataRequired(menssage='El campo es requerido'),
        validators.length(min=1, max=10, menssage='Ingresa edad valido')
        ])


class archivoTexto(Form):
    ingles= StringField('ingles', [
        validators.DataRequired(menssage='El campo es requerido'),
        validators.length(min=1, max=1000, menssage='Ingresa palabra en ingles valido')
        ])
    espaniol= StringField('espaniol', [
        validators.DataRequired(menssage='El español es requerido'),
        validators.length(min=1, max=1000, menssage='Ingresa plabra en español valido')
        ])
    
class leer(Form):
    ingles= StringField('ingles', [
        validators.DataRequired(menssage='El campo es requerido'),
        validators.length(min=1, max=1000, menssage='Ingresa palabra en ingles valido')
        ])
    espaniol= StringField('espaniol', [
        validators.DataRequired(menssage='El español es requerido'),
        validators.length(min=1, max=1000, menssage='Ingresa plabra en español valido')
        ])
    palabra= StringField('palabra', [
        validators.DataRequired(menssage='la palabra es requerido'),
        validators.length(min=1, max=1000, menssage='Ingresa plabra valida')
        ])