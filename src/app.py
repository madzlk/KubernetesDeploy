from flask import Flask, render_template
import socket

def fetchDetails():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return str(host_name), str(host_ip)

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/details')
def details():
    name, ip = fetchDetails()
    return render_template('index.html', hostname=name, IP=ip)
 
if __name__ == '__main__':

    app.run()