# 🎤 AI Service Demo Script

## Introduction (1 Minute)

Hello everyone.

Today I will demonstrate our AI-powered External Audit Coordinator service.

This system helps analyze audit-related issues and generates professional summaries, impacts, and recommendations using AI.

The application is built using:

- Flask
- Groq AI API
- ChromaDB
- REST APIs

The system supports:

- Audit issue analysis
- AI recommendations
- Batch processing
- History tracking
- Knowledge base integration

Now I will demonstrate the APIs step by step.

---

# Demo 1 — Describe API

## What I will say

"First, I will demonstrate the describe endpoint which analyzes an audit issue and generates a professional summary."

## API

POST `/describe`

## Input

```json
{
  "text": "Missing audit evidence for financial transactions"
}
```

## Expected Output

```json
{
  "status": "success",
  "data": {
    "issue_summary": "Missing audit evidence for financial transactions",
    "impact": "Lack of supporting evidence may reduce audit reliability and increase compliance risks.",
    "recommendation": "Ensure all financial transactions are supported with proper audit documentation."
  }
}
```

---

# Demo 2 — Recommendation API

## What I will say

"Now I will generate AI-powered recommendations for an audit issue."

## API

POST `/recommend`

## Input

```json
{
  "text": "Weak internal controls"
}
```

## Expected Output

```json
{
  "status": "success",
  "data": {
    "recommendations": [
      "Strengthen approval workflows",
      "Implement segregation of duties",
      "Conduct regular internal audits"
    ]
  }
}
```

---

# Demo 3 — Analyze API

## What I will say

"This endpoint combines audit analysis and recommendations into one complete AI response."

## API

POST `/analyze`

## Input

```json
{
  "text": "Delayed submission of tax compliance reports"
}
```

## Expected Output

```json
{
  "status": "success",
  "data": {
    "issue_summary": "Delayed submission of tax compliance reports",
    "impact": "May lead to penalties and regulatory risks.",
    "recommendation": "Implement compliance tracking processes.",
    "recommendations": [
      "Assign compliance owners",
      "Create submission reminders",
      "Perform regular compliance reviews"
    ]
  }
}
```

---

# Demo 4 — Batch Processing API

## What I will say

"Now I will demonstrate batch processing where multiple audit issues are analyzed together."

## API

POST `/batch-process`

## Input

```json
{
  "items": [
    "Missing audit documents",
    "Weak internal controls",
    "Delayed tax filing"
  ]
}
```

## Expected Output

```json
{
  "count": 3,
  "results": [
    {
      "input": "Missing audit documents",
      "output": "..."
    },
    {
      "input": "Weak internal controls",
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

# Demo 5 — History API

## What I will say

"This endpoint stores and returns previous audit analysis history."

## API

GET `/history`

## Expected Output

```json
[
  {
    "input": "Delayed tax filing",
    "timestamp": "..."
  }
]
```

---

# Demo 6 — ChromaDB Knowledge Base

## What I will say

"We also integrated ChromaDB to store audit-related domain knowledge documents for future semantic search and intelligent retrieval."

Stored topics include:

- Tax compliance
- Internal controls
- Audit evidence
- Risk assessments
- Cybersecurity controls

---

# Closing

## What I will say

"This concludes the demonstration of our AI-powered External Audit Coordinator system.

The platform successfully provides intelligent audit analysis, recommendations, batch processing, and scalable AI integration.

Thank you."
