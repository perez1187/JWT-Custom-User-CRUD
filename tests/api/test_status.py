import pytest
from status import models

'''
    if we want to test only this file:
    pytest tests/api/test_status.py

    here we test CRUD for status
'''

@pytest.mark.django_db
def test_create_status(auth_client, user):

    payload = dict(
        content="this is a relally coo test. I love tests"
    )

    response = auth_client.post("/api/status/", payload)

    # now we need to ask a question: what do we expect from this

    data = response.data
    # status_from_db = models.Status.objects.all().first() 
    # we can filter like that because this test should have only one record

    status_from_db = models.Status.objects.filter(user_id=user.id).first() 

    assert data["content"] == status_from_db.content # we check content
    assert data["id"] == status_from_db.id  
    assert data["user"]["id"] == user.id 
    # we check user if this is the same
    # user data are nested

@pytest.mark.django_db
def test_get_user_status(auth_client, user):
    '''
        we can create fixture in conftests for it
    '''
    # user_id cannot = user, because it is not a class (like he createad)
    models.Status.objects.create(user_id= user.id, content="another test status")
    models.Status.objects.create(user_id= user.id, content="sec status")

    response = auth_client.get("/api/status/")
    
    assert response.status_code == 200
    assert len(response.data) == 2

@pytest.mark.django_db
def test_get_user_status_detail(auth_client, user):
    status = models.Status.objects.create(user_id= user.id, content="another test status")
    response = auth_client.get(f"/api/status/{status.id}/")

    data = response.data
    assert data["content"] == "another test status" # or status.content
    assert data["id"] == status.id
    assert data["user"]["id"] == user.id


@pytest.mark.django_db
def test_get_user_status_detail_404(auth_client):
    response = auth_client.get("/api/status/0/") # beacuase id never will be 0

    assert response.status_code == 404

@pytest.mark.django_db
def test_put_user_status(auth_client, user):
    status = models.Status.objects.create(user_id= user.id, content="another test status")

    # now we create paylod for put request

    payload = dict(
        content = "I just updated my status"
    )

    response = auth_client.put(f"/api/status/{status.id}/", payload) # f means formatted

    status.refresh_from_db() # we need to refresh status

    data = response.data

    assert data["id"] == status.id # because id must remain the same
    assert status.content == payload["content"]

@pytest.mark.django_db
def test_delete_user_status(auth_client, user):
    status = models.Status.objects.create(user_id= user.id, content="another test status")
    response = auth_client.delete(f"/api/status/{status.id}/")

    assert response.status_code == 204 # 204 - no content


    with pytest.raises(models.Status.DoesNotExist):
        status.refresh_from_db()
    '''
        status.refresh cannot work because we just delete item
        that is why we try to catch an error
    '''