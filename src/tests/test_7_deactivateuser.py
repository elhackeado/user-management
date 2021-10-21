# this file contains the test cases related to "/users/<username>/deactivate" URI with PATCH method
# this URI takes username as input in URI and deactivates the user

# importing json library to convert response to json type
import json

# tests if response code, type and message is correct after deactivating the user
def test_deactivateuser_resp(app, client):
    res = client.patch("/users/ballen/deactivate")
    assert res.status_code == 200
    assert "application/json" == res.content_type
    excepted = {"message":"user deactivated sucessfully"}
    assert excepted == json.loads(res.get_data(as_text=True))


# tests if response message is correct if user is already deactivated
def test_deactivate_deactivateduser(app, client):
    res = client.patch("/users/ballen/deactivate")
    assert res.status_code == 200
    assert "application/json" == res.content_type
    excepted = {"message":"user already deactivated"}
    assert excepted == json.loads(res.get_data(as_text=True))



# tests if response code, type and message is correct if user doesn't exists
def test_deactivate_nonexistinguser(app, client):
    res = client.patch("/users/randomuser/deactivate")
    assert res.status_code == 404
    assert "application/json" == res.content_type
    excepted = {"message":"user doesn't exists"}
    assert excepted == json.loads(res.get_data(as_text=True))
