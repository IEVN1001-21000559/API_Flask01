from flask import Flask, render_template, request
import math                                 
 
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




 
@app.route("/distancia")
def distancia ():
    return render_template('distancia.html')


@app.route('/distancia', methods=['POST'])
def calcular_distancia():
    
        x1 = float(request.form.get('x1'))
        y1 = float(request.form.get('y1'))
        x2 = float(request.form.get('x2'))
        y2 = float(request.form.get('y2'))
        
     
        delta_x = x2 - x1
        delta_y = y2 - y1
        
        # Calcular la distancia
        distancia = math.sqrt((delta_x ** 2) + (delta_y ** 2))
        
        # Redondear a dos decimales
        resultado_final = round(distancia, 2)
        
        return render_template('distancia.html', distancia = distancia),f"<h1>La distancia entre el punto ({x1}, {y1}) y el punto ({x2}, {y2}) es {resultado_final}</h1>"
    

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


 
if __name__ == '__main__':
    app.run(debug=True)