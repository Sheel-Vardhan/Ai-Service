# AI Endpoint Response Time Report

## 1. /describe

Input:

```json
{
  "text": "Missing supporting audit evidence"
}
```

Response Time:

- 923 ms

Status:

- Success (200 OK)

Notes:

- AI response generated successfully
- Professional audit summary returned

---

## 2. /recommend

Input:

```json
{
  "text": "Weak internal controls"
}
```

Response Time:

- 748 ms

Status:

- Success (200 OK)

Notes:

- AI-generated recommendations returned successfully
- Response format validated

---

## 3. /analyze

Input:

```json
{
  "text": "Delayed tax compliance reporting"
}
```

Response Time:

- 1.17 seconds

Status:

- Success

---

## 4. /history

Response Time:

- 194 ms

Status:

- Success

---

## 5. /batch-process

Input:

```json
{
  "items": [
    "Missing audit documents",
    "Weak internal controls",
    "Delayed tax filing"
  ]
}
```

Response Time:

- 821 ms

Status:

- Success

---

## 6. /

Frontend UI loaded successfully.

Response Time:

- 1.03 seconds

Status:

- Success

---

# Final QA Summary

All endpoints tested successfully with live Groq API integration.

The system is stable and demo-ready.

No critical failures detected during dry run testing.
