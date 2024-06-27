import os
import requests
import streamlit as st
from streamlit_chat import message

st.set_page_config(
    page_title="Hospital System Chatbot",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)

CHATBOT_URL = os.getenv("CHATBOT_URL", "http://localhost:8000/hospital-rag-agent")

# Custom CSS for styling
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #F0F2F6;
        padding: 20px;
    }
    .sidebar .sidebar-content h2 {
        font-family: 'Arial', sans-serif;
        color: #4CAF50;
    }
    .sidebar .sidebar-content p, .sidebar .sidebar-content li {
        font-family: 'Arial', sans-serif;
        color: #333333;
    }
    .main .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("About 💡")
    st.markdown(
        """
        This chatbot interfaces with a
        [LangChain](https://python.langchain.com/docs/get_started/introduction)
        agent designed to answer questions about the hospitals, patients,
        visits, physicians, and insurance payers in a fake hospital system.
        The agent uses retrieval-augment generation (RAG) over both
        structured and unstructured data that has been synthetically generated.
        """
    )

    st.header("Example Questions 📋")
    example_questions = [
        "Which hospitals are in the hospital system?",
        "What is the current wait time at Wallace-Hamilton hospital?",
        "At which hospitals are patients complaining about billing and insurance issues?",
        "What is the average duration in days for closed emergency visits?",
        "What are patients saying about the nursing staff at Castaneda-Hardy?",
        "What was the total billing amount charged to each payer for 2023?",
        "What is the average billing amount for Medicaid visits?",
        "Which physician has the lowest average visit duration in days?",
        "How much was billed for patient 789's stay?",
        "Which state had the largest percent increase in Medicaid visits from 2022 to 2023?",
        "What is the average billing amount per day for Aetna patients?",
        "How many reviews have been written from patients in Florida?",
        "For visits that are not missing chief complaints, what percentage have reviews?",
        "What is the percentage of visits that have reviews for each hospital?",
        "Which physician has received the most reviews for their visits?",
        "What is the ID for physician James Cooper?",
        "List every review for visits treated by physician 270. Don't leave any out."
    ]
    for question in example_questions:
        st.markdown(f"- {question}")

st.title("🏥 Hospital System Chatbot")
st.info(
    "Ask me questions about patients, visits, insurance payers, hospitals, "
    "physicians, reviews, and wait times!"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if "output" in message.keys():
            st.markdown(message["output"])

        if "explanation" in message.keys():
            with st.expander("How was this generated"):
                st.info(message["explanation"])

if prompt := st.chat_input("What do you want to know?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "output": prompt})

    data = {"text": prompt}

    with st.spinner("Searching for an answer..."):
        response = requests.post(CHATBOT_URL, json=data)

        if response.status_code == 200:
            output_text = response.json()["output"]
            explanation = response.json()["intermediate_steps"]
        else:
            output_text = """An error occurred while processing your message.
            Please try again or rephrase your message."""
            explanation = output_text

    st.chat_message("assistant").markdown(output_text)
    with st.expander("How was this generated"):
        st.info(explanation)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "output": output_text,
            "explanation": explanation,
        }
    )
