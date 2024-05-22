from flask import Flask, jsonify, request

app = Flask(__name__)

# Route to the home page
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# Route to return a simple JSON response
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'message': 'Hello, World!',
        'status': 'success'
    }
    return jsonify(data)

# Route to echo back data sent in a POST request
@app.route('/api/echo', methods=['POST'])
def echo_data():
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
