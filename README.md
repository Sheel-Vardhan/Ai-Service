# 🚀 AI Service — External Audit Coordinator

## 📌 Overview

AI Service is a Flask-based AI-powered backend application designed to assist in external audit processes. The system analyzes audit issues and generates structured insights, impacts, and actionable recommendations using AI.

The project supports:

- AI-powered audit analysis
- Recommendation generation
- Batch processing
- History tracking
- REST API integration

---

# 🗓️ Development Progress

## ✅ Day 1 — Project Setup

- Initialized Flask backend application
- Created basic `/describe` API endpoint
- Organized project structure (`routes`, `services`, `prompts`)
- Tested API using Postman

---

## ✅ Day 2 — AI Integration

- Integrated Groq API for AI-powered responses
- Implemented prompt-based response generation
- Created dynamic prompt loading from file
- Generated structured audit descriptions

Generated fields:

- Issue Summary
- Impact
- Recommendation

---

## ✅ Day 3 — Structured API Response

- Converted AI output into structured JSON format
- Implemented JSON parsing of AI responses
- Added error handling and validation
- Improved API response format for frontend integration

### Example Response

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

## ✅ Day 4 — Recommendation Engine

- Built `/recommend` API endpoint
- Generated actionable recommendations
- Designed prompt for list-based AI output
- Returned structured recommendation list

### Example Response

```json
{
  "status": "success",
  "data": {
    "recommendations": ["...", "...", "..."]
  }
}
```

---

## ✅ Day 5 — Combined Analysis Endpoint

- Created `/analyze` API endpoint
- Integrated describe + recommendation logic
- Combined outputs into a single response

### Example Response

```json
{
  "status": "success",
  "data": {
    "issue_summary": "...",
    "impact": "...",
    "recommendation": "...",
    "recommendations": ["...", "..."]
  }
}
```

---

## ✅ Day 6 — AI Prompt Optimization

- Improved prompt engineering
- Added better AI response formatting
- Enhanced response consistency

---

## ✅ Day 7 — Frontend Integration

- Built frontend UI using HTML, CSS, and JavaScript
- Connected frontend with Flask APIs
- Displayed AI-generated outputs dynamically

---

## ✅ Day 8 — History Tracking

- Added history storage using `history.json`
- Created `/history` API endpoint
- Displayed previous analysis records

---

## ✅ Day 9 — Deployment Preparation

- Improved API stability
- Added validation and logging
- Prepared project for deployment

---

## ✅ Day 10 — Production Improvements

- Added error handling
- Added response validation
- Improved AI response parsing
- Deployed application on Render

---

## ✅ Day 11 — Batch Processing API

- Built `/batch-process` API endpoint
- Added support for processing multiple audit issues
- Added validation for maximum 20 items
- Added delayed batch processing (100ms delay)

### Example Response

```json
{
  "count": 2,
  "results": [
    {
      "input": "Missing audit documents",
      "output": "..."
    },
    {
      "input": "Delayed tax filing",
      "output": "..."
    }
  ]
}
```

---

# 📂 Project Structure

```bash
ai-service/
│
├── app.py
├── README.md
├── requirements.txt
├── .env
│
├── routes/
│   ├── describe.py
│   ├── recommend.py
│   ├── analyze.py
│   ├── history.py
│   └── batch_process.py
│
├── services/
│   └── groq_client.py
│
├── prompts/
│   ├── describe_prompt.txt
│   └── recommend_prompt.txt
│
├── templates/
│   └── index.html
│
├── utils/
│   ├── logger.py
│   └── response.py
│
└── data/
    └── history.json
```

---

# ⚙️ Prerequisites

Before running the project, ensure you have:

- Python 3.10 or above
- pip
- Git
- Groq API Key

---

# 🛠️ Setup Instructions

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd ai-service
```

---

## 2. Create Virtual Environment

```bash
python -m venv myenv
```

---

## 3. Activate Virtual Environment

### Windows

```bash
myenv\Scripts\activate
```

### Mac/Linux

```bash
source myenv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root.

Example:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

Application runs on:

```plaintext
http://localhost:5000
```

---

# 🔗 Full API Reference

---

## 1. POST `/describe`

Generates structured audit issue description.

### Request

```json
{
  "text": "Missing audit documents"
}
```

### Response

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

## 2. POST `/recommend`

Generates actionable recommendations.

### Request

```json
{
  "text": "Weak internal controls"
}
```

### Response

```json
{
  "status": "success",
  "data": {
    "recommendations": ["...", "...", "..."]
  }
}
```

---

## 3. POST `/analyze`

Combines issue analysis and recommendations.

### Request

```json
{
  "text": "Delayed tax filing"
}
```

### Response

```json
{
  "status": "success",
  "data": {
    "issue_summary": "...",
    "impact": "...",
    "recommendation": "...",
    "recommendations": ["...", "..."]
  }
}
```

---

## 4. GET `/history`

Returns previous analysis history.

### Response

```json
[
  {
    "input": "...",
    "output": {},
    "timestamp": "..."
  }
]
```

---

## 5. POST `/batch-process`

Processes multiple audit issues in batch.

### Request

```json
{
  "items": ["Missing audit documents", "Delayed tax filing"]
}
```

### Response

```json
{
  "count": 2,
  "results": [
    {
      "input": "...",
      "output": "..."
    }
  ]
}
```

---

# ⚠️ Error Handling

Common API errors:

- Invalid input
- Missing required fields
- Maximum batch size exceeded
- AI response parsing failure

---

# 🚀 Deployment

The application is deployed on Render.

---

# 🔮 Future Improvements

- Database integration
- Authentication system
- PDF report generation
- Advanced AI scoring
- Dashboard analytics

---

# 🎯 Status

✅ Day 1 Completed  
✅ Day 2 Completed  
✅ Day 3 Completed  
✅ Day 4 Completed  
✅ Day 5 Completed  
✅ Day 6 Completed  
✅ Day 7 Completed  
✅ Day 8 Completed  
✅ Day 9 Completed  
✅ Day 10 Completed  
✅ Day 11 Completed

🚀 Project Ready for Production Use
