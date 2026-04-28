# 🚀 AI Service — External Audit Coordinator

## 📌 Overview

This project is an AI-powered backend service designed to assist in external audit processes. It analyzes audit issues and generates structured descriptions along with actionable recommendations using AI.

---

# 🗓️ Day 1 — Project Setup

* Initialized Flask backend application
* Created basic `/describe` API endpoint
* Organized project structure (`routes`, `services`, `prompts`)
* Tested API using Postman

---

# 🧠 Day 2 — AI Integration

* Integrated **Groq API** for AI-powered responses
* Implemented prompt-based response generation
* Created dynamic prompt loading from file
* Generated structured audit descriptions:

  * Issue Summary
  * Impact
  * Recommendation

---

# ⚙️ Day 3 — Structured API Response

* Converted AI output into **structured JSON format**
* Implemented JSON parsing of AI responses
* Added error handling and validation
* Improved API response format for frontend integration

### Example Response:

```json
{
  "status": "success",
  "data": {
    "issue_summary": "...",
    "impact": "...",
    "recommendation": "..."
  }
}
```

---

# 💡 Day 4 — Recommendation Engine

* Built `/recommend` API endpoint
* Generated multiple actionable recommendations
* Designed prompt for list-based AI output
* Returned structured list of recommendations

### Example Response:

```json
{
  "status": "success",
  "data": {
    "recommendations": [
      "...",
      "...",
      "..."
    ]
  }
}
```

---

# 🔗 Day 5 — Combined Analysis Endpoint

* Created `/analyze` API endpoint
* Integrated both `/describe` and `/recommend` logic
* Combined outputs into a single response
* Built end-to-end AI audit assistant workflow

### Example Response:

```json
{
  "status": "success",
  "data": {
    "issue_summary": "...",
    "impact": "...",
    "recommendation": "...",
    "recommendations": [
      "...",
      "..."
    ]
  }
}
```

---

# 📂 Project Structure

```bash
ai-service/
│── app.py
│── routes/
│   ├── describe.py
│   ├── recommend.py
│   └── analyze.py
│── services/
│   └── groq_client.py
│── prompts/
│   ├── describe_prompt.txt
│   └── recommend_prompt.txt
│── requirements.txt
│── README.md
```

---

# 🔗 API Endpoints

## 1. POST `/describe`

Generates structured audit description

## 2. POST `/recommend`

Generates multiple recommendations

## 3. POST `/analyze`

Combines description + recommendations

---

# ▶️ Run the Project

```bash
pip install -r requirements.txt
python app.py
```

---

# ⚠️ Notes

* `.env` file is excluded for security
* Groq API key is required
* Ensure dependencies are installed

---

# 🎯 Status

✔ Day 1 Completed
✔ Day 2 Completed
✔ Day 3 Completed
✔ Day 4 Completed
✔ Day 5 Completed

🚀 Project Ready for Demo / Deployment
