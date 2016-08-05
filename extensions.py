from flask import Flask
from flask import request
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello World!</h1>\n<p>Your browser is %s</p>' % user_agent

@app.route('/user/<name>')
def user(name):
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello, {0}!</h1>\n<p>Your browser is {1}</p>'.format(name, user_agent)

if __name__ == '__main__':
    manager.run()