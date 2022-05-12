import random


def test_create_user_with_existing_email(client, new_account):
    """ users should not be able to create accounts with taken emails """
    response = client.post("/sign-up", data={
        "email": "tester@gmail.com",
        "password1": "testing1",
        "password2": "testing2",
    })
    data = response.data.decode("utf-8")
    assert 'Email already exists.' in data


def test_create_user_missing_at_symbol(client):
    """ users should not be able to enter emails without @ symbol """

    response = client.post("/sign-up", data={
        "email": "tester" + str(random.randint(1, 1000000)) + "gmail.com",
        "password1": "testing1",
        "password2": "testing1"
    })
    data = response.data.decode('utf-8')
    assert "Must be valid email using @" in data


def test_create_user_missing_domain(client):
    """ users should not be able to enter emails without domain like .com """

    response = client.post("/sign-up", data={
        "email": "tester" + str(random.randint(1, 1000000)) + "@gmail",
        "password1": "testing1",
        "password2": "testing1"
    })
    data = response.data.decode('utf-8')
    assert "Must be valid email using domain like .com" in data


def test_create_user_too_short_email(client):
    """ users should not be able to enter emails less than 10 characters """

    response = client.post("/sign-up", data={
        "email": str(random.randint(1, 99)) + "@gmail.com",
        "password1": "testing1",
        "password2": "testing1"
    })
    data = response.data.decode('utf-8')
    assert "Email must be greater than 12 characters." in data


def test_create_user_not_matching_password(client):
    """ users must have matching passwords """

    response = client.post("/sign-up", data={
        "email": "tester" + str(random.randint(1, 100000)) + "@gmail.com",
        "password1": "testing1",
        "password2": "testing2"
    })
    data = response.data.decode('utf-8')
    assert 'Passwords dont match.' in data


def test_create_user_too_short_password(client):
    """ passwords must be atleast 7 characters long """

    response = client.post("/sign-up", data={
        "email": "tester" + str(random.randint(1, 100000)) + "@gmail.com",
        "password1": "tstpss",
        "password2": "tstpss"
    })
    data = response.data.decode('utf-8')
    assert 'Password must be at least 7 characters.' in data


def test_create_user_no_capital_letter_in_pass(client):
    """ passwords must contain an uppercase letter """

    response = client.post("/sign-up", data={
        "email": "tester" + str(random.randint(1, 100000)) + "@gmail.com",
        "password1": "testing1",
        "password2": "testing1"
    })
    data = response.data.decode('utf-8')
    assert 'Password must contain atleast 1 uppercase letter' in data


def test_create_user_no_lowercase_letter_in_pass(client):
    """ passwords must contain a lowercase letter """

    response = client.post("/sign-up", data={
        "email": "tester" + str(random.randint(1, 100000)) + "@gmail.com",
        "password1": "TESTING1",
        "password2": "TESTING1"
    })
    data = response.data.decode('utf-8')
    assert 'Password must contain atleast 1 lowercase letter' in data


def test_create_user_no_number_in_pass(client):
    """ passwords must contain a number """

    response = client.post("/sign-up", data={
        "email": "tester" + str(random.randint(1, 100000)) + "@gmail.com",
        "password1": "TestingPass",
        "password2": "TestingPass"
    })
    data = response.data.decode('utf-8')
    assert 'Password must contain atleast 1 number' in data


