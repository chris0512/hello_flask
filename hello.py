from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/bye')
def say_bye():
    return "bye"


if __name__ == "__main__":
    app.run()