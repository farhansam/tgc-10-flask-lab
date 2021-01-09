from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.template.html')


@app.route('/say-hi')
def greetings():
    firstname = "Ah Kow"
    lastname = "Tan"
    today = datetime.now()
    return render_template('greetings.template.html', 
                            fname=firstname, 
                            lname=lastname,
                            today_date=today)

@app.route('/wish/<username>')
def wish_happy_new_year(username):
    return username


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host='localhost',
            port=8080,
            debug=True)
