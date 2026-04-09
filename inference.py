import os
from openai import OpenAI

client = OpenAI(base_url=os.getenv("API_BASE_URL"))
MODEL = os.getenv("MODEL_NAME", "gpt-4o-mini")

def predict(email: str):
    prompt = f"""
    Classify this email into one of: spam, important, normal.
    Email: {email}
    Answer only one word.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip().lower()
