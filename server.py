from flask import Flask
import random

random_num = random.randint(0,9)
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align:center;">Guess a number between 0 and 9</h1>' \
           '<img style="display:block;margin:0 auto;" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def greet(number):
    if number > random_num:
        return f'<p style=text-align:center;font-size:22px;color:red;>{number} is too high, try again! </p>' \
               '<img style="display:block; margin:0 auto" src="https://media.giphy.com/media/3o7abAHdYvZdBNnGZq/giphy.gif">'

    elif number < random_num:
        return f'<p style=text-align:center;font-size:22px;color:#F1CAFF>{number} is too low, try again! </p>' \
               '<img style="display:block; margin:0 auto;" src="https://media.giphy.com/media/fqst7AVqF6AVLlYklE/giphy.gif">'

    else:
        return '<p style=text-align:center;font-size:22px;>You god damn right! </p>' \
               '<img style="display:block; margin:0 auto;color:green" src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'


app.run(debug=True)

