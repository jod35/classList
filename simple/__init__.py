from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import DevConfig
from flask_migrate import Migrate

app=Flask(__name__)
app.config.from_object(DevConfig)

db=SQLAlchemy(app)
migrate=Migrate(app,db)

from . import routes
