# Read environment variables to use in application

import configparser
parser = configparser.ConfigParser()

# parsing configuration file containing variables
parser.read('config.env')

# Database Variables
DB_USERNAME = parser.get("DATABASE", "DB_USERNAME")
DB_PASSWORD = parser.get("DATABASE", "DB_PASSWORD")
DB_HOST = parser.get("DATABASE", "DB_HOST")
DB_PORT = parser.get("DATABASE", "DB_PORT")

# Application Variables
APP_PORT = parser.get("APPLICATION","APP_PORT")
APP_VERSION = parser.get("APPLICATION","APP_VERSION")
