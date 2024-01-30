from flask import Flask, request, jsonify, make_response
import socket 
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():

    if request.method == 'POST': # if POST method accept the seed value if integer
        args = ['python3', 'stress.py']
        subprocess.Popen(args)
        return make_response(jsonify({'message': 'Stress test started successfully'}), 200)
        
    elif request.method == 'GET':
        return str(socket.gethostname() ) # if GET method return the string of private IP

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
