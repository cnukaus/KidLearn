""""""

import flask
import socket

def increment_ascii(string):
    if not isinstance(string, str):
        raise TypeError("Expected <class 'str'>, got {}".format(type(string)))
    ret = list()
    for char in string:
        try:
            char = chr(ord(char) + 1)
        except ValueError:
            pass
        ret.append(char)
    return ''.join(ret)

def reverse_ascii(string):
    if not isinstance(string, str):
        raise TypeError("Expected <class 'str'>, got {}".format(type(string)))
    ret = list()
    for char in string:
        try:
            char = chr(ord(char) - 1)
        except ValueError:
            pass
        ret.append(char)
    return ''.join(ret)

app = flask.Flask('app')

@app.route('/')
def this():
    print('in this')
    return '<form action="/addRegion" method="post">Eval:<br><textarea name="teval" style="height:100px;width:500px;"></textarea><br><input type="submit" value="Submit"></form>'
    # internally:
    # flask.Response('<string>')

@app.route('/addRegion', methods=['POST'])
def any_func_name_but_this():
    f = (flask.request.form['teval'])
    resp = flask.Response(increment_ascii(f))
    resp.headers['Content-Type'] = 'text/plain'
    return resp

@app.route('/login', methods=['GET','POST'])
def login():
    if flask.request.method == "POST":
        username = flask.request.form['user']
        password = flask.request.form['pass']
        print(username, password)
        return 'done'
    return '<form action="/login" method="post"><label for="user">UN:</label><input name="user"><br><label for="pass">PW:</label><input name="pass" type="password"><br><input type="submit" value="Submit"></form>'
if __name__ == '__main__':
    print('IPs:', *socket.gethostbyaddr(socket.gethostname())[2])
    app.run(host='0.0.0.0', port=80)