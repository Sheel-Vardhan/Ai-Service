from flask import Blueprint, request, jsonify

describe_bp = Blueprint('describe', __name__)

@describe_bp.route('/describe', methods=['POST'])
def describe():
    data = request.json

    if not data or "text" not in data:
        return jsonify({"error": "Invalid input"}), 400

    return jsonify({
        "message": "Describe endpoint working",
        "input": data["text"]
    })