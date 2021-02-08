from flask import Flask , jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from four fruits'
    
@app.route('/send')
def send():
    dict = {
        "name" : "Md sharique",
        "age" : 12
        }
    return jsonify(dict)
