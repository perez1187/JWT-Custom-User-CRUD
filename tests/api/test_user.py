import pytest
from rest_framework.test import APIClient

# client = APIClient()
'''
    we can create client in conftest.py and then we paste client here:
    def test_register_user(client):
    def test_login_user(user, client):
    etc
'''

@pytest.mark.django_db # we need this decorator when we writing to db
def test_register_user(client): # remember to name def test_ (from pytest.ini)
    payload = dict(
        first_name="Harry",
        last_name="Potter", 
        email="harry@hooogwards.com",
        password="timeforsometesting1"
    )

    response = client.post("/api/register/", payload)

    # when we post something we get back user id etc
    data = response.data

    assert data["first_name"] == payload["first_name"]
    assert data["last_name"] == payload["last_name"]
    assert data["email"] == payload["email"]
    assert "id" in data
    assert "password" not in data


@pytest.mark.django_db
def test_login_user(user, client):
    '''
        we can create credentials manualy or use function from conftest.py
        then we paste user here: def test_login_user(user)
    '''
    
    # payload = dict(
    #     first_name="Harry",
    #     last_name="Potter", 
    #     email="harry@hooogwards.com",
    #     password="timeforsometesting1"
    # )

    # client.post("/api/register/", payload)

    response = client.post("/api/login/", dict(email="harry@hooogwards.com",password="timeforsometesting1"))

    assert response.status_code == 200

@pytest.mark.django_db
def test_login_user_fail(client):
    response = client.post("/api/login/", dict(email="harry@hooogwards.com",password="timeforsometesting1"))

    assert response.status_code == 403

@pytest.mark.django_db
def test_get_me():
    pass