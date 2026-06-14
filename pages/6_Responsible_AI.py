import streamlit as st

st.title("🛡 Responsible AI")

st.header("How Recommendations Are Generated")

st.write("""
FitGenAI uses Retrieval-Augmented Generation (RAG).

User Profile
→ Knowledge Retrieval
→ Groq LLM
→ Personalized Recommendation
""")

st.header("Data Privacy")

st.write("""
No personal data is permanently stored.
Only information required to generate recommendations is processed.
""")

st.header("AI Limitations")

st.write("""
Recommendations are based on available knowledge base data.
They may not account for medical conditions.
""")

st.header("Medical Disclaimer")

st.warning("""
FitGenAI provides fitness and nutrition guidance only.

It does not replace advice from doctors,
dietitians, or certified fitness professionals.
""")