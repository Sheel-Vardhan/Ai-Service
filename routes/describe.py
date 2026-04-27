from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from datetime import datetime

describe_bp = Blueprint('describe', __name__)

def load_prompt(input_text):
    with open("prompts/describe_prompt.txt", "r") as f:
        template = f.read()
    return template.replace("{input}", input_text)

@describe_bp.route('/describe', methods=['POST'])
def describe():
    data = request.json

    # Input validation
    if not data or "text" not in data:
        return jsonify({"error": "Invalid input"}), 400

    user_input = data["text"].strip()

    if len(user_input) < 5:
        return jsonify({"error": "Input too short"}), 400

    # Load prompt
    prompt = load_prompt(user_input)

    # Call AI
    ai_response = call_groq(prompt)

    return jsonify({
        "generated_at": datetime.utcnow().isoformat(),
        "model_used": "llama-3.3-70b",
        "description": ai_response
    })