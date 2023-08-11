"""Server"""
from flask import Flask, render_template, session, request

app = Flask(__name__, static_folder='static')
app.secret_key = "keep it secret, keep it safe"

@app.route("/")
def base():
    """Método que devuelve el template index"""
    return render_template("form.html")

@app.route('/process/', methods=['POST'])
def process():
    """Método para guardar los datos en cache"""
    session['name'] = request.form.get('name')
    session['location'] = request.form.get('location')
    session['language'] = request.form.get('language')
    session['comments'] = request.form.get('comments')

    print(request.form)
    return render_template('result.html')


if __name__=="__main__":
    app.run(debug=True)
