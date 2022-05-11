""" this file contains fixtures available to other test files """

import pytest
import os
from app import create_app, db

@pytest.fixture()
def application():
    """This makes the app"""
    os.environ['FLASK_ENV'] = 'testing'
    application = create_app()
    # application.app_context().push()
    application.config.update({
        "TESTING": True,
    })
    # testing
    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()
        #drops the database tables after the test runs
        #db.drop_all()s

@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()
