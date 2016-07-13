from flask import Flask
import data
import threading
import time

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Worddddld!"


@app.route("/table")
def table():
    tabela = ''
    for e in data.prices:
        tabela+='''
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </tr>
    ''' % e

    stil = '''
    <style>
        th,tr, td {
            border: 1px solid black;
            border-color: black;
        }
    </style>

    <html>
        <head>
	    <meta http-equiv="refresh" content="5">
	    </head>
        <body>
        <table style="width:100%%";>
          <tr>
            <th>Date</th>
            <th>Symbol</th>
            <th>Price</th>
          </tr>
          %s
        </body>
    </html>
            '''
    return stil % tabela


@app.route("/graph")
def graph():
    return "...graph html..."


@app.route("/getdata")
def getdata():
    data.get_data()
    return "OK\n"


@app.route("/data")
def returndata():
    s = '''
    <html>
	<head>
	<meta http-equiv="refresh" content="5">
	</head>
    <body>
    %r
    </body>
    </html>
    '''
    return s % data.prices


def poller():
    while True:
        data.get_data()
        time.sleep(10)


t = threading.Thread(target=poller)
t.setDaemon(True)
t.start()

if __name__ == "__main__":
    app.run()
