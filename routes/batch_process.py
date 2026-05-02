from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
import time

batch_bp = Blueprint("batch", __name__)


@batch_bp.route("/batch-process", methods=["POST"])
def batch_process():

    data = request.get_json()

    # Validate input
    if not data or "items" not in data:
        return jsonify({
            "error": "items array is required"
        }), 400

    items = data["items"]

    # Limit to 20 items
    if len(items) > 20:
        return jsonify({
            "error": "Maximum 20 items allowed"
        }), 400

    results = []

    for item in items:

        text = item.strip()

        # 100ms delay
        time.sleep(0.1)

        try:

            prompt = f"""
            Summarize this audit issue in one short sentence:

            {text}
            """

            ai_response = call_groq(prompt)

            results.append({
                "input": text,
                "output": ai_response
            })

        except Exception as e:

            results.append({
                "input": text,
                "error": str(e)
            })

    return jsonify({
        "count": len(results),
        "results": results
    })