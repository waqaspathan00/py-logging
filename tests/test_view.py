""" testing viewable routes """

def test_home_visitable(client):
    """ test that the home page is visible """
    # ARRANGE - using client fixture

    # ACT
    response = client.get("/")
    data = response.data.decode("utf-8")

    # ASSERT
    assert "Home" in data
