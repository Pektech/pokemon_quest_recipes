from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_ask import Ask, statement, question, session
from flask import render_template
from config import Config



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ask = Ask(app, '/pokemon_quest')

from app import routes, models



if __name__ == '__main__':
    app.run()
