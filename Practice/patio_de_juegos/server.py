"""Server"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play_page():
    """Método que devuelve el template play"""
    return render_template('play.html')

@app.route('/play/<int:num>')
def play_page_num(num):
    """Método que devuelve el template play 2, que devuelve la cantidad de cuadrados ingresados"""
    return render_template('play2.html', num = num)

@app.route('/play/<int:num>/<color>')
def play_page_num_color(num, color):
    """Método que devuelve el template play 2, que devuelve la cantidad y color de 
    cuadrados ingresados"""
    return render_template('play3.html', num = num, color = color)

if __name__=="__main__":
    app.run(debug=True)
