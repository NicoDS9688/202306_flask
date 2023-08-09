"""Server"""
from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def users_list():
    """Método que renderiza la lista de estudiantes"""


if __name__=="__main__":
    app.run(debug=True)
