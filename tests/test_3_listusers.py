# test cases in this file are related to "/users" URI with GET method
# this URI responds with list of all users present in the database


# importing json library to convert response data to json type
import json

# tests if correct response code is returned after getting all users
def test_getusers_respcode(app, client):
    res = client.get('/users')
    assert res.status_code == 200

# tests if type of response content is json after getting all users
def test_getusers_contenttype(app, client):
    res = client.get('/users')
    assert "application/json" == res.content_type

# tests if correct data is displayed after getting all users
def test_getusers_content(app, client):
    res = client.get('/users')
    assert "totalUsers" in json.loads(res.get_data(as_text=True))
    assert "users" in json.loads(res.get_data(as_text=True))
