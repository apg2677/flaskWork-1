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


@app.route('/theform')
def theform():

    return '''<form method="POST" action="/theform">
                <input type="text" name="name"/>
                <input type="text" name="location"/>
                <input type="submit" value="Submit"/>
               </form>'''


@app.route('/theform', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']

    return 'Hello {}.  You are from {}. You have submitted the form!'.format(name, location)


@app.route('/processjson', methods=['POST'])
def processjson():

    data = request.get_json()

    name = data['name']
    location = data['location']

    randomlist = data['randomlist']

    return jsonify({'result': 'success',
                    'name': name,
                    'location': location,
                    'randomkeyinlist': randomlist[1]
                    })


if __name__ == '__main__':
    app.run(host='localhost', port=5013, debug=True)
