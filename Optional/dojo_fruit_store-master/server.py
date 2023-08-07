"""SERVER"""
import datetime
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    """Index route"""
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    """Checkout route""" 

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    apple_qty = request.form['apple']
    blackberry_qty = request.form['blackberry']
    raspberry_qty = request.form['raspberry']
    strawberry_qty = request.form['strawberry']

    current_date = datetime.datetime.now().strftime("%B %dth %Y %I:%M:%S %p")

    fruit_basket = [int(apple_qty), int(blackberry_qty), int(raspberry_qty), int(strawberry_qty)]
    fruit_qty = sum(fruit_basket)

    print(request.form)
    print(f"Cobrando a {first_name} {last_name} por {fruit_qty} frutas")
    return render_template("checkout.html", first_name = first_name, last_name = last_name,
                           student_id = student_id, apple = apple_qty, blackberry = blackberry_qty,
                           raspberry = raspberry_qty, strawberry = strawberry_qty,
                           current_date = current_date, fruit_qty=fruit_qty)


@app.route('/fruits')
def fruits():
    """Fruits route"""
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)
    