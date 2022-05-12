import random


def test_create_blog(client):
    """ test creating a blog with filler post req"""
    response = client.post("/", data={
        "blog-comment": "this is blog post #" + str(random.randint(1, 1000000)),
        "user-id": 0,
        "owner": "tester@gmail.com"
    })
    data = response.data.decode("utf-8")
    assert "Blog added!" in data


def test_view_blogs(client):
    """ test blogs are being saved """
    from app.models import Blog
    blogs = Blog.query.all()
    assert blogs


def test_delete_blogs(client):
    from app.models import Blog
    from app import db
    db.session.query(Blog).delete()
    db.session.commit()
    blogs = Blog.query.all()
    assert not blogs



