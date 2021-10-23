# This file contains the data validation functions

# NOTE: Currently only empty value validations is implemented, further validations must be implemented to make sure that application data remains consistent

import hashlib, os, binascii

# check if string is empty or null
def notEmptyString(str):
    if str==None:
        return False
    if  len(str.strip())==0:
        return False
    return True

# Hash a password for storing.
def hashPassword(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 
# Verify a stored password against one provided by user
# this method can be used while implementing for login functionality
def verifyPassword(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password