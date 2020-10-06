import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from flask import Flask, jsonify, make_response, Blueprint
from DataBaseCrud.database_crud import DataBaseCrud

product_all = Blueprint('product_all', __name__)


@product_all.route('/api/products', methods=['GET'])
def index():
    """
    Get all products
    swagger_from_file: Contract.index.yml
    :return:
    """
    crud = DataBaseCrud()
    products = crud.get_all()
    return make_response(jsonify({'products': products}), 200)
