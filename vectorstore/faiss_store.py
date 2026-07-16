import json
import os

import faiss
import numpy as np

from config import Config
from services.embedder import Embedder


class FAISSStore:

    def __init__(self):

        self.embedder = Embedder()

        if os.path.exists(Config.FAISS_INDEX):

            self.index = faiss.read_index(
                Config.FAISS_INDEX
            )

        else:

            self.index = faiss.IndexFlatL2(
                Config.VECTOR_DIMENSION
            )

        if os.path.exists(Config.MEMORY_FILE):

            with open(
                Config.MEMORY_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                self.memories = json.load(file)

        else:

            self.memories = []

    def save(self):

        faiss.write_index(
            self.index,
            Config.FAISS_INDEX
        )

        with open(
            Config.MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.memories,
                file,
                indent=4,
                ensure_ascii=False
            )

    def add_memory(self, memory):

        embedding = self.embedder.encode(
            memory["text"]
        )

        self.index.add(
            np.array([embedding])
        )

        self.memories.append(memory)

        self.save()

    def add_memories(self, memory_list):

        for memory in memory_list:

            self.add_memory(memory)

    def search(self, query, top_k=5):

        if len(self.memories) == 0:

            return []

        query_embedding = self.embedder.encode(query)

        distances, indices = self.index.search(
            np.array([query_embedding]),
            top_k
        )

        results = []

        for idx in indices[0]:

            if idx == -1:
                continue

            if idx < len(self.memories):

                results.append(
                    self.memories[idx]
                )

        return results

    def total_memories(self):

        return len(self.memories)

    def clear(self):

        self.index = faiss.IndexFlatL2(
            Config.VECTOR_DIMENSION
        )

        self.memories = []

        self.save()