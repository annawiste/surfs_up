#import flask
from flask import Flask
#Create new Flask instance
app = Flask(__name__)
#Define root
@app.route('/')
#create a function
def hello_world():
    return 'Hello world'