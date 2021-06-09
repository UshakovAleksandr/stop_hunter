from flask import Flask
from flask_restful import Api, Resource, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
