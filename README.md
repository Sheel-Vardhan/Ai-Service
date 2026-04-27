# AI Service — External Audit Coordinator (Day 1)

## Overview

This is the AI microservice built using Flask for the External Audit Coordinator project.
Day 1 focuses on setting up the project and creating a basic API.

## Tech Stack

* Python 3.11
* Flask
* Flask-CORS

## Setup

```bash
git clone https://github.com/Sheel-Vardhan/Ai-Service.git
cd Ai-Service
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## API Endpoint

**POST /describe**

Request:

```json
{
  "text": "Sample audit issue"
}
```

Response:

```json
{
  "message": "Describe endpoint working",
  "input": "Sample audit issue"
}
```

## Day 1 Completed

* Flask setup
* Project structure created
* Basic `/describe` endpoint

## Next

Day 2 → Groq API integration and prompt design
