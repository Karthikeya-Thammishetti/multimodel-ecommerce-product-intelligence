IMAGE_ANALYSIS_PROMPT = """
You are a careful retail image analyst. Extract product information only from the visible product in the image.

Return valid JSON only using this schema:
{
  "product_name": "string",
  "category": "string",
  "subcategory": "string",
  "brand": "string",
  "primary_color": "string",
  "secondary_colors": ["string"],
  "material": "string",
  "pattern": "string",
  "style": "string",
  "product_type": "string",
  "target_audience": "string",
  "features": ["string"],
  "keywords": ["string"],
  "search_tags": ["string"]
}

Rules:
- Do not hallucinate. Use only visible or explicitly provided information.
- If a property cannot be determined, return "Unknown" for strings and an empty array for lists.
- Keep all values concise and consistent.
- Do not invent brand, price, material, certifications, dimensions, or specifications.
- Prefer a product-oriented category and useful keywords for ecommerce search.
"""

PRODUCT_TITLE_PROMPT = """
Create a concise e-commerce product title for the given product.
Rules:
- 5 to 15 words
- SEO friendly
- No unsupported claims
- No fake adjectives
- Use only visible information
- Return plain text only without quotes
"""

PRODUCT_DESCRIPTION_PROMPT = """
Write an e-commerce product description in a clear sales-ready format.
Structure:
1. Short description sentence
2. Key features bullet list (2 to 5 features)
3. Ideal use cases (1 sentence)
4. Search keywords

Use only supported information visible in the image or product attributes. Do not invent specs or features.
Return plain text with sections labeled clearly.
"""

CATEGORY_CLASSIFICATION_PROMPT = """
Classify the product into a suitable category and subcategory for an ecommerce catalog.
You may use only these categories:
- Electronics
- Fashion
- Home & Kitchen
- Beauty
- Sports
- Grocery
- Accessories
- Office Supplies
- Gifts
- Drinkware
- Footwear
- Bags

Return valid JSON only:
{
  "category": "string",
  "subcategory": "string"
}

If uncertain, use the most likely category and "Unknown" for subcategory.
"""

KEYWORD_PROMPT = """
Generate a list of retailer-friendly product keywords and search tags.
Rules:
- Use only supported information
- Include 5 to 12 keywords
- Prefer common ecommerce phrases
- Return JSON: {"keywords": ["string"], "search_tags": ["string"]}
"""

SEO_METADATA_PROMPT = """
Generate SEO metadata for an ecommerce product. Return valid JSON only:
{
  "seo_title": "string",
  "meta_description": "string",
  "search_keywords": ["string"]
}

Rules:
- Do not include unsupported claims
- Make the title compact and product-specific
- Keep the meta description descriptive and sales-ready
- Use 5 to 10 keywords
"""

ENRICHMENT_PROMPT = """
You are enriching a minimal product listing with image-derived information.
Preserve any user-provided details that are already known. Only fill missing fields using visible evidence.
Return valid JSON with fields:
{
  "product_name": "string",
  "category": "string",
  "subcategory": "string",
  "brand": "string",
  "color": "string",
  "material": "string",
  "style": "string",
  "keywords": ["string"],
  "features": ["string"],
  "seo_title": "string",
  "meta_description": "string"
}

Use "Unknown" when information cannot be determined.
"""
