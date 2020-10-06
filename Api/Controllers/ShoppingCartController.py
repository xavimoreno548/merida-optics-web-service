import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from flask import Flask, request, jsonify, make_response, Blueprint
from DataBaseCrud.database_crud import DataBaseCrud

shopping_cart = Blueprint('shopping_cart', __name__)


@shopping_cart.route('/api/product/items', methods=['GET'])
def cart_items():
    products = request.json['products']
    crud = DataBaseCrud()
    items = []
    for key in products:
        element = crud.show(key)
        if not element:
            return make_response(jsonify({'error': 'product dont\' exist'}), 406)
        items.append(element)
    return make_response(jsonify({'products': items}), 200)
