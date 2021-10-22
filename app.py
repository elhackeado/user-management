# This is the main entrypoint of the flask application

#import all endpoints from routes
from src.routes import *


# Application host and port configuration
if __name__ == '__main__':
   app.run(host="0.0.0.0",port=APP_PORT)
 