from wtforms import EmailField, Form
from wtforms import StringField, IntegerField, BooleanField, PasswordField

from wtforms import validators

class UserForm(Form):
    
    matricula=IntegerField('Matricula', [validators.DataRequired()])
    
    
    nombre=StringField('Nombre', [
        validators.DataRequired(),
        validators.Length(min=1, max=50)
    ])
    
    
    apellido=StringField('Apellido', [
        validators.DataRequired(),
        validators.Length(min=1, max=50)
    ])
    
    email=EmailField('Correo',[
        validators.Email(message='Ingrese un correo válido')
    ])

class Distancia(Form):
    x1 = IntegerField('x1', [validators.DataRequired(message='Ingrese un numero valido')])
    y1 = IntegerField('y1', [validators.DataRequired(message='Ingrese un numero valido')])
    x2 = IntegerField('x2', [validators.DataRequired(message='Ingrese un numero valido')])
    y2 = IntegerField('y2', [validators.DataRequired(message='Ingrese un numero valido')])