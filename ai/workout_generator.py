from groq import Groq
from dotenv import load_dotenv
from rag.retrieval import retrieve_context
import os
import streamlit as st


load_dotenv()

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

def generate_plan(user_profile):

    query = f"""
    Goal: {user_profile['goal']}
    Diet: {user_profile['diet']}
    Equipment: {user_profile['equipment']}
    """

    context = retrieve_context(query)

    prompt = f"""
You are an expert fitness coach and nutritionist.

USER PROFILE:
{user_profile}

RETRIEVED KNOWLEDGE:
{context}

Generate:

1. Personalized Weekly Workout Plan
2. Personalized Indian Diet Plan
3. Daily Protein Recommendation
4. Daily Water Recommendation

Also provide:

WHY THIS WORKOUT WAS CHOSEN
WHY THIS DIET WAS CHOSEN

Keep output professional and well formatted.
"""

    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
