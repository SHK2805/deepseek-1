from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

class ChatEngine:
    def __init__(self, model):
        self.llm_engine = ChatOllama(
            model=model,
            base_url="http://localhost:11434",
            temperature=0.3
        )

    def generate_response(self, prompt_chain):
        processing_pipeline = prompt_chain | self.llm_engine | StrOutputParser()
        return processing_pipeline.invoke({})
