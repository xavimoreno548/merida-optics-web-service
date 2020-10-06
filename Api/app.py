import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from flask import Flask, request, jsonify, make_response
from DataBaseCrud.database_crud import DataBaseCrud
from Api.Controllers.IndexController import product_all
from Api.Controllers.ProductShowController import product_show
from Api.Controllers.ProductPurchaseController import product_purchase
from Api.Controllers.ShoppingCartController import shopping_cart
from Api.Controllers.ContractController import contract

app = Flask(__name__)

app.register_blueprint(product_all)
app.register_blueprint(product_show)
app.register_blueprint(product_purchase)
app.register_blueprint(shopping_cart)
app.register_blueprint(contract)


@app.route('/', methods=['GET'])
def index():
    return make_response(jsonify({'optica_merida':'web_service'}), 200)


if __name__ == "__main__":
    app.run(debug=True)
