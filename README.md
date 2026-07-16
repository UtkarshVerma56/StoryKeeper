# StoryKeeper

StoryKeeper is an AI-powered storytelling system that helps language models remember important details across multiple chapters. 
It stores and retrieves character traits, relationships, and past events to generate more consistent and coherent long-form stories.

## Features

- Character memory tracking
- Semantic memory retrieval using vector embeddings
- Long-term story context management
- Consistent multi-chapter story generation
- Memory-aware prompting with Gemini
- Basic contradiction detection

## Tech Stack

- FastAPI
- Google Gemini
- Sentence Transformers
- FAISS
- Python

## Project Structure

StoryKeeper/
├── app.py
├── config.py
├── models/
├── services/
├── vectorstore/
├── prompts/
├── data/
└── README.md

## How It Works

1. User submits a story chapter.
2. Important memories are extracted.
3. Memories are converted into embeddings.
4. Embeddings are stored in FAISS.
5. Relevant memories are retrieved.
6. Retrieved context is provided to Gemini.
7. A new chapter is generated while maintaining story consistency.

