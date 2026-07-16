from vectorstore.faiss_store import FAISSStore


class MemoryRetriever:

    def __init__(self):

        self.store = FAISSStore()

    def retrieve(self, memories):

        if len(memories) == 0:

            return []

        retrieved = []

        visited = set()

        for memory in memories:

            similar = self.store.search(
                memory["text"],
                top_k=3
            )

            for item in similar:

                text = item["text"]

                if text not in visited:

                    visited.add(text)

                    retrieved.append(item)

        return retrieved

    def store(self, memories):

        if len(memories) == 0:

            return

        self.store.add_memories(memories)