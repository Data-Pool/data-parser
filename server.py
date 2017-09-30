from flask import Flask, request, jsonify
from os import path, makedirs
from bcrypt import hashpw, checkpw, gensalt
from math import *

app = Flask(__name__)

@app.route("/")
def root():
    res = request.args['res']
    res = float(res)
    payload = {}
    payload['res'] = res
    increment = 1.0/float((res-1))
    points = ""
    for x in range(0, int(res)):
        for z in range(0, int(res)):
            points += (str([x*increment, (x*increment)**2, z*increment])[1:-1]) + '/'
    payload['points'] = points[:-1]
    return jsonify(payload)

@app.route("/t")
def test():
    res = request.args['res']
    res = float(res)
    payload = {}
    payload['res'] = res
    func = request.args['func'][4:-1]
    func = func.replace('y', 'z')
    func = eval('lambda x, z: ' + func)
    increment = 1.0/(res-1)
    points = ""
    for xi in range(0, int(res)):
        for zi in range(0, int(res)):
            x = xi * increment
            z = zi * increment
            points += (str([x, func(x, z), z])[1:-1]) + '/'
    payload['points'] = points[:-1]
    return jsonify(payload)

def validate_user(username, password):
    if not path.isdir('./user/'+username):
        return False
    with open('./user/'+username+'/.pass') as f:
        p = f.readline().strip('\n')
        if checkpw(password.encode('utf8'), p.encode('utf8')):
            return True
        return False

@app.route("/register", methods=['POST'])
def register():
    username = request.get_json()['username']
    password = request.get_json()['password']
    if path.isdir('./user/'+username):
        return("User " + username + " already exists")
    makedirs('./user/'+username)
    with open('./user/'+username+'/.pass', 'w+') as f:
        f.write(hashpw(password.encode('utf8'), gensalt()).decode('utf8') + '\n')
    return "User created"

@app.route("/upload", methods=['POST'])
def upload():
    username = request.get_json()['username']
    password = request.get_json()['password']
    login = validate_user(username, password) 
    if not login:
        return("Incorrect username and/or password")
    return('suh dud ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8855)
