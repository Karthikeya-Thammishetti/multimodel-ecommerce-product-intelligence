from __future__ import annotations

import base64
import json
from pathlib import Path

from openai import OpenAI

from ai.prompts import IMAGE_ANALYSIS_PROMPT
from config.settings import settings
from models.schemas import ProductAnalysis


class VisionAnalyzer:
    def __init__(self, api_key: str | None = None, model: str = "gpt-4o-mini") -> None:
        self.api_key = api_key or settings.OPENAI_API_KEY
        self.model = model
        self.client = OpenAI(api_key=self.api_key) if self.api_key else None

    def _encode_image(self, image_path: str | Path) -> str:
        path = Path(image_path)
        with path.open("rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    def analyze_image(self, image_path: str | Path) -> ProductAnalysis:
        if not self.client:
            raise ValueError("OPENAI_API_KEY is missing. Add it to your .env file before analyzing images.")

        base64_image = self._encode_image(image_path)
        response = self.client.chat.completions.create(
            model=self.model,
            response_format={"type": "json_object"},
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": IMAGE_ANALYSIS_PROMPT},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                        },
                    ],
                }
            ],
        )

        raw_response = response.choices[0].message.content
        if not raw_response:
            raise ValueError("The vision model returned an empty response.")

        payload = json.loads(raw_response)
        return ProductAnalysis.model_validate(payload)
