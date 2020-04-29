from dotenv import load_dotenv
load_dotenv()
import os
print()
username=os.getenv('USERNAME')
password=os.getenv('PASSWORD')
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://{}:{}@localhost:5432/fyyur'.format(username, password)
