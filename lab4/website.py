from flask import Flask, render_template, request, redirect, url_for
import os

web = Flask(__name__)

# route
@web.route('/')
# view function
def home():
    return "This is the home page"

@web.route('/bmi/<height>/<weight>')
def bmi(height, weight):
    weight = float(weight)
    height = float(height)
    bmi = weight / (height * height)

    if bmi < 18.5:
        weight_cat = "Underweight"
    elif bmi <= 24.9:
        weight_cat = "Acceptable weight"
    elif bmi <= 29.9:
        weight_cat = "Overweight"
    else:
        weight_cat = "Obese"

    return render_template('website.html',
                            height=height,
                            weight=weight,
                            bmi=bmi,
                            weight_cat=weight_cat)


# "magic code" -- boilerplate
if __name__ == '__main__':
    web.run(host='localhost',
            port=8080,
            debug=True)