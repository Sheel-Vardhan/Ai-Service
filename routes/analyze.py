from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from datetime import datetime
import json
import os
from utils.logger import logger
from utils.response import success_response, error_response

# ✅ DEFINE BLUEPRINT FIRST
analyze_bp = Blueprint('analyze', __name__)


def load_prompt(file_path, input_text):
    with open(file_path, "r", encoding="utf-8") as f:
        template = f.read()
    return template.replace("{input}", input_text)


# ✅ SMART JSON EXTRACTOR (NEW)
def extract_json(text):
    try:
        return json.loads(text)
    except:
        try:
            start = text.find("{")
            end = text.rfind("}") + 1
            if start != -1 and end != -1:
                return json.loads(text[start:end])
        except:
            pass
    return None


# ✅ SAFE HISTORY SAVE
def save_history(entry):
    try:
        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists("data/history.json"):
            with open("data/history.json", "w") as f:
                json.dump([], f)

        with open("data/history.json", "r") as f:
            data = json.load(f)

    except:
        data = []

    data.append(entry)

    with open("data/history.json", "w") as f:
        json.dump(data, f, indent=2)


@analyze_bp.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

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

        # ✅ DEBUG (IMPORTANT)
        print("RAW DESCRIBE:", describe_response)
        print("RAW RECOMMEND:", recommend_response)

        # ✅ SMART PARSING
        describe_data = extract_json(describe_response)
        if not describe_data:
            logger.error("Describe JSON parsing failed")
            describe_data = {
                "issue_summary": "Error parsing AI response",
                "impact": "Unknown",
                "recommendation": "Retry analysis"
            }

        recommend_data = extract_json(recommend_response)
        if not recommend_data:
            logger.error("Recommend JSON parsing failed")
            recommend_data = {
                "recommendations": []
            }

        # ✅ FORCE STRUCTURE
        combined_data = {
            "issue_summary": describe_data.get("issue_summary", "Not available"),
            "impact": describe_data.get("impact", "Not available"),
            "recommendation": describe_data.get("recommendation", "Not available"),
            "recommendations": recommend_data.get("recommendations", [])
        }

        # Save history
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