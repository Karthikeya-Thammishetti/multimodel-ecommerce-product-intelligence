from __future__ import annotations

import json

from openai import OpenAI

from ai.prompts import (
    PRODUCT_DESCRIPTION_PROMPT,
    PRODUCT_TITLE_PROMPT,
    SEO_METADATA_PROMPT,
)
from config.settings import settings
from models.schemas import ProductAnalysis, SEOData


class ProductGenerator:
    def __init__(self, api_key: str | None = None, model: str = "gpt-4o-mini") -> None:
        self.api_key = api_key or settings.OPENAI_API_KEY
        self.model = model
        self.client = OpenAI(api_key=self.api_key) if self.api_key else None

    def _ensure_client(self) -> None:
        if not self.client:
            raise ValueError("OPENAI_API_KEY is missing. Add it to your .env file before generating AI metadata.")

    def generate_title(self, analysis: ProductAnalysis) -> str:
        self._ensure_client()
        prompt = (
            f"Product name: {analysis.product_name}\n"
            f"Category: {analysis.category}\n"
            f"Material: {analysis.material}\n"
            f"Color: {analysis.primary_color}\n"
            f"Style: {analysis.style}\n\n"
            f"{PRODUCT_TITLE_PROMPT}"
        )
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()

    def generate_description(self, analysis: ProductAnalysis, title: str | None = None) -> str:
        self._ensure_client()
        prompt = (
            f"Product title: {title or analysis.product_name}\n"
            f"Category: {analysis.category}\n"
            f"Brand: {analysis.brand}\n"
            f"Color: {analysis.primary_color}\n"
            f"Material: {analysis.material}\n"
            f"Style: {analysis.style}\n"
            f"Features: {', '.join(analysis.features) if analysis.features else 'Unknown'}\n"
            f"Keywords: {', '.join(analysis.keywords) if analysis.keywords else 'Unknown'}\n\n"
            f"{PRODUCT_DESCRIPTION_PROMPT}"
        )
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()

    def generate_seo_metadata(self, product_name: str, description: str, category: str, keywords: list[str]) -> SEOData:
        self._ensure_client()
        prompt = (
            f"Product name: {product_name}\n"
            f"Description: {description}\n"
            f"Category: {category}\n"
            f"Keywords: {', '.join(keywords)}\n\n"
            f"{SEO_METADATA_PROMPT}"
        )
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0,
            response_format={"type": "json_object"},
            messages=[{"role": "user", "content": prompt}],
        )
        payload = json.loads(response.choices[0].message.content)
        return SEOData.model_validate(payload)

    def enrich_product(self, existing_data: dict, analysis: ProductAnalysis) -> dict:
        merged = {
            "product_name": existing_data.get("product_name") or analysis.product_name,
            "category": existing_data.get("category") or analysis.category,
            "subcategory": existing_data.get("subcategory") or analysis.subcategory,
            "brand": existing_data.get("brand") or analysis.brand,
            "color": existing_data.get("color") or analysis.primary_color,
            "material": existing_data.get("material") or analysis.material,
            "style": existing_data.get("style") or analysis.style,
            "keywords": list(existing_data.get("keywords") or analysis.keywords),
            "features": list(existing_data.get("features") or analysis.features),
        }
        return merged
