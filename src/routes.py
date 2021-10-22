# This file contains the logic for all the API and routes.

# Reading application variable configured in config.env file
from src.init import APP_VERSION
from src.models import User
from src.utils import userExists, addUser, getAllUsers, getUserDetails, updateUserDetails, deleteUser, activateUser, activated, deactivateUser
from src.validations import notEmptyString
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
    try:
        #get payload from post request
        payload = request.get_json()

        username = payload.get("username")
        #Make sure username is not empty
        if notEmptyString(username):
        #Make sure user doesn't already exists in the system
            if not userExists(username):
                fname= payload.get("fname")
                lname= payload.get("lname")
                username = payload.get("username")
                password = payload.get("password")
                pincode = payload.get("pincode")
                # Make sure all input parameters are passed
                if notEmptyString(fname) and notEmptyString(lname) and notEmptyString(password) and notEmptyString(str(pincode)):
                    user = User(
                        fname= fname,
                        lname= lname,
                        username = username,
                        password = password,
                        pincode = pincode,
                        access = 0, # keeping user deactivated by default
                        role = 0,   # this variable can be used in case of Authorization of resources/APIs
                        timestamp = datetime.now() # Registration date and time
                    )
                    #add user to database
                    addUser(user)
                    #return successfull registered message
                    return jsonify({"message":"new user registered successfully"}),201

                else:
                    return jsonify({"message":"parameter missing"}),400
            else:
                # return message if user already exists
                return jsonify({"message":"user already exists"})
        else:
            # return message if username is not provided
            return jsonify({"message":"please provide username"})
    # return server error message if any exception occurs
    except:
        return jsonify({
                "message":"Internal server error"
                }),500


    


# LIST ALL USERS API
@api.route('/users',methods=['GET'])
def listUsers():
    return jsonify(getAllUsers())



# GET SINGLE USER DETAILS API
@api.route('/users/<username>',methods=['GET'])
def getUser(username):
    try:
        #check if user exists and then get the details
        if userExists(username):
            return jsonify(getUserDetails(username))
        
        #return message if user doesn't exists
        return jsonify({
            "message":"user doesn't exists"
            }),404
    # return server error message if any exception occurs
    except:
        return jsonify({
                "message":"Internal server error"
                }),500


# UPDATE SINGLE USER DETAILS API
@api.route('/users/<username>',methods=['PUT'])
def updateUser(username):
    try:
        payload = request.get_json()
        #check if user exists 
        if userExists(username):
            fname = payload.get("fname")
            lname = payload.get("lname")
            pincode = payload.get("pincode")
            # Make sure all input parameters are passed
            if notEmptyString(fname) and notEmptyString(lname) and notEmptyString(str(pincode)):
                # update the existing user details with the new details
                updateUserDetails(username,fname,lname,pincode)
                return jsonify({"message":"details updated sucessfully"})
            else:
                 return jsonify({"message":"parameter missing"}),400
        #return message if user doesn't exists
        return jsonify({
            "message":"user doesn't exists"
        }),404
    # return server error message if any exception occurs
    except:
        return jsonify({
                "message":"Internal server error"
                }),500


# DELETE SINGLE USER WITH GIVEN USERNAME API
@api.route('/users/<username>',methods=['DELETE'])
def removeUser(username):
    try:
        #check if user exists 
        if userExists(username):
            # delete user
            deleteUser(username)
            return jsonify({"message":"user deleted sucessfully"})
        
        #return message if user doesn't exists
        return jsonify({
            "message":"user doesn't exists"
        }),404
    # return server error message if any exception occurs
    except:
        return jsonify({
                "message":"Internal server error"
                }),500


# ACTIVATE SINGLE USER WITH GIVEN USERNAME API
@api.route('/users/<username>/activate',methods=['PATCH'])
def activate(username):
    try:
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
    # return server error message if any exception occurs
    except:
        return jsonify({
                "message":"Internal server error"
                }),500



# DEACTIVATE USER API
@api.route('/users/<username>/deactivate',methods=['PATCH'])
def deactivate(username):
    try:
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
    # return server error message if any exception occurs
    except:
        return jsonify({
                "message":"Internal server error"
                }),500









