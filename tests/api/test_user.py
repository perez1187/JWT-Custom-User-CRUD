import imp
import pytest
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db # we need this decorator when we writing to db
def test_register_user():
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