class StoryPrompt:

    @staticmethod
    def build(current_chapter, retrieved_memories):

        memory_section = ""

        if len(retrieved_memories) == 0:

            memory_section = "No previous memories available."

        else:

            for index, memory in enumerate(retrieved_memories, start=1):

                memory_section += (
                    f"{index}. "
                    f"{memory['text']} "
                    f"(Category: {memory['category']})\n"
                )

        prompt = f"""
You are an expert fantasy story writer.

Your task is to continue the story while keeping all
characters, relationships, locations and previous events
consistent.

Previously Remembered Facts

{memory_section}

Current Chapter

{current_chapter}

Instructions

- Continue the story naturally.
- Never contradict remembered facts.
- Keep characters consistent.
- Introduce new events only if they fit naturally.
- Write approximately 300-500 words.
- Do not summarize.
- Continue directly from the current chapter.

Generate the next chapter.
"""

        return prompt