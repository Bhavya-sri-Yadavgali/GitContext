# GitContext — Codebase Intelligence & Developer Copilot

**Understand any codebase. Find relevant code. Get answers backed by source-code evidence.**

GitContext is an AI-powered codebase intelligence system designed to help developers understand large and unfamiliar software repositories.

Instead of relying only on keyword searches or manually navigating files, GitContext combines semantic search, keyword retrieval, code structure analysis, and reranking to retrieve relevant code and generate context-aware answers with source-code citations.

The goal is to build a reliable developer copilot that understands not just individual code snippets, but also the relationships and dependencies between different parts of a codebase.

## Problem Statement

Understanding an unfamiliar codebase can be difficult and time-consuming.

Developers often need to:
- Find where a particular feature is implemented.
- Understand how functions interact with each other.
- Trace dependencies across multiple files.
- Locate error handling and business logic.
- Understand the impact of changes in one part of the application.

Traditional keyword search can miss code that expresses the same concept using different terminology. Basic semantic search, on the other hand, can struggle with exact function names, identifiers, and error codes.

GitContext aims to address these limitations through a hybrid code retrieval and reasoning pipeline.

## Key Objectives

- Understand source code at the function and structural level.
- Generate meaningful code chunks instead of splitting files arbitrarily.
- Build semantic representations of code using embeddings.
- Combine vector search with BM25 keyword retrieval.
- Rerank retrieved code chunks based on query relevance.
- Preserve relationships between functions through dependency analysis.
- Generate answers supported by retrieved source-code evidence.
- Evaluate retrieval quality, answer correctness, and citation accuracy.

## System Architecture

```text
                 GitHub Repository
                         |
                         v
               Code Parsing (AST)
                         |
                         v
                Intelligent Chunking
                         |
                         v
              Metadata + Code Graph
                         |
                         v
                    Embeddings
                         |
              +----------+----------+
              |                     |
              v                     v
         Vector Search          BM25 Search
              |                     |
              +----------+----------+
                         |
                         v
                    Rank Fusion
                         |
                         v
                      Reranker
                         |
                         v
                Dependency Expansion
                         |
                         v
                  Context Assembly
                         |
                         v
                  Language Model
                         |
                         v
               Answer + Citations
                         |
                         v
                     Evaluation
```

## Core Components

### 1. Code Understanding and Parsing
- Parse source files using Abstract Syntax Trees (AST).
- Identify functions, classes, and structural boundaries.
- Extract useful metadata such as filenames and line numbers.

### 2. Intelligent Code Chunking
- Split source code into meaningful units instead of arbitrary character-based chunks.
- Preserve function and class boundaries.
- Retain contextual information needed to understand individual chunks.

### 3. Embeddings and Semantic Search
- Convert code chunks and user queries into vector representations.
- Retrieve code based on semantic similarity.
- Identify relevant code even when the query uses different terminology.

### 4. Hybrid Retrieval
Combine two complementary retrieval techniques:

- **Vector Search:** Finds code based on semantic meaning.
- **BM25:** Finds code based on keyword and identifier relevance.

Use rank fusion to combine the results from both retrieval systems.

### 5. Reranking
Use a reranking model to evaluate the relevance of retrieved candidates against the original query and improve the final retrieval order.

### 6. Dependency-Aware Retrieval
Analyze relationships between functions and other code components.

For example:

```text
login_user()
    |
    +---- find_user()
    |
    +---- verify_password()
    |
    +---- create_session()
```

This helps retrieve related code that may be necessary to understand a particular operation.

### 7. Answer Generation with Citations
Use the retrieved code context to generate answers grounded in the repository.

Answers should identify relevant source files and code locations, rather than relying on unsupported assumptions.

### 8. Evaluation and Reliability
Evaluate the system using measurable metrics:

| Area | Metrics |
|---|---|
| Retrieval | Recall@K, Precision@K |
| Ranking | Mean Reciprocal Rank (MRR) |
| Generation | Answer correctness |
| Grounding | Citation accuracy, unsupported claims |
| Performance | Retrieval latency, total response time |

The system should also identify when retrieved evidence is insufficient and avoid generating unsupported answers.

## Technology Stack

The stack will evolve as the project develops.

| Component | Technology |
|---|---|
| Programming Language | Python |
| Code Parsing | Python AST |
| Embedding Models | Sentence Transformers |
| Semantic Retrieval | Vector Search |
| Keyword Retrieval | BM25 |
| Reranking | Cross-Encoder |
| API Layer | FastAPI |
| Vector Database | To be selected |
| Evaluation | Custom evaluation pipeline |

## Development Roadmap

- [x] Understand embedding fundamentals.
- [x] Implement a basic semantic search experiment.
- [x] Explore AST-based code chunking.
- [x] Understand code dependency extraction.
- [x] Study hybrid retrieval and BM25.
- [x] Understand reranking.
- [x] Study RAG evaluation metrics.
- [ ] Implement scalable vector retrieval.
- [ ] Integrate a vector database.
- [ ] Implement complete hybrid retrieval.
- [ ] Integrate reranking into the retrieval pipeline.
- [ ] Implement dependency-aware context assembly.
- [ ] Integrate an LLM for grounded answer generation.
- [ ] Add source-code citations.
- [ ] Build a FastAPI backend.
- [ ] Implement evaluation and failure analysis.
- [ ] Add GitHub repository ingestion and incremental indexing.

## Project Philosophy

GitContext is being developed with a focus on understanding and engineering reliable AI systems.

The emphasis is not simply on connecting an LLM to a codebase. It is on understanding how retrieval works, why it fails, how to evaluate it, and how to improve the system through measurable experiments.

**The objective is to build a codebase assistant that developers can trust, not just one that generates convincing answers.**

---

*Status: Under Development*  
