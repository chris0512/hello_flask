from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/bye')
def say_bye():
    return "bye"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name} you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
