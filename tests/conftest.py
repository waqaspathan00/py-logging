""" this file contains fixtures available to other test files """

import pytest
import os

from werkzeug.security import generate_password_hash

from app import create_app, db
from app.models import User


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
        # drops the database tables after the test runs
        # db.drop_all()


@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()


@pytest.fixture()
def new_account(application):
    user = User.query.filter_by(email="tester@gmail.com").first()

    # make an account for testing
    if not user:
        user = User(
            email="tester@gmail.com",
            password=generate_password_hash("testingpass123", method="sha256")
        )
        db.session.add(user)
        db.session.commit()

    return user

@pytest.fixture
def delete_user_t(application):
    user = User.query.filter_by(email="tester@gmail.com").first()
    db.session.delete(user)
    db.session.commit()
    return user
