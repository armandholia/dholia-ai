import os
import streamlit as st
from memory_manager import process_files
from chat_engine import get_response

os.environ["LANGCHAIN_CALLBACKS_DISABLED"] = "true"

st.set_page_config(page_title="Dholia — Your Second Brain")
st.title("🧠 Dholia: Talk to Your Memory")

uploaded_files = st.file_uploader("Upload documents (PDF or TXT)", type=["pdf", "txt"], accept_multiple_files=True)

if uploaded_files:
    process_files(uploaded_files)
    st.success("✅ Files embedded into Dholia's memory!")

query = st.text_input("Ask your AI clone:")
if query:
    answer = get_response(query)
    st.markdown("🧠 **Dholia says:**")
    st.write(answer)
