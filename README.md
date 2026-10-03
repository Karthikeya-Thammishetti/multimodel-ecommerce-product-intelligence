# 🛍️ Multimodal E-Commerce Product Intelligence Platform

An AI-powered e-commerce product intelligence platform that uses **multimodal LLMs, computer vision, embeddings, and vector search** to automatically analyze product images, generate structured product information, enrich product catalogs, and enable intelligent semantic product discovery.

---

## 🚀 Project Overview

E-commerce businesses often have large product catalogs containing incomplete or inconsistent product information. Manually creating product titles, descriptions, categories, attributes, and search keywords is time-consuming and difficult to scale.

This project automates the product catalog creation and enrichment process using Generative AI.

The platform accepts a **product image** and uses a vision-capable LLM to identify product characteristics such as:

* Product name
* Category
* Subcategory
* Color
* Material
* Style
* Product attributes
* Features
* Keywords

The generated product information is then converted into **embeddings** and stored in **ChromaDB**, enabling semantic product search and similar-product recommendations.

---

## 🎯 Key Features

### 1. 📸 AI Product Image Analysis

Upload a product image and let the AI automatically analyze it.

The system extracts:

* Product type
* Category
* Subcategory
* Color
* Material
* Style
* Pattern
* Features
* Keywords
* Target audience

---

### 2. ✍️ AI Product Title Generation

Automatically generates SEO-friendly product titles from product images and extracted attributes.

Example:

> Premium Black Stainless Steel Insulated Water Bottle

---

### 3. 📝 AI Product Description Generation

Automatically creates e-commerce-ready product descriptions.

Example:

> Premium black stainless steel water bottle designed for convenient everyday hydration.

The generated content is based only on available product information to reduce unsupported claims.

---

### 4. 🏷️ Automatic Product Categorization

The system automatically classifies products into categories and subcategories.

Example:

```text
Category: Drinkware
Subcategory: Water Bottles
```

Supported categories can include:

* Electronics
* Fashion
* Home & Kitchen
* Beauty
* Sports
* Grocery
* Accessories
* Office Supplies
* Gifts
* Drinkware
* Footwear
* Bags

---

### 5. 🔍 Intelligent Product Discovery

Users can search for products using natural language instead of exact keywords.

Example queries:

```text
black gifts for corporate employees
```

```text
premium bottles for office use
```

```text
red women's handbags
```

```text
minimal home decor
```

The system converts the search query into an embedding and retrieves semantically similar products using vector search.

---

### 6. 🧠 Embedding-Based Search

Product information is converted into vector embeddings.

Example representation:

```text
Product Name
+
Category
+
Description
+
Attributes
+
Keywords
```

These embeddings are stored in **ChromaDB**.

This enables semantic search even when the user's query does not exactly match the product keywords.

---

### 7. 🔗 Similar Product Recommendations

For every product, the system can find similar products using vector similarity.

Example:

```text
Current Product:
Black Stainless Steel Water Bottle

Similar Products:
- Stainless Steel Travel Mug
- Insulated Coffee Flask
- Silver Water Bottle
- Stainless Steel Tumbler
```

---

### 8. ⚡ Automated Catalog Enrichment

Existing product catalogs can be enriched automatically.

For example, if a catalog contains:

```text
SKU: WB001
Image: bottle.jpg
```

The system can generate:

```text
Product Name
Description
Category
Subcategory
Color
Material
Style
Features
Keywords
SEO Title
Meta Description
Embedding
```

---

### 9. 📦 Bulk Product Processing

Multiple product images can be uploaded and processed automatically.

Workflow:

```text
Product Images
      ↓
Image Processing
      ↓
Vision LLM
      ↓
Attribute Extraction
      ↓
Product Title
      ↓
Product Description
      ↓
Category Classification
      ↓
Keyword Generation
      ↓
Embeddings
      ↓
Database
      ↓
ChromaDB
```

The dashboard displays processing progress and success/failure statistics.

---

### 10. 📊 Product Analytics Dashboard

The Streamlit dashboard provides basic catalog analytics such as:

* Total Products
* Total Categories
* Products Added Today
* Products with Embeddings
* Products by Category
* Products by Color
* Products by Material

---

### 11. 📥 Catalog Export

Generated catalog information can be exported as:

* CSV
* Excel

Example columns:

```text
Product ID
Product Name
Description
Category
Subcategory
Brand
Color
Material
Style
Features
Keywords
Image Path
SEO Title
Meta Description
```

---

# 🏗️ System Architecture

```text
                    PRODUCT IMAGE
                          │
                          ▼
                 IMAGE PROCESSING
                          │
                          ▼
                VISION CAPABLE LLM
                          │
                          ▼
                 PRODUCT ATTRIBUTES
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
       PRODUCT CATALOG            TEXT DATA
              │                       │
              ▼                       ▼
        SQL DATABASE             EMBEDDINGS
                                      │
                                      ▼
                                  CHROMADB
                                      │
                                      ▼
                               VECTOR SEARCH
                                      │
                         ┌────────────┴────────────┐
                         │                         │
                         ▼                         ▼
                  PRODUCT SEARCH          SIMILAR PRODUCTS
                         │                         │
                         └────────────┬────────────┘
                                      ▼
                               STREAMLIT UI
```

---

# 🛠️ Technology Stack

## Programming Language

* Python 3.11+

## Generative AI

* OpenAI API
* Vision-capable LLM
* LangChain

## Embeddings

* OpenAI Embeddings

## Vector Database

* ChromaDB

## Database

* SQLite / PostgreSQL
* SQLAlchemy

## Data Processing

* Pandas
* NumPy

## Image Processing

* Pillow

## Frontend

* Streamlit

## Validation

* Pydantic

## Environment Management

* python-dotenv

## Testing

* Pytest

---

# 📁 Project Structure

```text
multimodal-ecommerce-intelligence/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── models/
│   ├── __init__.py
│   └── schemas.py
│
├── ai/
│   ├── __init__.py
│   ├── vision_analyzer.py
│   ├── product_generator.py
│   ├── embeddings.py
│   └── prompts.py
│
├── vector_db/
│   ├── __init__.py
│   └── chroma_manager.py
│
├── database/
│   ├── __init__.py
│   ├── connection.py
│   └── models.py
│
├── services/
│   ├── __init__.py
│   ├── catalog_service.py
│   ├── search_service.py
│   ├── recommendation_service.py
│   └── enrichment_service.py
│
├── utils/
│   ├── __init__.py
│   ├── image_utils.py
│   └── validation.py
│
├── data/
│   ├── products/
│   └── catalog/
│
└── chroma_db/
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/multimodal-ecommerce-intelligence.git
```

Move into the project:

```bash
cd multimodal-ecommerce-intelligence
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key

DATABASE_URL=sqlite:///products.db

CHROMA_DB_PATH=./chroma_db
```

For PostgreSQL:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/product_db
```

⚠️ Never commit `.env` to GitHub.

Add it to `.gitignore`:

```text
.env
venv/
__pycache__/
chroma_db/
*.pyc
```

---

# ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually:

```text
http://localhost:8501
```

---

# 🖥️ Application Modules

## Dashboard

Displays:

* Product count
* Category statistics
* Embedding statistics
* Catalog analytics

---

## Add Product

Upload an image:

```text
Product Image
      ↓
AI Analysis
      ↓
Attributes
      ↓
Product Title
      ↓
Description
      ↓
Category
      ↓
Keywords
```

Review the generated information and save it to the catalog.

---

## Bulk Catalog Generator

Upload multiple product images.

The system automatically processes each image and generates catalog information.

Example:

```text
100 Product Images
        ↓
AI Processing
        ↓
100 Product Records
        ↓
100 Embeddings
        ↓
ChromaDB
```

---

# 🔎 Semantic Search

Instead of searching only by exact keywords, users can describe what they need.

Example:

```text
Find premium gifts for corporate employees
```

The system converts the query into an embedding and searches the vector database.

Another example:

```text
Show me products suitable for office use
```

The system retrieves semantically relevant products even if the exact phrase does not appear in the product description.

---

# 🧠 How Vector Search Works

Traditional keyword search:

```text
User Query
     ↓
Keyword Matching
     ↓
Exact/Partial Matches
```

This project uses semantic search:

```text
User Query
     ↓
Embedding Model
     ↓
Vector Representation
     ↓
ChromaDB
     ↓
Similarity Search
     ↓
Relevant Products
```

For example:

```text
Query:
"corporate gifts for employees"

Possible results:

Corporate Gift Box
Desk Organizer
Coffee Mug
Premium Notebook
Water Bottle
```

The products can be retrieved based on semantic similarity rather than exact keyword matches.

---

# 🤖 Multimodal AI Workflow

The platform combines **visual information and textual information**.

```text
Product Image
     ↓
Vision LLM
     ↓
Visual Understanding
     ↓
Structured Product Data
     ↓
Text Representation
     ↓
Embeddings
     ↓
Vector Database
```

This allows the system to understand product information from images and make that information searchable.

---

# 🧩 Example Product Processing

### Input

```text
black_water_bottle.jpg
```

### AI Output

```json
{
  "product_name": "Black Stainless Steel Water Bottle",
  "category": "Drinkware",
  "subcategory": "Water Bottles",
  "color": "Black",
  "material": "Stainless Steel",
  "style": "Minimal",
  "keywords": [
    "water bottle",
    "black bottle",
    "stainless steel bottle",
    "reusable bottle"
  ]
}
```

### Generated Description

```text
A black stainless steel water bottle with a simple,
minimal design suitable for everyday use.
```

### Embedding

The product information is converted into a vector representation and stored in ChromaDB.

---

# 📈 Product Recommendation

When a user opens a product:

```text
Product
   ↓
Retrieve Product Embedding
   ↓
Similarity Search
   ↓
Top Similar Products
   ↓
Display Recommendations
```

This can support e-commerce features such as:

* Similar Products
* Related Products
* Frequently Relevant Products
* Personalized Discovery

---

# 🔄 Catalog Enrichment Workflow

Existing product:

```text
SKU
Image
Basic Product Name
```

↓

AI enrichment:

```text
Better Product Name
Description
Category
Subcategory
Attributes
Keywords
SEO Title
Meta Description
```

↓

Embedding generation:

```text
Product Information
        ↓
Embedding
        ↓
ChromaDB
```

↓

Searchable product catalog.

---

# 🔒 Security Considerations

The application follows basic security practices:

* API keys stored in environment variables
* `.env` excluded from Git
* Uploaded file validation
* File type validation
* File size restrictions
* Structured LLM output validation
* No sensitive credentials in source code
* Error handling for external API failures

---

# 🧪 Testing

Run tests using:

```bash
pytest
```

Tests cover areas such as:

* Image validation
* Product schema validation
* Database operations
* Embedding generation
* Vector search
* Search ranking
* Product enrichment

---

# 🚀 Future Improvements

Possible future enhancements:

* Image-to-image product search
* Multilingual product descriptions
* Personalized recommendations
* Customer-specific product ranking
* Product duplicate detection
* Product quality scoring
* Automated background removal
* OCR for product labels
* Barcode/QR code detection
* Hybrid keyword + vector search
* Elasticsearch integration
* PostgreSQL + pgvector
* Authentication and role-based access
* Cloud deployment
* AWS S3 image storage
* FastAPI backend
* React frontend
* Real-time catalog synchronization

---

# 💼 Business Use Cases

This platform can be used by:

### E-Commerce Businesses

Automatically create and enrich large product catalogs.

### Online Marketplaces

Standardize product information submitted by sellers.

### Retailers

Generate product descriptions and attributes from product images.

### Corporate Gifting Platforms

Automatically categorize and search large gift catalogs.

### Product Discovery Systems

Enable semantic search and similar-product recommendations.

---

# 🎓 Skills Demonstrated

This project demonstrates practical knowledge of:

* Python
* Generative AI
* Multimodal LLMs
* Computer Vision
* Prompt Engineering
* LangChain
* OpenAI API
* Embeddings
* Vector Databases
* ChromaDB
* Semantic Search
* Recommendation Systems
* Pandas
* SQL
* SQLAlchemy
* Streamlit
* Pydantic
* REST/API integration
* Data Engineering
* Catalog Automation
* AI Application Development

---

# 📌 Resume Project Description

**Multimodal E-Commerce Product Intelligence Platform**

* Developed a multimodal AI platform using **Python, Vision LLMs, LangChain, embeddings, and ChromaDB** to analyze product images and automatically generate structured product information.
* Automated **product catalog creation and enrichment**, including titles, descriptions, categories, attributes, keywords, and SEO metadata.
* Implemented **embedding-based semantic product search and similarity recommendations** using vector search, enabling intelligent product discovery beyond keyword matching.
* Built an interactive **Streamlit dashboard** for image analysis, bulk catalog processing, product search, recommendations, analytics, and CSV/Excel export.

---

# 👨‍💻 Author

**Karthikeya Thammishetti**

B.Tech – Information Technology

Interested in:

* Artificial Intelligence
* Data Science
* Generative AI
* Machine Learning
* Cybersecurity

---

# ⭐ Project Highlights

```text
📸 Image Understanding
        +
🤖 Multimodal LLM
        +
🧠 Embeddings
        +
🔎 Vector Search
        +
🛍️ Product Intelligence
        +
⚡ Catalog Automation
        =
AI-Powered E-Commerce Platform
```

If you find this project useful, consider giving the repository a ⭐ on GitHub.
