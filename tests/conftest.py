import pytest
from rest_framework.test import APIClient
from user import services as user_services

# we can do it with user model as well
@pytest.fixture
def user():
    user_dc = user_services.UserDataClass( # user data class
        first_name="Harry",
        last_name="Potter", 
        email="harry@hooogwards.com",
        password="timeforsometesting1"
    )
    user = user_services.create_user(user_dc=user_dc)

    return user

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def auth_client(user, client): # we need to create user adn we need to use client
    client.post("/api/login/", dict(email=user.email,password="timeforsometesting1"))
    # we need to paste password manually

    return client # we just retunrn a client who is autheticated
