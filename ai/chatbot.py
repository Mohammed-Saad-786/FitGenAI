from groq import Groq
from dotenv import load_dotenv
from rag.retrieval import retrieve_context
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_coach(question):

    context = retrieve_context(question)

    prompt = f"""
You are FitGenAI Coach.

Knowledge:
{context}

User Question:
{question}

Answer professionally.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content