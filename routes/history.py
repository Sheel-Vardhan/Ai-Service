from flask import Blueprint, jsonify
import json

history_bp = Blueprint('history', __name__)

@history_bp.route('/history', methods=['GET'])
def get_history():
    try:
        with open("data/history.json", "r") as f:
            data = json.load(f)
        return jsonify(data)
    except:
        return jsonify([])