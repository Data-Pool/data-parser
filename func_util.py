from sys import argv
from json import dumps

if argv[1] == 'gen':
    data = {}
    func = raw_input('z = ')
    func = func.replace('y', 'z')
    func = eval('lambda x, z: ' + func)
    res = int(raw_input('Resolution: '))
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
    with open('./'+filename, 'w+') as f:
        f.write(dumps(data))

