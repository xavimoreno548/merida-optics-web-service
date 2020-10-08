import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from flask import Flask, jsonify, make_response, Blueprint
from DataBaseCrud.database_crud import DataBaseCrud

product_show = Blueprint('product_show', __name__)


@product_show.route('/api/product/<id>', methods=['GET'])
def show(id: int):
    crud = DataBaseCrud()
    product = crud.show(id)
    if not product:
        return make_response(jsonify({'error': 'El producto no existe'}), 406)
    return make_response(jsonify({'data':{'product': product}}), 200)
