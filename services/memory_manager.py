from vectorstore.faiss_store import FAISSStore
from services.contradiction_checker import (
    ContradictionChecker
)


class MemoryManager:

    def __init__(self):

        self.store = FAISSStore()

        self.checker = ContradictionChecker()

    def process(self, extracted_memories):

        accepted = []

        rejected = []

        existing = self.store.memories

        for memory in extracted_memories:

            duplicate = self.checker.is_duplicate(
                memory,
                existing
            )

            if duplicate:

                rejected.append(
                    {
                        "memory": memory,
                        "reason": "Duplicate memory"
                    }
                )

                continue

            contradictions = (
                self.checker.find_possible_contradictions(
                    memory,
                    existing
                )
            )

            if len(contradictions) > 0:

                rejected.append(
                    {
                        "memory": memory,
                        "reason": "Possible contradiction",
                        "matches": contradictions
                    }
                )

                continue

            accepted.append(memory)

            self.store.add_memory(memory)

            existing.append(memory)

        return {

            "accepted": accepted,

            "rejected": rejected

        }