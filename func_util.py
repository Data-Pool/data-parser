from sys import argv
from json import dumps
from math import *
from csv import reader

if argv[1] == 'gen':
    data = {}
    func = raw_input('z = ')
    func = func.replace('y', 'z')
    func = eval('lambda x, z: ' + func)
    res = int(raw_input('Resolution: '))
    desc = raw_input('desc')
    p = raw_input('points')
    filename = raw_input('File name:')
    increment = 1.0/(res-1)
    points = ""
    for xi in range(0, int(res)):
        for zi in range(0, int(res)):
            x = xi * increment
            z = zi * increment
            points += (str([x, func(x, z), z])[1:-1]) + '/'
    data['points'] = points[:-1]
    data['res'] = res
    data['desc'] = desc
    if p:
        data['point'] = p
    with open('./'+filename, 'w+') as f:
        f.write(dumps(data))

if argv[1] == 'gen_lin_reg':
    data = {}
    #func = raw_input('c = ')
    #c = (y - (mx + b))**2
    #m = 
    #func = func.replace('y', 'z')
    #func = eval('lambda x, z: ' + func)
    res = int(raw_input('Resolution: '))
    filename = raw_input('File name:')
    increment = 1.0/(res-1)
    x = []
    y = []
    with open('./housing.csv') as f:
        rows = reader(f)
        next(rows)
        for row in rows:
            x.append(float(row[2]))
            y.append(float(row[1]))
        
    points = ""
    for mi in range(0, int(res)):
        for bi in range(0, int(res)):
            m = mi * increment
            b = bi * increment
            c = 0
            for i in range(0, len(x)):
                c += (y[i]-(m*x[i]+b))**2
            c = c/float(len(x))/1e9
            points += (str([m, c, b])[1:-1]) + '/'
    data['points'] = points[:-1]
    data['res'] = res
    with open('./'+filename, 'w+') as f:
        f.write(dumps(data))
