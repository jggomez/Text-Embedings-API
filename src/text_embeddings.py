import mediapipe as mp
from dataclasses import dataclass

# Import libraries and get the classes
BaseOptions = mp.tasks.BaseOptions
TextEmbedder = mp.tasks.text.TextEmbedder
TextEmbedderOptions = mp.tasks.text.TextEmbedderOptions


@dataclass
class GetTextSimilarityResp:
    text1_embeddings: str
    text2_embeddings: str
    similarity: float


class GetTextSimilarityEmbeddings:

    def __init__(self, model_ml) -> None:
        self.model_ml = model_ml

    def run(self, text1: str, text2: str) -> GetTextSimilarityResp:
        # Declare options
        options = TextEmbedderOptions(
            base_options=BaseOptions(model_asset_path=self.model_ml),
            quantize=True)

        with TextEmbedder.create_from_options(options) as text_embedder:
            embedding_result_text1 = text_embedder.embed(text1)
            embedding_result_text2 = text_embedder.embed(text2)

        # Cosine or Euclid method used
        similarity = TextEmbedder.cosine_similarity(
            embedding_result_text1.embeddings[0],
            embedding_result_text2.embeddings[0]
        )

        return GetTextSimilarityResp(
            embedding_result_text1.embeddings[0].embedding,
            embedding_result_text2.embeddings[0].embedding,
            similarity
        )
