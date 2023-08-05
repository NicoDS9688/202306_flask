"""Server"""
from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/lists')
def users_list():
    """Método que renderiza la lista de estudiantes"""
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("index.html", users = users)

if __name__=="__main__":
    app.run(debug=True)
