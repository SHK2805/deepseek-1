import streamlit as st
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Custom CSS styling
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }

    /* Chat Input Styling */
    .stChatInput input {
        background-color: #1E1E1E !important;
        color: #FFFFFF !important;
        border: 1px solid #3A3A3A !important;
    }

    /* User Message Styling */
    .stChatMessage[data-testid="stChatMessage"]:nth-child(odd) {
        background-color: #1E1E1E !important;
        border: 1px solid #3A3A3A !important;
        color: #E0E0E0 !important;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }

    /* Assistant Message Styling */
    .stChatMessage[data-testid="stChatMessage"]:nth-child(even) {
        background-color: #2A2A2A !important;
        border: 1px solid #404040 !important;
        color: #F0F0F0 !important;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }

    /* Avatar Styling */
    .stChatMessage .avatar {
        background-color: #00FFAA !important;
        color: #000000 !important;
    }

    /* Text Color Fix */
    .stChatMessage p, .stChatMessage div {
        color: #FFFFFF !important;
    }

    .stFileUploader {
        background-color: #1E1E1E;
        border: 1px solid #3A3A3A;
        border-radius: 5px;
        padding: 15px;
    }

    h1, h2, h3 {
        color: #00FFAA !important;
    }
    </style>
    """, unsafe_allow_html=True)

# prompt template
prompt_text = """
You are an expert research assistant. Use the provided context to answer the query. If you are unsure, state that you do not know.
Be concise and factual. Do not provide any personal opinions or beliefs. Always respond in English. Max 3 sentences.

Query: {user_query}
Context: {document_context}
Answer:
"""

pdf_storage_path = "./document_store/pdfs/"
embedding_model = OllamaEmbeddings(model="deepseek-r1:1.5b")
vector_store = InMemoryVectorStore(embedding=embedding_model)
language_model = OllamaLLM(model="deepseek-r1:1.5b")

# upload the pdf file
def upload_pdf(uploaded_file):
    pdf_file_path = pdf_storage_path + uploaded_file.name
    with open(pdf_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return pdf_file_path

# load the pdf file
def load_pdf(pdf_file_path):
    pdf_loader = PDFPlumberLoader(pdf_file_path)
    return pdf_loader.load()

# split the text
def split_text(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    return text_splitter.split_documents(text)

# add chunks to the vector store
def add_chunks_to_vector_store(chunks):
    vector_store.add_documents(chunks)

# find related chunks
def find_related_chunks(user_query):
   return vector_store.similarity_search(user_query)

# generate a response
def generate_response(related_chunks, user_query):
    context = "\n\n".join([doc.page_content for doc in related_chunks])
    prompt = ChatPromptTemplate.from_template(prompt_text.format(user_query=user_query, document_context=context))
    chain = prompt | language_model
    return chain.invoke({})

# UI
st.title("📚 Document Assistant")
st.caption("🚀 AI Assistant")
st.markdown("### Upload a PDF document to get started")

# file upload
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"], accept_multiple_files=False, help="Upload a PDF file")

if uploaded_file:
    pdf_file_path = upload_pdf(uploaded_file)
    st.success(f"PDF file uploaded successfully to {pdf_file_path}! 🎉")

    # check if the file is uploaded
    if not pdf_file_path:
        st.error("Please upload a PDF file to continue.")
        st.stop()
    # load the pdf file
    pdf_text = load_pdf(pdf_file_path)

    # split the text
    pdf_chunks = split_text(pdf_text)

    # add chunks to the vector store
    add_chunks_to_vector_store(pdf_chunks)
    st.success("PDF text processed successfully! 🎉")

    # user query
    user_query = st.text_input("Type your query here...")
    if user_query:
       with st.chat_message("user"):
           st.write(user_query)

         # find related chunks
       with st.spinner("Searching for related information..."):
            related_chunks = find_related_chunks(user_query)
            response = generate_response(related_chunks, user_query)
            with st.chat_message("assistant", avatar="🤖"):
                st.write(response)









