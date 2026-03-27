from openai import OpenAI
from src.config import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_text(prompt: str) -> str:
    response = client.responses.create(
        model=MODEL_NAME,
        input=prompt
    )
    return response.output_text.strip()