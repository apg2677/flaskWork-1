from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


@app.route('/home', methods=['POST', 'GET'], defaults={'name': 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    return '<h1>{} You are on the Home Page!</h1>'.format(name)


@app.route('/json')
def json():
    return jsonify({"key": "value", "list": [1, 2, 3, 4]})


@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {}, You are in {} !</h1>'.format(name, location)


if __name__ == '__main__':
    app.run(host='localhost', port=5013, debug=True)
