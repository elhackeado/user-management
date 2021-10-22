# this file contains the test cases related to "/users" URI with POST method
# this URI takes user details as input and registers in database

# importing json library to convert response data to json type
import json


data = {
    "fname":"John",
    "lname":"Doe",
    "username":"jdoe",
    "password" : "rockingjdoe",
    "pincode" : 144008
    }

newdata = {
    "fname": "Barry",
    "lname": "Allen",
    "username": "ballen",
    "password" : "speeditup",
    "pincode" : 740008
    
}


# tests if response code is correct after registering new user
def test_registeruser_respcode(app, client):
    res = client.post("/users",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},)
    assert res.status_code == 201

# tests if response content type is correct
def test_registeruser_contenttype(app, client):
    res = client.post("/users",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},)
    assert "application/json" == res.content_type

# tests if correct response is given when alredy existing user is registered again
def test_registerusers_existinguser(app, client):
     res = client.post("/users",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},)
     expected = {"message":"user already exists"}
     assert expected == json.loads(res.get_data(as_text=True))

# tests if correct response is returend when new user is registered
def test_registerusers_newuser(app, client):
     res = client.post("/users",
                data=json.dumps(newdata),
                headers={"Content-Type": "application/json"},)
     expected = {"message":"new user registered successfully"}
     assert expected == json.loads(res.get_data(as_text=True))