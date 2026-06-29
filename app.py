import streamlit as st

from src.agent import chat

st.set_page_config(
    page_title="Personal AI Assistant",
    page_icon="🤖"
)

st.title("🤖 Personal AI Assistant")

st.write("Welcome Rohit!")

user_input = st.text_input(
    "Ask anything"
)

if st.button("Send"):

    if user_input:

        response = chat(user_input)

        st.markdown("### Assistant")

        st.write(response)