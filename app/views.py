from flask import Blueprint, render_template, request
import logging

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        password = request.form.get('password')

        if len(password) < 1:
            logging.error('Blog is too short!')
        else:
            logging.info('Blog added!')

    return render_template("home.html")
