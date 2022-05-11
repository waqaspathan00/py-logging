""" testing viewable routes """

def test_home_visitable(client):
    """ test that the home page is visible """
    # ARRANGE - using client fixture

    # ACT
    response = client.get("/")
    data = response.data.decode("utf-8")

    # ASSERT
    assert "Search for a recipe!" in data

def test_login_visitable(client):
    """ test that the home page is visible """
    # ARRANGE - using client fixture

    # ACT
    response = client.get("/login")
    data = response.data.decode("utf-8")

    # ASSERT
    assert "Login" in data

def test_sign_up_visitable(client):
    """ test that the home page is visible """
    # ARRANGE - using client fixture

    # ACT
    response = client.get("/sign-up")
    data = response.data.decode("utf-8")

    # ASSERT
    assert "Sign up" in data
