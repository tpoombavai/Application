from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# seedvalue is initialized to zero
seed = 0

@app.route('/', methods=['POST', 'GET'])
def home():
    global seed # we need to modify the global variable seed hence declaring it as global

    if request.method == 'POST': # if POST method accept the seed value if integer
        data = request.get_json()

        if 'num' in data and type(data['num']) is int:
            seed = data['num']
            return make_response(jsonify({'message': 'Seed value updated successfully'}), 200)
        else:
            return make_response(jsonify({'message': 'Invalid seed value; Should be an integer value'}), 400)

    elif request.method == 'GET':
        return str(seed) # if GET method return the string seed value

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
