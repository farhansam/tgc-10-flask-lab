# import
from flask import Flask
import os
import random

app = Flask(__name__)

# route
@app.route('/')
# view function
def home():
    return "Hello world"

@app.route('/about-us')
def about():
    return "<h1>About Us</h1>"

@app.route('/lucky')
def lucky_number():
    number = random.randint(1000, 9999)
    return "Your lucky number is " + str(number)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
