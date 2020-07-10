#setting up dependencies
from flask import Flask

#Creating a new flask instance called app
app = Flask(__name__)

#create flask route
@app.route('/')
def hello_world():
    return 'Hello world'
@app.route('/test1/')
def hello2():
    print ('you are at test1 page')
    return 'test1 page loaded'
