import streamlit as st
from ai.chatbot import ask_coach

st.title("🤖 AI Fitness Coach")

question = st.text_input(
    "Ask a fitness question"
)

if st.button("Ask Coach"):

    with st.spinner("Thinking..."):

        answer = ask_coach(question)

    st.success("Answer")

    st.write(answer)