from flask import Flask, jsonify, request, url_for, redirect, session, render_template

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Thisisasecret!'


@app.route('/')
def index():
    session.pop('name', None)
    return '<h1>Hello, World!</h1>'


@app.route('/home', methods=['POST', 'GET'], defaults={'name': 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    session['name'] = name
    return render_template('home.html', name=name, display=False,
                           myList=['one', 'two', 'three', 'four'],
                           Listofdictionaries=[
                               {'name': 'Zach'}, {'name': 'Zoe'}]
                           )


@app.route('/json')
def json():
    if 'name' in session:
        myList = [1, 2, 3, 4]
        name = session['name']
    else:
        name = 'NotInSession'
    return jsonify({"key": "value", "list": [1, 2, 3, 4], "name": name})


@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {}, You are in {} !</h1>'.format(name, location)


@app.route('/theform')
def theform():
    return render_template('form.html')


@app.route('/theform', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']

    # return 'Hello {}.  You are from {}. You have submitted the form!'.format(name, location)
    return redirect(url_for('home', name=name, location=location))


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
    app.run(host='localhost', port=5013)
