# User Management System
------------------------
**Developer** : Amandeep Singh <br>
**Email** : amanthakur0001@gmail.com<br>

## Problem Statement
To build a API backend for the user management system which can perform basic CRUD operation like register new user, get all users, get details of a user, update details for a user and delete the user.

## Technology Used
**Programming Language** : Python v3.7.3 <br>
**Framework** : Flask v1.1.1 <br>
**Python Libraries** : configparser, flask, pymongo, json, datetime, pytest <br>
**Database** : MongoDB v5.0.3 <br>

## API Overview
A total of 7 APIs were developed to perform basic user management operations. <br>
### 1. Register New User
This API registers new user to the system. It takes `first name`, `last name`, `username`, `password`, `pincode` as an input and adds the user to the database with respective details. Here username attribute is the primary key so before adding the new user the system checks that no user with same username exists in the database. If there is some user with the same username then it will not add new user to the system and respond with a already exists message.

**Route** : `/users` <br>
**Method Type** : `POST` <br>
**Header** : `Content-Type: application/json` <br>
**Sample Request Body** : 
```json 
  {
      "fname": "Barry",
      "lname": "Allen",
      "username": "ballen",
      "password" : "speeditup",
      "pincode" : "740008"
    
  }
 ```
***After successful execution of the above request you will get the following respone*** <br>

**Sample Response Body** :
```json
  {
      "message":"new user registered sucessfully"
  }
```

### 2. Get All Users
This API gets all the users registered in the database. This API doesn't require any input.

**Route** : `/users` <br>
**Method Type** : `GET` <br>
**Sample Request Body** : ***Not Needed***

***After successful execution of the above request you will get the following respone*** <br>

**Sample Response Body** :
```json
    {
        "totalUsers": 18,
        "users": "amansinghhh, amansin, amansi, amansiss, amansssi, amanssi, amanssiaaa, BeverlyFox, SherrySchaefer, BethanyNelson, JessicaTaylor, GinaHansen, RobertJenkins, ChristopherOchoa, AudreyAnderson, JamesMills, SaraRobertson, MistyPalmer"
    }
```