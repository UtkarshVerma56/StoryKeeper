from services.embedder import Embedder


class ContradictionChecker:

    def __init__(self):

        self.embedder = Embedder()

    def cosine_similarity(self, vector1, vector2):

        numerator = (vector1 * vector2).sum()

        denominator = (
            (vector1 ** 2).sum() ** 0.5
        ) * (
            (vector2 ** 2).sum() ** 0.5
        )

        if denominator == 0:

            return 0

        return float(numerator / denominator)

    def is_duplicate(self, new_memory, stored_memories):

        new_embedding = self.embedder.encode(
            new_memory["text"]
        )

        for memory in stored_memories:

            embedding = self.embedder.encode(
                memory["text"]
            )

            similarity = self.cosine_similarity(
                new_embedding,
                embedding
            )

            if similarity > 0.90:

                return True

        return False

    def find_possible_contradictions(
        self,
        new_memory,
        stored_memories
    ):

        keywords = set(
            new_memory["text"].lower().split()
        )

        possible = []

        for memory in stored_memories:

            existing = set(
                memory["text"].lower().split()
            )

            overlap = keywords.intersection(existing)

            if len(overlap) >= 3:

                possible.append(memory)

        return possible