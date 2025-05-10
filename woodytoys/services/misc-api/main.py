import uuid
from datetime import datetime

from flask import Flask, request
from flask_cors import CORS

import woody

import redis

app = Flask('my_api')
cors = CORS(app)

redis_db = redis.Redis(host='redis', port=6379, db=0)


@app.get('/api/ping')
def ping():
    return 'ping'


# ### 1. Misc service ### (note: la traduction de miscellaneous est 'divers'
@app.route('/api/misc/time', methods=['GET'])
def get_time():
    return f'misc: {datetime.now()}'


@app.route('/api/misc/heavy', methods=['GET'])
def get_heavy():
    # TODO TP9: cache ?
    name = request.args.get('name')
    r = woody.make_some_heavy_computation(name)
    # on rajoute la date pour pas que le resultat ne soit mis en cache par le browser
    return f'{datetime.now()}: {r}'


if __name__ == "__main__":
    woody.launch_server(app, host='0.0.0.0', port=5000)
