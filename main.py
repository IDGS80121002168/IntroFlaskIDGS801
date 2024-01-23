from flask import Flask, render_template

app = Flask (__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

@app.route("/alumnos")
def alumnos():
    titulo="UTL!!!!"
    nombres=["cristian", "mario", "pedro", "dario"]
    return render_template("alumnos.html", titulo=titulo, nombres=nombres)

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




if __name__ =="__main__":
    app.run(debug=True)