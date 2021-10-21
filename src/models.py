from pymongo import MongoClient
from readenvvars import DB_HOST,DB_PASSWORD,DB_PORT,DB_USERNAME


class db:

    #get database connection
    def getConnection(self):
        conString = "mongodb://{username}:{password}@{host}:{port}/".format(
            username=DB_USERNAME,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return MongoClient(conString,connect=False)
    




class User:


    def __init__(self,fname,lname,username,password,pincode,access,role,timestamp):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password
        self.pincode = pincode
        self.access = access
        self.role = role
        self.timestamp = timestamp


    


