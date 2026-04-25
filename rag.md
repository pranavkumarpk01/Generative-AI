# Retrieval-Augmented Generation (RAG) Notes


## How to find these changes in the correct Git repository

If you cannot see this file or commit in your local machine, verify you are in the same repository and branch where the change was made.

### Quick verification commands
```bash
pwd
git rev-parse --show-toplevel
git remote -v
git branch --show-current
git log --oneline -n 5
```

### What to check
- **Repository root** should be `Generative-AI` (or your local clone of `pranavkumarpk01/Generative-AI`).
- **Branch** should match the branch where the commit was pushed/opened.
- **Commit history** should include the commit that added this file.

### Locate this exact file
```bash
# From repo root
ls rag.md

# Show tracked location
git ls-files | rg '^rag\.md$'

# Open file quickly
sed -n '1,80p' rag.md
```

### If still missing
```bash
git fetch --all --prune
git checkout <branch-name>
git pull
```
Then re-run:
```bash
git log --oneline -- rag.md
```

---
## 1) RAG Overview

Retrieval-Augmented Generation (RAG) is an architecture that combines:
- **Retrieval**: finding relevant external knowledge for a user query.
- **Generation**: using an LLM to produce a grounded response from that retrieved knowledge.

### Why RAG matters
- **Reduces hallucinations** by grounding answers in source documents.
- **Keeps knowledge fresh** without retraining the model.
- **Improves transparency** by enabling source citations.
- **Lowers cost/time** compared to frequent model fine-tuning.

### Typical RAG pipeline
1. **Ingestion**
   - Collect documents (PDFs, webpages, FAQs, tickets, policies).
2. **Preprocessing**
   - Clean text, remove boilerplate, normalize formatting.
3. **Chunking**
   - Split long text into retrievable units.
4. **Embedding**
   - Convert chunks into vectors.
5. **Indexing**
   - Store vectors + metadata in a vector database.
6. **Retrieval at query time**
   - Embed user query and fetch top-k similar chunks.
7. **Augmented prompt construction**
   - Build prompt with query + retrieved context.
8. **Generation**
   - LLM produces final answer using retrieved context.
9. **Post-processing (optional)**
   - Add citations, confidence notes, formatting, guardrails.

### Common RAG patterns
- **Naive RAG**: single retrieval step, direct prompt to LLM.
- **Hybrid RAG**: combine keyword/BM25 + vector search.
- **Reranked RAG**: retrieve many, rerank with cross-encoder.
- **Agentic RAG**: multiple retrieval/planning steps and tool usage.
- **Conversational RAG**: memory-aware retrieval over chat history.

### Core challenges in RAG
- Retrieving irrelevant chunks (poor recall/precision).
- Chunk size mismatch (too small loses context, too large adds noise).
- Embedding/model mismatch with domain language.
- Stale or duplicate documents.
- Prompt injection and untrusted context risks.

---

## 2) Embeddings

Embeddings are dense numerical representations of text where semantically similar texts are placed close together in vector space.

### Key idea
A sentence like **"reset my password"** should have a vector near **"how to change account credentials"**, and far from unrelated text like **"refund policy for damaged items"**.

### Embedding workflow in RAG
- Convert each document chunk into an embedding vector (offline ingestion).
- Convert each user query into an embedding vector (online query time).
- Use nearest-neighbor search to find similar chunk vectors.

### Important embedding considerations
- **Model choice**
  - General-purpose vs domain-specific embeddings.
  - Dimensions differ (e.g., 384, 768, 1536, 3072).
- **Normalization**
  - Some systems normalize vectors to unit length (important for cosine similarity).
- **Latency and cost**
  - Large models may improve quality but increase inference cost.
- **Language coverage**
  - Multilingual embeddings for global corpora.
- **Domain adaptation**
  - Jargon-heavy domains (legal, medical, HR, finance) may need specialized models.

### Best practices
- Use **the same embedding model** for indexing and query embeddings.
- Version embeddings and re-index when changing model/version.
- Store metadata (document id, source, section, timestamp).
- Evaluate retrieval quality with domain-specific test queries.

---

## 3) Document Chunking

Chunking is the process of splitting documents into smaller pieces so retrieval can target relevant sections efficiently.

### Why chunking is critical
- LLM context windows are finite.
- Retrieval is more accurate when chunks are focused.
- Good chunking improves both recall and answer quality.

### A) Fixed Chunking
Split text by constant size (e.g., 500 tokens/chars each).

**Pros**
- Simple and fast.
- Easy to implement at scale.

**Cons**
- May split sentences/ideas awkwardly.
- Can mix unrelated topics in one chunk.

**Use when**
- You need a baseline quickly.
- Documents are relatively uniform and structured.

### B) Overlapping Chunking
Create fixed chunks with overlap (e.g., 500-token chunks with 100-token overlap).

**Pros**
- Preserves context across boundaries.
- Reduces risk of losing key sentences split between chunks.

**Cons**
- Increased storage and indexing cost (duplicate text in overlaps).
- Potential repeated retrieval of similar chunks.

**Use when**
- Context continuity is important (policies, long procedures, contracts).

### C) Semantic Chunking
Split based on meaning/structure:
- Paragraph boundaries
- Headings/subheadings
- Sentence similarity shifts
- Topic segmentation models

**Pros**
- Better semantic coherence per chunk.
- Often improves retrieval precision.

**Cons**
- More complex and slower preprocessing.
- Requires careful tuning and validation.

**Use when**
- High-quality retrieval is a priority.
- Documents have clear logical structure.

### Practical chunking guidelines
- Start with token-based chunks (e.g., 300–800 tokens).
- Add overlap (10–20%) for continuity.
- Keep structure metadata (title, section, page number).
- Measure retrieval metrics before/after chunk strategy changes.

---

## 4) Embedding Similarity Metrics

Once embeddings are generated, similarity metrics determine which chunks are “closest” to a query.

### A) Cosine Similarity
Measures angle between vectors (ignores magnitude).

\[
\text{cosine}(A, B) = \frac{A \cdot B}{\|A\|\|B\|}
\]

**Interpretation**
- 1.0 => highly similar direction
- 0 => orthogonal (unrelated)
- -1 => opposite direction

**When useful**
- Most text embedding use cases.
- Especially when vector magnitude is not meaningful.

### B) Euclidean Distance (L2)
Measures straight-line distance between vectors.

\[
\|A - B\|_2 = \sqrt{\sum_i (A_i - B_i)^2}
\]

**Interpretation**
- Smaller distance => more similar.

**When useful**
- Spaces where absolute coordinates and magnitude matter.
- Some ANN indexes are tuned for L2.

### C) Dot Product
Raw inner product:

\[
A \cdot B = \sum_i A_i B_i
\]

**Interpretation**
- Larger value => higher similarity.
- Influenced by both direction and magnitude.

**When useful**
- If embedding training objective aligns with dot-product scoring.
- Efficient in some vector DB/index settings.

### Metric selection notes
- For **normalized vectors**, cosine and dot product ranking can become equivalent.
- Check metric compatibility with embedding model recommendations.
- Ensure metric consistency between index build and query search.

---

## 5) Vector Databases (Chroma, Pinecone)

A vector database stores embeddings and supports fast similarity search (ANN) with metadata filtering.

### What vector DBs provide
- High-dimensional vector indexing.
- Top-k nearest-neighbor retrieval.
- Metadata filters (department=HR, language=en, date>=...).
- Persistence, scaling, and operational tooling.

### A) Chroma
Open-source, developer-friendly vector store often used for local or small-to-medium deployments.

**Strengths**
- Easy setup for prototypes.
- Local persistence options.
- Strong ecosystem integration for experimentation.

**Trade-offs**
- Production scaling and managed operations may require additional infrastructure planning.

**Good fit**
- Learning, prototyping, local/offline development, moderate workloads.

### B) Pinecone
Managed vector database service optimized for production-scale retrieval.

**Strengths**
- Fully managed infrastructure.
- Scalable, low-latency vector search.
- Operational convenience for production deployments.

**Trade-offs**
- Managed service cost.
- Vendor-specific deployment considerations.

**Good fit**
- Production systems needing reliability, scaling, and minimal ops overhead.

### Choosing between Chroma and Pinecone
- Pick **Chroma** for cost-conscious local development and rapid iteration.
- Pick **Pinecone** when you need managed scale, reliability, and production SLAs.

---

## 6) Mini Project: Domain-Specific RAG Assistant

### Project goal
Build a RAG assistant for a focused domain (example: **HR policy assistant**) that answers employee questions using internal policy documents.

### Example use cases
- “How many casual leaves do I get per year?”
- “What is the reimbursement limit for internet expenses?”
- “What are maternity leave eligibility rules?”

### Suggested architecture
1. **Data sources**
   - HR handbook PDFs, policy docs, FAQs, announcement emails.
2. **Ingestion pipeline**
   - Parse docs -> clean -> chunk -> embed -> index in vector DB.
3. **Query pipeline**
   - User query -> query embedding -> retrieve top-k chunks -> rerank (optional).
4. **Prompting**
   - System prompt enforces “answer only from provided context”.
   - Include citation format (doc name + section/page).
5. **LLM answer generation**
   - Return concise response + references.
6. **Evaluation loop**
   - Test set of domain questions; monitor retrieval and answer quality.

### Minimal implementation stack
- **Chunking**: token-based + overlap.
- **Embeddings**: one robust text embedding model.
- **Vector DB**: Chroma (local) or Pinecone (managed).
- **Backend**: Python FastAPI/Flask service.
- **UI**: simple chat interface (Streamlit/web app).

### Implementation checklist
- [ ] Collect and sanitize domain docs.
- [ ] Define chunk size/overlap and store metadata.
- [ ] Create ingestion script for embeddings + upsert.
- [ ] Build retrieval endpoint (top-k + filters).
- [ ] Build generation endpoint with grounding prompt.
- [ ] Add citation and “I don’t know from current docs” fallback.
- [ ] Add logging for queries and retrieved chunks.
- [ ] Run evaluation on representative domain questions.

### Evaluation metrics for the mini project
- **Retrieval hit rate@k**: Does relevant chunk appear in top-k?
- **Answer faithfulness**: Is answer supported by retrieved text?
- **Citation accuracy**: Are cited sections correct?
- **Latency**: end-to-end response time.
- **User satisfaction**: human rating of answer usefulness.

### Extensions (next steps)
- Hybrid search (keyword + vector).
- Cross-encoder reranking.
- Query rewriting for short/ambiguous questions.
- Multi-turn conversational memory.
- Role-based access control for sensitive documents.

---

## Quick Summary
- RAG improves LLM reliability by grounding outputs in retrieved domain knowledge.
- Embeddings map text into vectors used for similarity search.
- Chunking strategy heavily impacts retrieval quality.
- Cosine, Euclidean, and dot-product metrics each behave differently.
- Chroma is great for local/prototyping; Pinecone for managed production scale.
- A domain-specific mini RAG assistant should prioritize retrieval quality, grounding, citations, and evaluation.
