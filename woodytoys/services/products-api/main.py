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

# ### 2. Product Service ###
@app.route('/api/products', methods=['GET'])
def add_product():
    # product = request.json.get('product', '')
    product = request.args.get('product')
    woody.add_product(str(product))
    return str(product) or "none"


@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return "not yet implemented"


@app.route('/api/products/last', methods=['GET'])
def get_last_product():
    # TODO TP9: put in cache ? cache duration ?
    cached_data = redis_db.get('last')
    
    if cached_data:
        last_product = cached_data
    else:
        redis_db.setex('last', 60, woody.get_last_product())
        last_product = redis_db.get('last')
    return f'db: {datetime.now()} - {last_product}'

if __name__ == "__main__":
    woody.launch_server(app, host='0.0.0.0', port=5001)
