"""Comprender el enrutamiento"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hola_mundo():
    """Funcion que devuelve hola mundo"""
    return 'Hola Mundo!'

@app.route('/dojo')
def dojo():
    """Funcion que devuelve Dojo!"""
    return 'Dojo!'

@app.route('/say/<name>')
def hello_name(name):
    """Funcion que devuelve Hola + un nombre"""
    return 'Hola, ' + name

@app.route('/repeat/<int:n>/<string:word>')
def repeat(n, word):
    """Funcion que repite la palabra ingresada un numero n de veces"""
    return f'{n * word}'

@app.errorhandler(404)
def page_not_found(error):
    """Funcion que devulve un mensaje al utilizar de manera incorrecta la ruta"""
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404

if __name__=="__main__":
    app.run(debug=True)
