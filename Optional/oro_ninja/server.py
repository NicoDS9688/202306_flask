"""SERVER"""
import random
import datetime
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__, static_folder='static')
app.secret_key = "keep it secret, keep it safe"

@app.route("/")
def index():
    """Metodo que devuelve index.html"""
    if "gold" not in session:
        session["gold"] = 0
    print(session["gold"])

    if "activities" not in session:
        session["activities"] = [" "]

    if "moves" not in session:
        session["moves"] = 0

    return render_template("index.html")

@app.route("/process_money/", methods=["POST"])
def earn_gold():
    """Metodo que realiza las condicionales"""

    building = request.form["building"]
    print("building")


    time = datetime.datetime.now()

    if building == "farm":
        value = random.randint(10,20)
        session["gold"] += value
        session["moves"] += 1

        session["activities"].insert(0, f"<div style='color: green'>Earned {value} golds from the \
                                     farm! ({time:%Y/%m/%d}  {time:%H:%M})</div>")

    elif building == "cave":
        value = random.randint(5,10)
        session["gold"] += value
        session["moves"] += 1

        session["activities"].insert(0, f"<div style='color: green'>Earned {value} golds from the \
                                     cave! ({time:%Y/%m/%d}  {time:%H:%M})</div>")

    elif building == "house":
        value = random.randint(2,5)
        session["gold"] += value
        session["moves"] += 1

        session["activities"].insert(0, f"<div style='color: green'>Earned {value} golds from the \
                                     house! ({time:%Y/%m/%d}  {time:%H:%M})</div>")

    elif building == "casino":
        stake = random.randint(0, 100)

        if stake >= 50:
            value = random.randint(0,50)
            session["gold"] += value
            session["moves"] += 1

            session["activities"].insert(0, f"<div style='color: green'>Entered a casino and won \
                                         {value} gold! YAY! ({time:%Y/%m/%d}  {time:%H:%M})</div>")

        else:
            value = random.randint(0,50)
            session["gold"] -= value
            session["moves"] += 1

            session["activities"].insert(0, f"<div style='color: red'>Entered a casino and lost \
                                         {value}, gold.. Ouch!({time:%Y/%m/%d} {time:%H:%M})</div>")

    if session["gold"] >= 100 and session["moves"] <= 15:
        session["game_result"] = "win"
        session["activities"].insert(0, "<div style='color: red'>YOU WON!</div>")

    elif session["moves"] > 15:
        session["game_result"] = "lose"
        session["activities"].insert(0, "<div style='color: red'>YOU LOOSE!</div>")

    return redirect("/")


@app.route("/restart/")
def restart():
    """Metodo que resetea la sesion"""

    session.clear()

    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
