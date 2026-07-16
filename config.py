import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    EMBEDDING_MODEL = "all-MiniLM-L6-v2"

    GEMINI_MODEL = "gemini-2.5-flash"

    VECTOR_DIMENSION = 384

    MEMORY_FILE = "data/memories.json"

    FAISS_INDEX = "data/faiss.index"