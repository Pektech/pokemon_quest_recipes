from flask_ask import Ask, statement, question, session
from app import app, ask


@ask.launch
def start_skill():
    welcome_message = 'Hello there, would you like a recipe to catch a pokemon?'
    return question(welcome_message)


@app.route('/')
def hello_world():
    return 'Hello World!'
