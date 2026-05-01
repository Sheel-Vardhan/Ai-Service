from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from datetime import datetime
import json
from utils.logger import logger
from utils.response import success_response, error_response

analyze_bp = Blueprint('analyze', __name__)


def load_prompt(file_path, input_text):
    with open(file_path, "r") as f:
        template = f.read()
    return template.replace("{input}", input_text)


# 🔥 NEW FUNCTION: Save history
def save_history(entry):
    try:
        with open("data/history.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open("data/history.json", "w") as f:
        json.dump(data, f, indent=2)


@analyze_bp.route('/analyze', methods=['POST'])
def analyze():
    data = request.json

    if not data or "text" not in data:
        return jsonify(error_response("Invalid input")), 400

    user_input = data["text"].strip()

    if len(user_input) < 5:
        return jsonify(error_response("Input too short")), 400

    try:
        logger.info(f"Processing input: {user_input}")

        # Load prompts
        describe_prompt = load_prompt("prompts/describe_prompt.txt", user_input)
        recommend_prompt = load_prompt("prompts/recommend_prompt.txt", user_input)

        # Call AI
        describe_response = call_groq(describe_prompt)
        recommend_response = call_groq(recommend_prompt)

        # Parse responses
        describe_data = json.loads(describe_response)
        recommend_data = json.loads(recommend_response)

        # Combine results
        combined_data = {
            "issue_summary": describe_data.get("issue_summary"),
            "impact": describe_data.get("impact"),
            "recommendation": describe_data.get("recommendation"),
            "recommendations": recommend_data.get("recommendations", [])
        }

        # 🔥 SAVE HISTORY
        history_entry = {
            "input": user_input,
            "output": combined_data,
            "timestamp": datetime.utcnow().isoformat()
        }
        save_history(history_entry)

        logger.info("Successfully generated analysis")

        return jsonify({
            **success_response(combined_data),
            "generated_at": datetime.utcnow().isoformat()
        })

    except Exception as e:
        logger.error(f"Error: {str(e)}")

        return jsonify(error_response("Failed to analyze input")), 500