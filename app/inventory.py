from flask import Blueprint, jsonify

inventory_bp = Blueprint('inventory', __name__)

items = [
    {"id": 1, "name": "Mouse", "quantity": 100},
    {"id": 2, "name": "Keyboard", "quantity": 50}
]

@inventory_bp.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(items)