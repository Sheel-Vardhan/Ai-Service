from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from datetime import datetime
import json

analyze_bp = Blueprint('analyze', __name__)

def load_prompt(file_path, input_text):
    with open(file_path, "r") as f:
        template = f.read()
    return template.replace("{input}", input_text)

@analyze_bp.route('/analyze', methods=['POST'])
def analyze():
    data = request.json

    if not data or "text" not in data:
        return jsonify({"status": "error", "message": "Invalid input"}), 400

    user_input = data["text"].strip()

    if len(user_input) < 5:
        return jsonify({"status": "error", "message": "Input too short"}), 400

    try:
        # Load prompts
        describe_prompt = load_prompt("prompts/describe_prompt.txt", user_input)
        recommend_prompt = load_prompt("prompts/recommend_prompt.txt", user_input)

        # Call AI twice
        describe_response = call_groq(describe_prompt)
        recommend_response = call_groq(recommend_prompt)

        # Parse JSON
        describe_data = json.loads(describe_response)
        recommend_data = json.loads(recommend_response)

        # Combine results
        return jsonify({
            "status": "success",
            "generated_at": datetime.utcnow().isoformat(),
            "model_used": "llama-3.3-70b",
            "data": {
                "issue_summary": describe_data.get("issue_summary"),
                "impact": describe_data.get("impact"),
                "recommendation": describe_data.get("recommendation"),
                "recommendations": recommend_data.get("recommendations", [])
            }
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Failed to analyze input",
            "error": str(e)
        }), 500