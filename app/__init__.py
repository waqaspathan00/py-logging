from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path
import logging

db = SQLAlchemy()
DB_NAME = "database.db"

logging.basicConfig(
    level=logging.INFO,  # output log levels >= this one
    filename="logs/log.log",  # filename to output to
    filemode="w",  # create a new file each time
)

"""
# log types and their levels

logging.debug("debug message")  # L1
logging.info("info message")  # L2
logging.warning("warning message")  # L3
logging.error("error message")  # L4
logging.critical("critical message")  # L5
"""

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'uc328b3787dsa'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    create_database(app)

    return app


def create_database(app):
    if not path.exists('app/' + DB_NAME):
        db.create_all(app=app)
        logging.info('Created Database!')
