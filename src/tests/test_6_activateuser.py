# this file contains the test cases related to "/users/<username>/activate" URI with PATCH method
# this URI takes username as input in URI and activates the user

# importing json library to convert response to json type
import json

# tests if response code, type and message is correct after activating the user
def test_activateuser_resp(app, client):
    res = client.patch("/users/ballen/activate")
    assert res.status_code == 200
    assert "application/json" == res.content_type
    excepted = {"message":"user activated sucessfully"}
    assert excepted == json.loads(res.get_data(as_text=True))


# tests if response message is correct if user is already activated
def test_activate_activateduser(app, client):
    res = client.patch("/users/ballen/activate")
    assert res.status_code == 200
    assert "application/json" == res.content_type
    excepted = {"message":"user already activated"}
    assert excepted == json.loads(res.get_data(as_text=True))



# tests if response code, type and message is correct if user doesn't exists
def test_activate_nonexistinguser(app, client):
    res = client.patch("/users/randomuser/activate")
    assert res.status_code == 404
    assert "application/json" == res.content_type
    excepted = {"message":"user doesn't exists"}
    assert excepted == json.loads(res.get_data(as_text=True))
