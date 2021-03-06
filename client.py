from sys import argv, exit
from requests import post
from json import dumps
from getpass import getpass

if argv[1] == 'upload':
    if len(argv) < 3:
        print('Upload file must be specified')
        exit()
    payload = {'username': 'user', 'password': 'pass'}
    headers = {'Content-Type': 'application/json'}
    payload['username'] = raw_input('username:')
    payload['password'] = getpass('password:')
    with open('./' + argv[2]) as f:
        lines = f.readlines()
    text = ''
    for line in lines:
        text += line
    payload['text'] = text
    payload['filename'] = argv[2]
    r = post('http://kerlin.tech:8855/upload', data=dumps(payload), headers=headers)
    print(r.text)

if argv[1] == 'register':
    payload = {'username': 'user', 'password': 'pass'}
    headers = {'Content-Type': 'application/json'}
    payload['username'] = raw_input('username:')
    payload['password'] = getpass('password:')
    headers = {'Content-Type': 'application/json'}
    r = post('http://kerlin.tech:8855/register', data=dumps(payload), headers=headers)
    print(r.text)
