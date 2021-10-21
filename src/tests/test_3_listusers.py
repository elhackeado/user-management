# test cases in this file are related to "/users" endpoint with GET method
# this endpoint responds with list of all users present in the database
#TESTS
# 1. check response code
# 2. check response content type
# 3. check reponse message 


# importing json library to convert response data to json type
import json

# tests if correct response code is returned
def test_getusers_respcode(app, client):
    res = client.get('/users')
    assert res.status_code == 200

# tests if type of response content is json
def test_getusers_contenttype(app, client):
    res = client.get('/users')
    assert "application/json" == res.content_type

# tests if correct data is displayed
def test_getusers_content(app, client):
    res = client.get('/users')
    assert "totalUsers" in json.loads(res.get_data(as_text=True))
    assert "users" in json.loads(res.get_data(as_text=True))
