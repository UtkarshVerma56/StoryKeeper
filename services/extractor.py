import json
import google.generativeai as genai

from config import Config


class MemoryExtractor:

    def __init__(self):

        genai.configure(
            api_key=Config.GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            Config.GEMINI_MODEL
        )

    def build_prompt(self, chapter):

        return f"""
You are an AI memory extraction system.

Read the story chapter and extract only the important long-term memories.

Store information that will be useful in future chapters.

Examples:
- Character introductions
- Character traits
- Relationships
- Important locations
- Objects
- Major events
- Secrets
- Goals

Return ONLY valid JSON.

Example:

[
 {{
   "text":"John is a brave knight.",
   "category":"character",
   "importance":3
 }},
 {{
   "text":"Emma is John's sister.",
   "category":"relationship",
   "importance":2
 }}
]

Story:

{chapter}
"""

    def extract(self, chapter):

        prompt = self.build_prompt(chapter)

        response = self.model.generate_content(prompt)

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "")
            text = text.replace("```", "").strip()

        elif text.startswith("```"):
            text = text.replace("```", "").strip()

        try:

            memories = json.loads(text)

        except Exception:

            memories = []

        return memories