from fastapi import FastAPI

from models.story import StoryRequest
from services.extractor import MemoryExtractor
from services.generator import StoryGenerator
from services.retriever import MemoryRetriever
from services.memory_manager import MemoryManager

app = FastAPI(title="StoryKeeper")

extractor = MemoryExtractor()
retriever = MemoryRetriever()
generator = StoryGenerator()
memory_manager = MemoryManager()


@app.get("/")
def home():

    return {
        "message": "StoryKeeper API Running"
    }


@app.post("/generate")
def generate_story(request: StoryRequest):

    # Step 1: Extract important memories from the current chapter
    extracted_memories = extractor.extract(
        request.chapter
    )

    # Step 2: Retrieve relevant memories from FAISS
    retrieved_context = retriever.retrieve(
        extracted_memories
    )

    # Step 3: Generate the next chapter using retrieved context
    next_chapter = generator.generate(
        request.chapter,
        retrieved_context
    )

    # Step 4: Store only valid memories
    memory_report = memory_manager.process(
        extracted_memories
    )

    # Step 5: Return the response
    return {
        "generated_story": next_chapter,
        "retrieved_memory": retrieved_context,
        "memory_report": memory_report
    }