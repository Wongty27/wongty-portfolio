import streamlit as st
from models.llm import csv_agent

st.subheader("LLM powered by Gemini")

with st.form("my_form"):
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "pdf"])
    user_question = st.text_input(label="Ask a question:")
    submitted = st.form_submit_button(label="Start")
    if uploaded_file and user_question and submitted:
        try:
            ai_response = csv_agent(input_file=uploaded_file, question=user_question)
            st.write(ai_response)

        except Exception as e:
            st.write(e)

    elif uploaded_file and not user_question:
        st.write("Please upload a file and ask a question.")



