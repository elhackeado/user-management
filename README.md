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


## Project Structure
Following is the directory structure of the project.

```   
   main project directory
                |
                |
                --------  src
                |         |
                |         --------- init.py
                |         --------- models.py
                |         --------- routes.py
                |         --------- utils.py
                |
                --------- tests
                |         |
                |         |
                |         --------- conftest.py
                |         --------- test_1_root.py
                |         --------- test_2_registeruser.py
                |         --------- test_3_listusers.py
                |         --------- test_4_getuser.py
                |         --------- test_5_updateuser.py
                |         --------- test_6_activateuser.py
                |         --------- test_7_deactivateuser.py
                |         --------- test_8_deleteuser.py
                |
                |
                ---------- app.py
                ---------- config.env
                ---------- readenvvars.py
                ---------- README.md
                ---------- requirements.txt
```
 ### src <br>
  This directory contains the main source code of the api server. <br>
           1. init.py - to initialize the application and environment variables for the application <br>
           2. models.py - contains User and db model class <br>
           3. routes.py - contains the actual routing and API logics <br>
           4. utils.py - contains helper functions and database query functions <br>

### tests <br>
  This directory contains the unit test cases for the api server. <br>
           1. configtest.py - initialize testing configurations <br>
           2. test_1_root.py - contains 1 test case for index route <br>
           3. test_2_registeruser.py - contains 4 test case for register user API  <br>
           4. test_3_listusers.py - contains 3 test cases for getting all users details API <br>
           5. test_4_getuser.py - contains 4 test cases for getting single user detail API<br>
           6. test_5_updateuser.py - contains 4 test cases for updating user details API <br>
           7. test_6_activateuser.py - contains 3 test cases for activating user API <br>
           8. test_7_deactivateuser.py - contains 3 test cases for deactivating user API <br>
           9. test_8_deleteuser.py - contains 3 test cases for delete user APi <br>

### app.py
 Main flask application containing configurable host and port details

### config.env
Contains application and user variables as follows
```
[DATABASE]
DB_USERNAME - username for database authentication
DB_PASSWORD - password for database authentication
DB_HOST - host name or ip of the database host 
DB_PORT - port on which database services are running

[APPLICATION]
APP_PORT - port at which flask application will run
APP_VERSION - current version of the application
```

### readenvvars.py
This python file reads and initializes the variables from the `config.env` file.

### README.md
This file contains the information reagarding the application and how to use the the application.

### requirements.txt
This file contains list of all the python libraries that are being used in this project.

## Setup Environment & Run Application
This section will help you to setup basic infrastructure for the application and running the application.
### 1. Setup MongoDB Database
       i. Install mongoDB database either standalone or on docker using below link. <br>
            ***Standalone*** : https://docs.mongodb.com/guides/server/install/ <br>
            ***Docker*** : https://www.bmc.com/blogs/mongodb-docker-container/ <br>

      ii. login to mongo shell using `mongo admin -u <username> -p <password>` <br>
     iii. switch to new database using `use user-management` <br>
      iv. insert new document to create collection, use command `db.users.insert({"username":"aman"})` <br>
***Now our database is ready to use. Update all the database related information in `config.env` file.***

### 2. Install Python
    Install python 3.7 version from https://www.python.org/downloads/ for your respective Operating System.

### 3. Install Python Libraries
    Switch to main project directory and install all python dependencies using following command:
        `pip install requirements.txt`

### 4. Run Unit Test Cases [OPTIONAL]
    This section is option just to make sure everything is working fine. There are in total 25 test cases to test basic functionality of the application.
    To run the unit test cases use the following command
        `python -m pytest`

### 5. Run Applicatoin
    Switch to main project directory and run the following command:
        `flask run`
After successfull run it will show the below output on the console:
```
Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
Debug mode: off
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

 Now your flask application is running on port 5000.

 NOTE: If there is any error then first make sure port 5000 is not in use already, in that case you can change to any other free port by changing value of `APP_PORT` variable in `config.env` file.



## API Overview
A total of 7 APIs were developed to perform basic user management operations. <br>

* #### Register User `/users` - POST    ***To add new user***
* #### Get All Users `/users` - GET    ***To get list and count of all users***
* #### Get User Details `/users/<username>` - GET    ***To get details of a single user***
* #### Update User Details `/users/<username>` - PUT    ***To update details of a user***
* #### Delete User `/users/<username>` - DELETE    ***To delete a user***
* #### Activate User `/users/<username>/activate` - PATCH    ***To activate the user***
* #### Deactivate User `/users/<username>/deactivate` - PATCH    ***To deactivate a user*** <br>

Detailed description for each API is given below. This will give you a good idea what that particular API does and how you can use that API. <br>

### 1. Register New User
This API registers new user to the system. It takes `first name`, `last name`, `username`, `password`, `pincode` as an input and adds the user to the database with respective details. Here `username` attribute is the primary key so before adding the new user, the system checks that no user with same username exists in the database. If there is some user with the same username then it will not add new user to the system and returns a already exists message.

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
***If user with the given username already exists in the database then following response is returned***
```json
  {
      "message":"user already exists"
  }
```

### 2. Get All Users
This API gets total count of registered users and list of usernames of all users in the system. This API doesn't require any input.

**Route** : `/users` <br>
**Method Type** : `GET` <br>
**Sample Request Body** : ***Not Needed***

***After successful execution of the above request you will get the following respone*** <br>

**Sample Response Body** :
```json
    {
        "totalUsers": 11,
        "users":  "BeverlyFox, SherrySchaefer, BethanyNelson, JessicaTaylor, GinaHansen, RobertJenkins, ChristopherOchoa, AudreyAnderson, JamesMills, SaraRobertson, MistyPalmer"
    }
```

### 3. Get User Details
This API gets details of a single user. This API takes username as a input in the URI which in turn gets the details of that user from the database. If the user with the given username doesn't exists the API returns a user doesn't exists message.


**Route** : `/users/<username>` <br>
**Method Type** : `GET` <br>
**Sample Request Body** : ***Not Needed***

***After successful execution of the above request you will get the following respone*** <br>

**Sample Response Body** :
```json
    {
    "access": 0,
    "fname": "Barry",
    "lname": "Allen",
    "pincode": 740008,
    "role": 0,
    "timestamp": "Thu, 21 Oct 2021 12:37:15 GMT",
    "username": "ballen"
    }
```
***If user with the given username doesn't exists the following message is given in response***
```json 
    {
        "message":"user doesn't exists"
    }
```

### 4. Update User Details
This API updates details of a single user. This API takes `username` as a input in the URI and `fname`, `lname` and `pincode` in the request body. This API also checks existence of the username in the database before updating the details, If the user with the given username doesn't exists the API returns a user doesn't exists message.


**Route** : `/users/<username>` <br>
**Method Type** : `PUT` <br>
**Sample Request Body** :
```json
    {
        "fname":"The",
        "lname":"Flash",
        "pincode":"11111"
    }
```

***After successful execution of the above request you will get the following respone*** <br>

**Sample Response Body** :
```json
    {
        "message": "details updated sucessfully"
    }
```
***If user with the given username doesn't exists the following message is given in response***
```json 
    {
        "message": "user doesn't exists"
    }
```

### 5. Delete User
This API deletes a single user from the database. This API takes `username` as an input in the URI. This API checks existence of the username in the database before deleting the user, If the user with the given username doesn't exists the API returns user doesn't exists message.


**Route** : `/users/<username>` <br>
**Method Type** : `DELETE` <br>
**Sample Request Body** : ***Not Needed***

***After successful execution of the above request you will get the following respone*** <br>

**Sample Response Body** :
```json
    {
        "message": "user deleted sucessfully"
    }
```
***If user with the given username doesn't exists the following message is given in response***
```json 
    {
        "message": "user doesn't exists"
    }
```

### 6. Activate User
By default, when any new user registers it is in deactivated mode until activated. So this particular API is used to activate the user by setting the user attribute `access=1` in the database. This API takes `username` as a input in the URI. This API checks existence of the username in the database before activating the user, If the user with the given username doesn't exists the API returns a user doesn't exists message. Also if the user is already activated then it returns already activated message.


**Route** : `/users/<username>/activate` <br>
**Method Type** : `PATCH` <br>
**Sample Request Body** : ***Not Needed***

***After successful execution of the above request you will get the following respone*** <br>

**Sample Response Body** :
```json
    {
        "message": "user activated sucessfully"
    }
```
***If user with the given username doesn't exists the following message is given in response***
```json 
    {
        "message": "user doesn't exists"
    }
```
***If user with the given username is already activated the following message is given in response***
```json 
    {
        "message": "user already activated"
    }
```

### 7. Deactivate User
This API is used to deactivate the user by setting the user attribute `access=0` in the database. This API takes `username` as an input in the URI. This API checks existence of the username in the database before deactivating the user, If the user with the given username doesn't exists the API returns user doesn't exists message. Also if the user is already deactivated then it returns already deactivated message.


**Route** : `/users/<username>/deactivate` <br>
**Method Type** : `PATCH` <br>
**Sample Request Body** : ***Not Needed***

***After successful execution of the above request you will get the following respone*** <br>

**Sample Response Body** :
```json
    {
        "message": "user deactivated sucessfully"
    }
```
***If user with the given username doesn't exists the following message is given in response***
```json 
    {
        "message": "user doesn't exists"
    }
```
***If user with the given username is already deactivated the following message is given in response***
```json 
    {
        "message": "user already deactivated"
    }
```

## Functionalities
This section will give you a brief idea about the use and functionalities of the application.

1. A user can register with user attributes like `first name`, `last name`, `username` etc.
2. The application will check if the given username is available i.e. there should be no user with given username in the database.
3. The application will register the user if the unique username is provided.
4. By default user is in deactivated mode that means it can't login until it is activated by some Admin or email verification.
5. Admin will activate the user.
6. Now user can login using his registered credentials.
7. A user or Admin can change the details of the user like `first name`, `last name`, `pincode`.
8. A user can be deactivated by Admin.
9. A user can be deleted by Admin.
10. Admin can get list of all the users.
11. Admin can get details of a user.

***NOTE : Authentication/Authorization, Session Management, User activation by email verification and secured APIs is not yet implemented. So all the APIs can be accessed by anyone. These feature may come as the enhancements to the project in near future. Following section will give you more insight on why you would need these features.***

## Enhancement
This section will give of information about all the upcoming enhancements. Following is the list of few features that can be expected to be implemented in near future.
1. `Secure APIs` - Currently all the APIs can be accessed by anyone, so there is need of role based access to make this application work properly.
2. `Authentication/Authorization` - This feature is in accordance with the first feature since the APIs can only be secured if proper Authentication and Authorization is in place.
3. `Logging` - This is one of the most important feature when you want to build any production grade application since logging helps a lot in troubleshooting the application in case any exception occurs.
4. `Session Management` - This feature becomes important if you want to implement Login/Logout feature in your application. This can be implemented along with the AUTHORIZATION feature using the JWT tokens.
5. `Automated User Activation` - The user activation can be automated by sending verification links to the registered user. This can be a great feature to make the application flow seamless and avoid the manual activation of the user.
6. `Hashing the Passwords and Other Personal Information` - Currently all the user information is saved in the plain text format in database but to align with Data Privacy policy its always recommended to save personal in hash/encoded format.
7. `Data Validation` - Currently only one level of data validation is done i.e simple empty or null value checker, further level of validation can be included such as data type validations, string length validations, password policy validation and more.

## End of File