from fastapi import APIRouter
from fastapi import Response
from fastapi import status
from pydantic import BaseModel
from pydantic import Field
from text_embeddings import GetTextSimilarityEmbeddings

router = APIRouter()


class RequestTextEmbeddingsDTO(BaseModel):
    text1: str = Field(alias="text1")
    text2: str = Field(alias="text2")


class ResponseTextEmbeddingsDTO(BaseModel):
    text1_embedding: str = Field(alias="text1embedding")
    text2_embedding: str = Field(alias="text2embedding")
    similarity: str = Field(alias="similarity")


@router.post("/apis/v1/textembeddings", name="textembeddings")
async def text_embeddings(
    request_body: RequestTextEmbeddingsDTO,
    response: Response,
):
    try:
        text1 = request_body.text1
        text2 = request_body.text2

        model_ml = "models/universal_sentence_encoder.tflite"

        text_embeddings = GetTextSimilarityEmbeddings(model_ml)
        result_embeddings = text_embeddings.run(text1, text2)

        print(f"Similarity => {result_embeddings.similarity}")

        return ResponseTextEmbeddingsDTO.construct(
            text1_embedding=str(result_embeddings.text1_embeddings),
            text2_embedding=str(result_embeddings.text2_embeddings),
            similarity=result_embeddings.similarity
        )

    except Exception as e:
        print(f"Fatal error in textembeddings => {e}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"code": 500, "message": str(e)}
