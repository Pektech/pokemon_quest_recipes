from flask import Flask
from flask_ask import Ask, statement, question, session
from flask import render_template



app = Flask(__name__)
ask = Ask(app, '/pokemon_quest')


@ask.launch
def start_skill():
    welcome_message = 'Hello there, would you like a recipe to catch a pokemon?'
    return question(welcome_message)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
