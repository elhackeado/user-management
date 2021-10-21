# this file contains the test case related to "/" URI i.e basically index URI
# this URI responds with the welcome information related to the application 

# using json library to convert the response to json
import json

# test if response code and response content is valid
def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = {"application":"user-management","maintainedBy":"Amandeep Singh","message":"Welcome to User-Management API","version":"v0.1"}
    assert expected == json.loads(res.get_data(as_text=True))