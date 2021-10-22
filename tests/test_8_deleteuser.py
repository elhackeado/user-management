# this file contains the test cases related to "/users/<username>" URI with DELETE method.
# this URI deletes the user from the database and responds with the appropriate message


# importing json library to convert response data to json type
import json

# tests if correct response code and message is returned after deleting the user
def test_deleteuser_respcode(app, client):
    res = client.delete('/users/jdoe')
    assert res.status_code == 200
    excepted = {"message":"user deleted sucessfully"}
    assert excepted == json.loads(res.get_data(as_text=True))


# tests if type of response content is json
def test_deleteuser_contenttype(app, client):
    res = client.delete('/users/ballen')
    assert "application/json" == res.content_type

# tests if correct message is displayed when user doesn't exists
def test_deleteuser_content(app, client):
    res = client.delete('/users/ballen')
    excepted = {"message":"user doesn't exists"}
    assert excepted == json.loads(res.get_data(as_text=True))
    assert res.status_code == 404