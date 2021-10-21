# this file contains the test cases related to "/users/<username>" URI with PUT method
# this URI takes the new user details as input and updates it in the database under given username

#to convert response to json type
import json


updateddata = {
    "fname": "flash",
    "lname": "cnet",
    "pincode" : "900005"
    
}


# tests if response code is correct after updating the user details
def test_updateuser_respcode(app, client):
    res = client.put("/users/ballen",
            data=json.dumps(updateddata),
            headers={"Content-Type": "application/json"},)
    assert res.status_code == 200

# test if response content type is correct after updating the user details
def test_updateuser_respcontenttype(app, client):
    res = client.put("/users/ballen",
        data=json.dumps(updateddata),
        headers={"Content-Type": "application/json"},)
    assert "application/json" == res.content_type


# test if response message is correct after updating the user
def test_updateuser_rescontent(app, client):
    res = client.put("/users/ballen",
        data=json.dumps(updateddata),
        headers={"Content-Type": "application/json"},)
    expected = {"message":"details updated sucessfully"}
    assert expected == json.loads(res.get_data(as_text=True))

# test if response message and response code is correct if given user doesn't exists in database
def test_updateuser_nousercontent(app, client):
    res = client.put("/users/randomuser",
        data=json.dumps(updateddata),
        headers={"Content-Type": "application/json"},)
    expected = {"message":"user doesn't exists"}
    assert expected == json.loads(res.get_data(as_text=True))
    assert res.status_code == 404

