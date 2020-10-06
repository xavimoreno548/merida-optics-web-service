import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from flask import Flask, Blueprint, render_template

contract = Blueprint('contract', __name__)


@contract.route("/api/info/contract")
def spec():
    print('sending docs')
    return render_template('swaggerui.html')
