from flask import Flask
import os

web = Flask(__name__)

# route
@web.route('/')
# view function
def home():
    return "This is the home page"

@web.route('/bmi')
def bmi():
    weight = float(input("Enter weight in kg:"))
    height = float(input("Enter height in metres:"))
    bmi = weight / (height * height)
    print("Your BMI is:", bmi)

    if bmi < 18.5:
        print("Underweight")
    elif bmi <= 24.9:
        print("Normal Weight")
    elif bmi <= 29.9:
        print("Overweight")
    else:
        print("Obese")

    return str(bmi)


# "magic code" -- boilerplate
if __name__ == '__main__':
    web.run(host='localhost',
            port=8080,
            debug=True)