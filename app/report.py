from flask import Blueprint, jsonify

report_bp = Blueprint('report', __name__)

@report_bp.route('/report', methods=['GET'])
def report():
    return jsonify({"total_items": 150, "out_of_stock": 2})