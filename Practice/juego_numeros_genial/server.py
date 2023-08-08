"""SERVER"""
import random
from flask import Flask, render_template, session, redirect, request


app = Flask(__name__, static_folder='static')
app.secret_key = "keep it secret, keep it safe"


def random_num():
    """Retorna un numero random"""
    return random.randint(1, 100)

@app.route("/")
def game():
    """Devuelve html base"""
    if "num" not in session:
        session["num"] = random_num()
    print(session["num"])
    return render_template("game.html")

@app.route("/number/", methods=["POST"])
def check_number():
    """Chequea el numero"""
    guess = int(request.form.get("number"))
    num_to_guess = session["num"]

    if guess > num_to_guess:
        response = "Too High!"
        square_color = "bg-warning"
    elif guess < num_to_guess:
        response = "Too Low!"
        square_color = "bg-danger"
    else:
        response = str(num_to_guess) + " era el número!"
        square_color = "bg-success"

    return render_template("game.html", response=response, square_color=square_color)

@app.route("/reset/", methods=["GET"])
def reset_number():
    """Metodo que resetea el numero"""
    session.pop("num", None)
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
