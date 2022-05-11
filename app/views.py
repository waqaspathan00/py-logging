from flask import Blueprint, render_template, request, flash
from flask_login import current_user
from .models import Blog
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        comment = request.form.get('blog-comment')

        if len(comment) < 1:
            flash('Blog is too short!', category='error')
        else:
            new_blog = Blog(comment=comment, user_id=current_user.id, owner=current_user.email)
            db.session.add(new_blog)
            db.session.commit()
            flash('Blog added!', category='success')

    blogs = Blog.query.all()
    return render_template("home.html", blogs=blogs)

