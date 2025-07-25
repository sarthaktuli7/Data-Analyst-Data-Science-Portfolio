from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4",  # or use "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content

"""
Provide:
1. What this dataset appears to be.
2. 3 key trends or patterns.
3. Any outliers or anomalies.
4. 3 chart ideas to visualize the data.
"""