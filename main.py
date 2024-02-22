from flask import Flask, render_template,request
from flask import flash
from flask_wtf.csrf import CSRFProtect
import forms 

app = Flask (__name__)
app.secret_key = 'Esta es mi clave secreta'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.before_request
def before_request():
    print("before 1")
    

@app.after_request
def after_request(response):
    print("after 1")
    return response

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/alumnos", methods= ['GET','POST'])
def alumnos():
    print("Alumno: {}".format(g.nombre))
    nombre=""
    apaterno=""
    amaterno=""
    alumno_clase= forms.UserForm(request.form)
    if request.method == 'POST' and alumno_clase.validate():
        nombre=alumno_clase.nombre.data
        apaterno=alumno_clase.apaterno.data
        amaterno=alumno_clase.amaterno.data

        print('Nombre: {}', format(nombre))
        print('apaterno: {}', format(apaterno))
        print('amaterno: {}', format(amaterno))
       
        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)
         
    return render_template("alumnos.html",form=alumno_clase, nombre=nombre, apaterno=apaterno, amaterno=amaterno)

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")


@app.route("/hola")
def hola():
    return "<h1>Salidos desde Holaaa</h1>"

@app.route("/saludos")
def saludo():
    return "<h1>Salidos desde Saludo</h1>"

@app.route("/nombre/<string:nombre>")
def nombre(nombre):
    return "Hola: "+nombre

@app.route("/numero/<string:numero>")
def numero(numero):
    return "Este es el numero:  " + str(numero)

@app.route("/user/<string:id>/<string:nom>")
def user(id,nom):
    return "Bienvenido Usuario" + nom + " " + id

@app.route("/suma/<string:num1>/<string:num2>")
def suma(num1,num2):
    total = int(num1) + int(num2)
    return "La suma de" + str(num1) + " " + str(num2) + " es igual a: " + str(total) 

@app.route("/calcular",methods=["GET","POST"])
def calcular():

    if request.method=="POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La multiplicacion de {} x {} = {}".format(num1,num2,str(int(num1) * int(num2)))
    else:
        return '''
        <form action = "/calcular", method ="POST">
        <label>Numero 1:</label>
        <input type="text" name="n1"><br>
        <label>Numero 2:</label>
        <input type="text" name="n2"><br>
        <input type="submit "/>
        </form>
            '''
    
@app.route("/operaBas")
def operaBas():
    return render_template("operaBas.html")

@app.route("/resultado",methods=["GET","POST"])
def resultado():
    if request.method=="POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La multiplicacion de {} x {} = {}".format(num1,num2,str(int(num1) * int(num2)))


if __name__ =="__main__":
    app.run(debug=True)