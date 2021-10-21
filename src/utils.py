# This file contains the helper functions and queries related user data from database

#import database connection class
from src.models import db




# to check if user already exist in the database
def userExists(username):
    # get host db connection 
    con = db().getConnection()
    # select the user database 
    usermgmt = con['user-management']
    # query list of users with given username
    users = list(usermgmt.users.find({"username":username},{'_id':0}))
    con.close()
    if len(users)==0:
         return False
    return True


# to add new user to database
def addUser(user):
    con = db().getConnection()
    # select the user database 
    usermgmt = con['user-management']
    # serialize user object and insert to database
    usermgmt.users.insert_one(toJSON(user))
    con.close()


    
# to serialize the User object to JSON
def toJSON(user):
    return {
    "fname" : user.fname,
    "lname" : user.lname,
    "username" : user.username,
    "password" : user.password,
    "pincode" : user.pincode,
    "access" : user.access,
    "role" : user.role,
    "timestamp" : user.timestamp
    }


# query list of all users from database
def getAllUsers():
    # get host db connection 
    con = db().getConnection()
    # select the user database 
    usermgmt = con['user-management']
    # query list of users with given username
    users = list(usermgmt.users.find({},{'username':1,'_id':0}))
    users = [x['username'] for x in users]
    con.close()
    return {
        "totalUsers":len(users), 
        "users":", ".join(users)}



# query details of single user
def getUserDetails(username):
    # get host db connection 
    con = db().getConnection()
    # select the user database 
    usermgmt = con['user-management']
    # query the details for the user using username
    user = list(usermgmt.users.find({"username":username},{'_id':0,'password':0}))
    con.close()
    return user[0]


# to update the user details in the database
def updateUserDetails(username,fname,lname,pincode):
    # get host db connection 
    con = db().getConnection()
    # select the user database 
    usermgmt = con['user-management']
    # update the details for the user for given username
    usermgmt.users.update_one({'username':username},
    {"$set":{
        'fname': fname,
        'lname': lname,
        'pincode': pincode
        }})
    con.close()


# to delete user from the database
def deleteUser(username):
    # get host db connection 
    con = db().getConnection()
    # select the user database 
    usermgmt = con['user-management']
    # delete the user from database with the given username
    usermgmt.users.delete_one({'username':username})
    con.close()


# activate the user by setting access value to 1 in database for the given user
def activateUser(username):
    # get host db connection 
    con = db().getConnection()
    # select the user database 
    usermgmt = con['user-management']
    # update the access value to 1 to activate the user
    usermgmt.users.update_one({'username':username},
    {"$set":{
        'access': 1
        }})
    con.close()


# check if user already activated by checking access attribute of the user
def activated(username):
    user  = getUserDetails(username)
    # check the access value of the user
    if user["access"]==0:
         return False
    return True


# deactivate the user by setting access value to 0 in database for the given user
def deactivateUser(username):
    # get host db connection 
    con = db().getConnection()
    # select the user database 
    usermgmt = con['user-management']
    # update the access value to 1 to activate the user
    usermgmt.users.update_one({'username':username},
    {"$set":{
        'access': 0
        }})
    con.close()