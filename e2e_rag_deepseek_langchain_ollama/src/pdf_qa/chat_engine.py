from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_core.vectorstores import InMemoryVectorStore

LANGUAGE_MODEL = OllamaLLM(model="deepseek-r1:1.5b")
EMBEDDING_MODEL = OllamaEmbeddings(model="deepseek-r1:1.5b")

PROMPT_TEMPLATE = """
You are an expert research assistant. Use the provided context to answer the query. 
If unsure, state that you don't know. Be concise and factual (max 3 sentences).

Query: {user_query} 
Context: {document_context} 
Answer:
"""

def find_related_documents(query, document_vector_db):
    return document_vector_db.similarity_search(query)

def generate_answer(user_query, context_documents, prompt_template):
    context_text = "\n\n".join([doc.page_content for doc in context_documents])
    conversation_prompt = ChatPromptTemplate.from_template(prompt_template)
    response_chain = conversation_prompt | LANGUAGE_MODEL
    return response_chain.invoke({"user_query": user_query, "document_context": context_text})

def generate_response(user_query, processed_chunks, prompt_template):
    document_vector_db = InMemoryVectorStore(EMBEDDING_MODEL)
    document_vector_db.add_documents(processed_chunks)
    relevant_docs = find_related_documents(user_query, document_vector_db)
    return generate_answer(user_query, relevant_docs, prompt_template)
