class MemoryPrompt:

    @staticmethod
    def build(chapter):

        return f"""
Extract long-term memories from the story.

Only include information that is important for future chapters.

Categories

- character
- relationship
- object
- location
- event
- goal
- secret

Return ONLY JSON.

Story

{chapter}
"""