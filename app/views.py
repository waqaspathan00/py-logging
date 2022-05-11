import json
from flask import Blueprint, render_template, request, flash, jsonify
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
            try:
                user_id = current_user.id
                email = current_user.email
            except:
                user_id = request.form.get('user-id')
                email = request.form.get('email')
            finally:
                new_blog = Blog(comment=comment, user_id=user_id, owner=email)
                db.session.add(new_blog)
                db.session.commit()
                flash('Blog added!', category='success')

    blogs = Blog.query.all()
    return render_template("home.html", blogs=blogs)


@views.route('/delete-blog', methods=['POST'])
def delete_note():
    blog = json.loads(request.data)
    blogId = blog['blogId']
    blog = Blog.query.get(blogId)
    if blog:
        if blog.user_id == current_user.id:
            db.session.delete(blog)
            db.session.commit()
            flash('Deleted blog!', category='success')
        else:
            flash("You do not own this blog", category="error")

    return jsonify({})
