import streamlit as st
from chat_engine import ChatEngine
from ui_components import configure_sidebar, configure_custom_css
from prompt_builder import build_prompt_chain

# Custom CSS styling
configure_custom_css()

st.title("🧠 DeepSeek AI")
st.caption("🚀 AI Assistant")

# Sidebar configuration
selected_model = configure_sidebar()

# Initialize chat engine
chat_engine = ChatEngine(model=selected_model)

# Session state management
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]

# Chat container
chat_container = st.container()

# Display chat messages
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input and processing
user_query = st.chat_input("Type your coding question here...")

if user_query:
    # Add user message to log
    st.session_state.message_log.append({"role": "user", "content": user_query})

    # Generate AI response
    with st.spinner("🧠 Processing..."):
        prompt_chain = build_prompt_chain(st.session_state.message_log)
        ai_response = chat_engine.generate_response(prompt_chain)

    # Add AI response to log
    st.session_state.message_log.append({"role": "ai", "content": ai_response})

    # Rerun to update chat display
    st.rerun()
