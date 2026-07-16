import google.generativeai as genai

from config import Config
from prompts.story_prompt import StoryPrompt


class StoryGenerator:

    def __init__(self):

        genai.configure(
            api_key=Config.GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            Config.GEMINI_MODEL
        )

    def generate(self, current_chapter, retrieved_memories):

        prompt = StoryPrompt.build(
            current_chapter,
            retrieved_memories
        )

        response = self.model.generate_content(prompt)

        return response.text.strip()