from flask import Blueprint, render_template, request, flash
import logging

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        password = request.form.get('password')
        flash("Check log files")

        if len(password) < 6:
            logging.error('Password is too short!')
        else:
            logging.info('Password is valid!')

    return render_template("home.html")
