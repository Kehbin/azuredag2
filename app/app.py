from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/iets',methods=['GET'])
def hello_world_iets():
    return 'Hello, World! IETS'
