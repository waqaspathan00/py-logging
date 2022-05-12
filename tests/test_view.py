""" testing viewable routes """


def test_home_visitable(client):
    """ test that the home page is visible """
    response = client.get("/")
    data = response.data.decode("utf-8")
    assert "Blogs" in data


def test_login_visitable(client):
    """ test that the home page is visible """
    response = client.get("/login")
    data = response.data.decode("utf-8")
    assert "Login" in data


def test_sign_up_visitable(client):
    """ test that the home page is visible """
    response = client.get("/sign-up")
    data = response.data.decode("utf-8")
    assert "Sign Up" in data
