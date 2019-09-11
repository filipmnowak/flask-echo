import os
from elasticapm.contrib.flask import ElasticAPM
from flask import Flask
from flask import request
from pprint import pformat


app = Flask(__name__)
apm = ElasticAPM(app)


@app.route("/", defaults={'path': ''}, methods=['GET', 'POST', 'HEAD'])
@app.route('/<path:path>', methods=['GET', 'POST', 'HEAD'])
def echo(path):
    try:
        return pformat(request.__dict__), 200, {'Content-Type': 'text/plain'}
    except Exception as e:
        return e

if __name__ == "__main__":
    _host = os.getenv('ECHO_HOST') or '0.0.0.0'
    _port = int(os.getenv('ECHO_PORT') or '8080')
    app.run(host=_host, port=_port)
