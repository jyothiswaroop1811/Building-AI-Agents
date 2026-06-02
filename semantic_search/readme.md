# FAISS Semantic Search Engine

## Overview

This project implements a mini Semantic Search Engine using Sentence Transformers and FAISS. The system converts text into vector embeddings, stores them in a FAISS index, and retrieves the most semantically similar knowledge base entries for a user query.

The project demonstrates the core retrieval component used in modern Retrieval-Augmented Generation (RAG) systems and vector databases.

---

## Objectives

* Generate sentence embeddings using a pre-trained transformer model.
* Store embeddings in a FAISS vector index.
* Perform semantic similarity search.
* Retrieve the Top-K most relevant results.
* Build an interactive command-line search application.

---

## Technologies Used

* Python
* Sentence Transformers
* FAISS
* NumPy

---

## Project Structure

```text
faiss-semantic-search/
│
├── semantic_search.py
├── theory_answers.md
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the Repository

```bash
git clone <your-repository-url>
cd faiss-semantic-search
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Dependencies

```text
sentence-transformers
faiss-cpu
numpy
torch
```

---

## Knowledge Base

The application uses a small customer-support knowledge base containing information related to:

* Password Reset
* Billing and Invoices
* Account Management
* Login Issues
* Security Settings
* Subscription Plans
* Refund Requests
* Account Deletion
* Customer Support
* Profile Management

---

## Implementation Steps

### 1. Generate Embeddings

The project uses the Sentence Transformer model:

```python
all-MiniLM-L6-v2
```

to convert each knowledge-base sentence into a 384-dimensional vector representation.

Example Output:

```text
Embedding Matrix Shape:
(10, 384)
```

---

### 2. Create a FAISS Index

A FAISS IndexFlatL2 index is created:

```python
index = faiss.IndexFlatL2(384)
```

Embeddings are normalized before indexing to support cosine-similarity-like behavior.

```python
faiss.normalize_L2(embeddings)
```

---

### 3. Semantic Search

For each user query:

1. Generate query embedding.
2. Normalize query embedding.
3. Search the FAISS index.
4. Retrieve the Top 3 most relevant results.

Example:

```text
Query:
How can I reset my password?

Results:
1. You can reset your password using the forgot password link.
2. Login issues can occur due to incorrect credentials.
3. Two-factor authentication improves account security.
```

---

### 4. Interactive Search

The application supports continuous querying through a command-line interface.

Example:

```text
Enter Query:
How do I update my email address?

Top Matches:
1. Users can update their email address from account settings.
2. Profile information can be edited from the profile page.
3. You can contact support through the help center.
```

Type:

```text
exit
```

to terminate the application.

---

## Sample Queries

```text
How do I reset my password?
```

```text
Where can I view my invoices?
```

```text
How can I delete my account?
```

```text
How do I contact support?
```

---

## Key Concepts Learned

* Sentence Embeddings
* Vector Databases
* FAISS Indexing
* Semantic Search
* Similarity Metrics
* Cosine Similarity
* Nearest Neighbour Search
* Information Retrieval

---

## Screenshots

Add screenshots demonstrating:

1. Embedding generation output
2. FAISS index creation
3. Password reset query
4. Billing-related query
5. Account deletion query
6. Interactive CLI execution

Example structure:

```text
screenshots/
├── embedding_generation.png
├── faiss_index.png
├── password_query.png
├── billing_query.png
└── account_query.png
```

---

## Learning Outcomes

By completing this project, you will understand:

* How text is converted into embeddings.
* How vector databases store embeddings.
* How FAISS performs similarity search.
* Why semantic search is superior to keyword matching.
* How retrieval systems work in modern AI applications.

---

## Future Enhancements

Possible improvements include:

* Support for larger knowledge bases.
* Use of Approximate Nearest Neighbour (ANN) indexes.
* Integration with PDFs and document retrieval.
* Building a complete Retrieval-Augmented Generation (RAG) chatbot.
* Web-based user interface using Streamlit.

---

## Conclusion

This project demonstrates the fundamental retrieval workflow used in modern AI systems. By combining Sentence Transformers with FAISS, we can efficiently perform semantic search and retrieve contextually relevant information, forming the foundation of production-grade RAG applications and vector search engines.

