from flask import Flask, request, jsonify

from math import sin

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

@app.route("/register", methods=['POST'])
def register()

@app.route("/upload", methods=['POST'])
def upload():
    print('TESTINGINGING')
    username = request.get_json('username')
    password = request.get_json('password')
    print(username, password)
    return 'suh dud'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8855)
