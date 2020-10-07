import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from flask import Flask, jsonify, make_response, Blueprint
from DataBaseCrud.database_crud import DataBaseCrud

seeder_product = Blueprint('seeder_product', __name__)

@seeder_product.route('/add', methods=['GET'])
def add_data():
    crud = DataBaseCrud()
    products = request.json['products']
    for p in products:
        crud.add_products(p)
    return make_response(jsonify({'status': 'ok'}), 200)