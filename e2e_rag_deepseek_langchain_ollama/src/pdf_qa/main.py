import streamlit as st
from document_processing import process_uploaded_pdf
from ui_components import configure_custom_css
from chat_engine import generate_response, PROMPT_TEMPLATE

# Custom CSS styling
configure_custom_css()

st.title("📘 DocuMind AI")
st.markdown("### Your Intelligent Document Assistant")
st.markdown("---")

# File Upload Section
uploaded_pdf = st.file_uploader(
    "Upload Research Document (PDF)",
    type="pdf",
    help="Select a PDF document for analysis",
    accept_multiple_files=False
)

if uploaded_pdf:
    raw_docs, processed_chunks = process_uploaded_pdf(uploaded_pdf)

    st.success("✅ Document processed successfully! Ask your questions below.")

    user_input = st.chat_input("Enter your question about the document...")

    if user_input:
        with st.chat_message("user"):
            st.write(user_input)

        with st.spinner("Analyzing document..."):
            ai_response = generate_response(user_input, processed_chunks, PROMPT_TEMPLATE)

        with st.chat_message("assistant", avatar="🤖"):
            st.write(ai_response)
