from groq import Groq
from dotenv import load_dotenv
from rag.retrieval import retrieve_context
import os
import streamlit as st


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    api_key = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=api_key)

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
