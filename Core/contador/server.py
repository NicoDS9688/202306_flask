"""SERVER"""
from flask import Flask, render_template, redirect, session, url_for
app = Flask(__name__, static_folder='static')
app.secret_key = "keep it secret, keep it safe"

@app.route("/")
def count():
    """Metodo que cuenta las visitas"""
    session['counter'] = session.get('counter', 0 ) + 1

    return render_template("index.html", counter = session["counter"])

@app.route("/destroy_session")
def destroy():
    """Metodo que elimina las visitas"""
    session['counter'] = 0
    return redirect(url_for('count'))

@app.route("/plus")
def plus():
    """Metodo que suma 2 visitas"""
    session['counter'] = session.get('counter', 0 ) + 1
    return redirect(url_for('count'))

if __name__=="__main__":
    app.run(debug=True)
