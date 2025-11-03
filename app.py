from flask import Flask, render_template, request
import math                                 
import forms 

app = Flask(__name__)
 
@app.route('/')
def home ():
    return "Hello, world!"
 
@app.route("/hola")
def func ():
    return "<h1>!Hola,</h1>"
 
@app.route("/user/<string:user>")
def user(user):
    return "<h1>!Hola, {}</h1>".format(user)
 
@app.route("/square/<int:num>")
def square(num):
    return "<h1>The square or, {} is {}.</h1>".format(num, num**2)
 
 
@app.route("/repeat/<string:text>/<int:times>")
def repeat(text,times):
    return "<h1>" + " ".join([text] * times) + "</h1>"
 
 
@app.route("/suam/<float:a>/<float:b>")
def suam(a, b):
    return "<h1>The sum of {} and {} is {}.</h1>".format(a, b, a + b)
 
@app.route("/index")
def index ():
    titulo="IEVN1001"
    listado=["Python","Flask","HTML","CSS","JavaScript"]
    return render_template('index.html', titulo=titulo, listado=listado)
 
@app.route("/aporb")
def apor ():
    return render_template('aporb.html')



@app.route("/resultado",methods=['POST'])
def resultado():
    n1=request.form.get("a")
    n2=request.form.get("b")
    return "La multiplicacion de {} y {} es {}".format(n1,n2,int(n1)*int(n2)) 





    

@app.route("/distancia",methods=['GET', 'POST'])
def distanciaForms():
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    dist = 0
    dist_cls = forms.Distancia(request.form)
    if request.method == 'POST' and dist_cls.validate():
        x1 = dist_cls.x1.data
        y1 = dist_cls.y1.data
        x2 = dist_cls.x2.data
        y2 = dist_cls.y2.data
        dist = math.sqrt((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2)
    return render_template('distancia.html',
                           form = dist_cls, x1 = x1, y1 = y1, x2 = x2, y2 = y2, dist =dist)




@app.route("/figuras", methods=['GET', 'POST'])
def figuras():
    #return render_template('figuras.html')

    area = None
    figura_seleccionada = None
    
    if request.method == 'POST':
        
        figura_seleccionada = request.form.get('figura')
        
        if figura_seleccionada == 'rectangulo':
            base = float(request.form.get('base'))
            altura = float(request.form.get('altura'))
            area = base * altura
        
        elif figura_seleccionada == 'triangulo':
            base = float(request.form.get('base'))
            altura = float(request.form.get('altura'))
            area = 0.5 * base * altura
        
        elif figura_seleccionada == 'circulo':
            radio = float(request.form.get('radio'))
            area = math.pi * (radio ** 2)
            area = round(area, 2) 
        
        elif figura_seleccionada == 'pentagono':
            lado = float(request.form.get('lado'))
            apotema = float(request.form.get('altura')) 
            perimetro = 5 * lado
            area = (perimetro * apotema) / 2

    return render_template('figuras.html', area=area, figura=figura_seleccionada)


@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
        math=0
        nom=''
        apell=''
        email=''
        alumno_clas=forms.UserForm(request.form)
        if request.method=='POST'  and alumno_clas.validate():
            math=alumno_clas.matricula.data
            nom=alumno_clas.nombre.data
            apell=alumno_clas.apellido.data
            email=alumno_clas.email.data
        return render_template('Alumnos.html', form=alumno_clas, math=math, nom=nom, apell=apell, email=email)
    


 
if __name__ == '__main__':
    app.run(debug=True)