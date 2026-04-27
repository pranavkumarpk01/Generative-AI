# 🚀 Gen AI Mini Project — Build a Website Q&A System using Qdrant

## 🎯 Objective

Build a Retrieval-Augmented Generation (RAG) based Question Answering system that can:

1. Scrape website content from GeeksforGeeks
2. Store the content inside Qdrant
3. Convert the text into embeddings
4. Retrieve Top-K relevant chunks (`TopK = 5`)
5. Generate accurate answers based on the ingested website content

---

# 🌐 Website to Scrape

```text
https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
```

---

# 📌 Requirements

## 1. Web Scraping

- Scrape the webpage content using Python
- Extract only textual content
- Do not scrape:
  - Images
  - Scripts
  - Advertisements
  - Navigation bars
  - Footer content

---

# 📌 2. Chunking Methodology

- Implement chunking on the extracted content
- Store chunks before generating embeddings

---

# 📌 3. Embedding Model

- Generate embeddings for each chunk
- Use the embedding vectors for semantic retrieval

---

# 📌 4. Qdrant Database

- Create a collection in Qdrant
- Store:
  - chunked text
  - embeddings
  - metadata

---

# 📌 5. Retrieval System

For every user query:

1. Convert the query into embeddings
2. Retrieve:

```python
TopK = 5
```

3. Fetch the most relevant chunks from Qdrant
4. Generate the final answer based on retrieved content

---

# 📌 Expected Workflow

```text
Website
   ↓
Web Scraper
   ↓
Clean Text
   ↓
Chunking
   ↓
Embedding Model
   ↓
Qdrant Collection
   ↓
User Query
   ↓
TopK Retrieval
   ↓
LLM
   ↓
Final Answer
```

---

# 📌 Deliverables

- Python scraping script
- Chunking implementation
- Embedding generation
- Qdrant collection setup
- Retrieval pipeline
- Final Question Answering system
