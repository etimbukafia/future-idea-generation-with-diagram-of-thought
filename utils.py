import os
from dotenv import load_dotenv
from langchain_fireworks import ChatFireworks
from langchain_huggingface import HuggingFaceEmbeddings
load_dotenv()

class Config:
    """
    Class to initialize the LLM and Embedding model configs
    """
    def __init__(self):
        self.llm = None
        self.embeddings = None
        self.fireworks_api_key = os.environ.get("FIREWORKS_API_KEY")

    def initialize(self):
        self.llm = ChatFireworks(
            model="accounts/fireworks/models/llama-v3p1-405b-instruct",
            temperature = 0.6,
            max_tokens = 16384,
            model_kwargs={"top_p": 1},
            cache=None
        )

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': False}
        )


    def get_llm(self):
        return self.llm

    def get_embeddings(self):
        return self.embeddings
