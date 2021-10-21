# test cases in this file are related to "/users/<username>" URI with GET method
# this URI responds with details of the single user by using username as primary key from the URI



# importing json library to convert response data to json type
import json

# tests if correct response code is returned after getting user details
def test_getuser_respcode(app, client):
    res = client.get('/users/jdoe')
    assert res.status_code == 200

# tests if type of response content is json after getting user details
def test_getuser_contenttype(app, client):
    res = client.get('/users/ballen')
    assert "application/json" == res.content_type

# tests if correct data is returned for user details
def test_getuser_content(app, client):
    res = client.get('/users/ballen')
    assert "fname" in json.loads(res.get_data(as_text=True))
    assert "lname" in json.loads(res.get_data(as_text=True))
    assert "pincode" in json.loads(res.get_data(as_text=True))

# tests if correct message is returned when user doesn't exists
def test_deleteuser_content(app, client):
    res = client.get('/users/randomuser')
    excepted = {"message":"user doesn't exists"}
    assert excepted == json.loads(res.get_data(as_text=True))
    assert res.status_code == 404
