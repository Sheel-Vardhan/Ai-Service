from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from datetime import datetime
import json

describe_bp = Blueprint('describe', __name__)

def load_prompt(input_text):
    with open("prompts/describe_prompt.txt", "r") as f:
        template = f.read()
    return template.replace("{input}", input_text)

@describe_bp.route('/describe', methods=['POST'])
def describe():
    data = request.json

    # Validation
    if not data or "text" not in data:
        return jsonify({"status": "error", "message": "Invalid input"}), 400

    user_input = data["text"].strip()

    if len(user_input) < 5:
        return jsonify({"status": "error", "message": "Input too short"}), 400

    try:
        prompt = load_prompt(user_input)
        ai_response = call_groq(prompt)

        # Convert AI JSON string → Python dict
        parsed_response = json.loads(ai_response)

        return jsonify({
            "status": "success",
            "generated_at": datetime.utcnow().isoformat(),
            "model_used": "llama-3.3-70b",
            "data": parsed_response
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Failed to process request",
            "error": str(e)
        }), 500