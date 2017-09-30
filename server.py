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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8855)
