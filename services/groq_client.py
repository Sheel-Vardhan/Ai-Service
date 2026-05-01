import os
from groq import Groq
from dotenv import load_dotenv
from functools import lru_cache   # 👈 ADD THIS

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@lru_cache(maxsize=50)   # 👈 ADD THIS (caching)
def call_groq(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=300
        )
        return response.choices[0].message.content

    except Exception as e:
        print("Groq Error:", e)
        return """{
            "issue_summary": "Unable to generate response",
            "impact": "AI service temporarily unavailable",
            "recommendation": "Please try again later"
        }"""