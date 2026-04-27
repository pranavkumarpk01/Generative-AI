🚀 Gen AI Mini Project — Build a Website Q&A System using Qdrant
🎯 Objective
Build a Retrieval-Augmented Generation (RAG) based Question Answering system that can:
Scrape website content from:
GeeksforGeeks
Store the content inside:
Qdrant
Convert the text into embeddings
Retrieve Top-K relevant chunks (TopK = 5)
Generate accurate answers based on the ingested website content
🌐 Website to Scrape
Writing
https://www.geeksforgeeks.org/python/python-programming-language-tutorial/
📌 Requirements
1. Web Scraping
Scrape the webpage content using Python
Extract only textual content
Do not scrape:
Images
Scripts
Advertisements
Navigation bars
Footer content
📌 2. Chunking Methodology
Implement chunking on the extracted content
Store chunks before generating embeddings
📌 3. Embedding Model
Generate embeddings for each chunk
Use the embedding vectors for semantic retrieval
📌 4. Qdrant Database
Create a collection in:
Qdrant
Store:
chunked text
embeddings
metadata
📌 5. Retrieval System
For every user query:
Convert the query into embeddings
Retrieve:
TopK = 5
Fetch the most relevant chunks from Qdrant
Generate the final answer based on retrieved content
📌 Expected Workflow
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
📌 Deliverables
Python scraping script
Chunking implementation
Embedding generation
Qdrant collection setup
Retrieval pipeline
Final Question Answering system
