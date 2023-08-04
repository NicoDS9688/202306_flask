"""Server"""
from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def chess_16():
    """Método que devuelve el template con el tablero de ajedrez 8x8"""

    rows = 8
    cols = 8
    color1 = 'red'
    color2 = 'black'
    return render_template('index.html', rows=rows, cols=cols, color1=color1, color2=color2)

@app.route('/<int:cols>')
def chess_12(cols):
    """Método que devuelve el template con el tablero de ajedrez 8 por el numero que se ingrese"""

    rows = 8
    color1 = 'red'
    color2 = 'black'
    return render_template('index.html', rows=rows, cols=cols, color1=color1, color2=color2)

@app.route('/<int:rows>/<int:cols>')
def chess_x_y(rows, cols):
    """Método que devuelve el template con el tablero de ajedrez filas por columnas 
    que se ingrese"""

    color1 = 'red'
    color2 = 'black'
    return render_template('index.html', rows=rows, cols=cols, color1=color1, color2=color2)

@app.route('/<int:rows>/<int:cols>/<string:color1>/<string:color2>')
def chess_x_y_colors(rows, cols, color1, color2):
    """Método que devuelve el template con el tablero de ajedrez filas por columnas 
    y dos colores ingresados"""

    return render_template('index.html', rows=rows, cols=cols, color1=color1, color2=color2)


if __name__=="__main__":
    app.run(debug=True)
