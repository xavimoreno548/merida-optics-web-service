import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from flask import Flask, request, jsonify, make_response, Blueprint
from DataBaseCrud.database_crud import DataBaseCrud

product_purchase = Blueprint('product_purchase', __name__)


@product_purchase.route('/api/products/buy', methods=['POST'])
def buy_product():
    products = request.json['products']
    crud = DataBaseCrud()
    for product in products:
        result = crud.remove(product['id'], product['amount'])
        if not result:
            return make_response(jsonify({'error': 'El producto no existe, o no hay la cantidad requerida'}), 406)
    return make_response(jsonify({'status': 'ok', 'message': 'Compra satisfactoria'}), 200)
