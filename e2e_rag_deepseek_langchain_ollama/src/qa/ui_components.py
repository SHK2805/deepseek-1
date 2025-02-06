import streamlit as st

def configure_custom_css():
    st.markdown("""
    <style>
        .main {
            background-color: #1a1a1a;
            color: #ffffff;
        }
        .sidebar .sidebar-content {
            background-color: #2d2d2d;
        }
        .stTextInput textarea {
            color: #ffffff !important;
        }
        .stSelectbox div[data-baseweb="select"] {
            color: white !important;
            background-color: #3d3d3d !important;
        }
        .stSelectbox svg {
            fill: white !important;
        }
        .stSelectbox option {
            background-color: #2d2d2d !important;
            color: white !important;
        }
        div[role="listbox"] div {
            background-color: #2d2d2d !important;
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)

def configure_sidebar():
    with st.sidebar:
        st.header("⚙️ Configuration")
        selected_model = st.selectbox(
            "Choose Model",
            ["deepseek-r1:1.5b", "deepseek-r1:3b"],
            index=0
        )
        st.divider()
        st.markdown("### Model Capabilities")
        st.markdown("""
        - 🐍 Python Expert
        - 🐞 Debugging Assistant
        - 📝 Code Documentation
        - 💡 Solution Design
        """)
        st.divider()
        st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")
    return selected_model
