# This file contains the logic for all the API and routes.


from src.init import APP_VERSION
from src.models import User
from src.utils import userExists, addUser, getAllUsers, getUserDetails, updateUserDetails, deleteUser, activateUser, activated, deactivateUser
from flask import Flask, request, jsonify
from datetime import datetime
api = Flask(__name__)


# WELCOME API
@api.route('/')
def welcome():
    return jsonify({
        "application":"user-management",
        "message":"Welcome to User-Management API",
        "version":APP_VERSION,
        "maintainedBy":"Amandeep Singh"
    })



#  REGISTER NEW USER API
@api.route('/users',methods=['POST'])
def register():
    #get payload from post request
    try:
        payload = request.get_json()
        username = payload.get("username")
        if not userExists(username):
            user = User(
                fname= payload.get("fname"),
                lname= payload.get("lname"),
                username = payload.get("username"),
                password = payload.get("password"),
                pincode = payload.get("pincode"),
                access = 0,
                role = 0,
                timestamp = datetime.now()
            )
            #add user to database
            addUser(user)

            return jsonify({"message":"new user registered sucessfully"}),201
    #catch exception        
    except Exception:
        return jsonify({"message":"bad request"}),400


    return jsonify({"message":"user already exists"})


# LIST ALL USERS API
@api.route('/users',methods=['GET'])
def listUsers():
    return jsonify(getAllUsers())



# GET SINGLE USER DETAILS API
@api.route('/users/<username>',methods=['GET'])
def getUser(username):
    #check if user exists and then get the details
    if userExists(username):
        return jsonify(getUserDetails(username))
    
    #return message if user doesn't exists
    return jsonify({
        "message":"user doesn't exists"
    }),404


# UPDATE SINGLE USER DETAILS API
@api.route('/users/<username>',methods=['PUT'])
def updateUser(username):
    payload = request.get_json()
    #check if user exists 
    if userExists(username):
        fname = payload.get("fname")
        lname = payload.get("lname")
        pincode = payload.get("pincode")
        # update the existing user details with the new details
        updateUserDetails(username,fname,lname,pincode)
        return jsonify({"message":"details updated sucessfully"})
    
    #return message if user doesn't exists
    return jsonify({
        "message":"user doesn't exists"
    }),404


# DELETE SINGLE USER WITH GIVEN USERNAME API
@api.route('/users/<username>',methods=['DELETE'])
def removeUser(username):
    #check if user exists 
    if userExists(username):
        # delete user
        deleteUser(username)
        return jsonify({"message":"user deleted sucessfully"})
    
    #return message if user doesn't exists
    return jsonify({
        "message":"user doesn't exists"
    }),404


# ACTIVATE SINGLE USER WITH GIVEN USERNAME API
@api.route('/users/<username>/activate',methods=['PATCH'])
def activate(username):
    # check if user exists
    if userExists(username):
        # make sure user already not activated
        if not activated(username):
            # activate user
            activateUser(username)
            return jsonify({"message":"user activated sucessfully"})
        else:
            return jsonify({"message":"user already activated"})
    
    #return message if user doesn't exists
    return jsonify({
        "message":"user doesn't exists"
    }),404



# DEACTIVATE USER API
@api.route('/users/<username>/deactivate',methods=['PATCH'])
def deactivate(username):
    # check if user exists
    if userExists(username):
        # check if user is activated
        if activated(username):
            # deactivate user
            deactivateUser(username)
            return jsonify({"message":"user deactivated sucessfully"})
        else:
            return jsonify({"message":"user already deactivated"})
    
    #return message if user doesn't exists
    return jsonify({
        "message":"user doesn't exists"
    }),404









