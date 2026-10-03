from __future__ import annotations

from typing import Any

from langchain_openai import OpenAIEmbeddings

from config.settings import settings


def create_embedding_model() -> OpenAIEmbeddings:
    if not settings.OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is missing. Please set it in the environment or .env file.")
    return OpenAIEmbeddings(model="text-embedding-3-small", api_key=settings.OPENAI_API_KEY)


def generate_embedding(text: str) -> list[float]:
    model = create_embedding_model()
    return model.embed_query(text)


def build_embedding_text(
    product_name: str,
    category: str,
    description: str,
    attributes: dict[str, Any],
    keywords: list[str],
) -> str:
    attribute_values = []
    for key in ["color", "material", "style", "pattern", "shape"]:
        value = attributes.get(key)
        if value and value != "Unknown":
            attribute_values.append(str(value))

    keyword_text = ", ".join(str(item) for item in keywords if item and item != "Unknown")
    attribute_text = " | ".join(attribute_values)
    return (
        f"{product_name} | {category} | {description} | {attribute_text} | {keyword_text}"
    ).strip(" | ")
