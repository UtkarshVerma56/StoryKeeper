from sentence_transformers import SentenceTransformer

from config import Config


class Embedder:

    def __init__(self):

        self.model = SentenceTransformer(
            Config.EMBEDDING_MODEL
        )

    def encode(self, text):

        embedding = self.model.encode(
            text,
            convert_to_numpy=True
        )

        return embedding.astype("float32")

    def encode_batch(self, texts):

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        return embeddings.astype("float32")