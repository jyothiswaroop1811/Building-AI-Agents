# Conversational RAG Assistant with Tool Calling

## Overview

This project implements a Conversational Retrieval-Augmented Generation (RAG) Assistant capable of:

* Answering questions from a PDF document
* Maintaining conversation history
* Understanding follow-up questions
* Rewriting follow-up questions into standalone questions
* Using external tools when required
* Routing queries between document retrieval and tool execution

The project demonstrates the core concepts behind modern AI assistants and AI agents.

---

# Features

### 1. Conversational Memory

The assistant maintains chat history and remembers previous interactions.

**Example**

User:

```text
What is RAG?
```

User:

```text
Can you explain it more?
```

The assistant understands that "it" refers to "RAG".

---

### 2. History-Aware Retrieval

Follow-up questions are converted into standalone questions before retrieval.

**Example**

Input:

```text
Can you explain it more?
```

Rewritten:

```text
What is RAG? Can you explain it more?
```

---

### 3. Retrieval-Augmented Generation (RAG)

The assistant:

* Reads a PDF document
* Splits text into chunks
* Generates embeddings
* Stores embeddings in FAISS
* Retrieves relevant chunks
* Uses retrieved context to answer questions

---

### 4. Tool Calling

The assistant can invoke external tools when required.

Implemented Tool:

```python
get_current_time()
```

Example:

```text
User: What is the current time?
```

The assistant calls the tool and returns the result.

---

### 5. Routing Logic

The system decides whether to:

* Answer from retrieved PDF content
* Execute an external tool

---

# Project Structure

```text
conversational-rag-assistant/
│
├── Conversational_RAG_Assistant.ipynb
├── tools.py
├── README.md
├── requirements.txt
├── sample_data/
│   └── sample.pdf
├── screenshots/
│   ├── retrieval_answer.png
│   ├── followup_question.png
│   └── tool_call.png
```

---

# Technologies Used

* Python
* Jupyter Notebook
* LangChain
* Sentence Transformers
* FAISS
* Hugging Face Transformers
* PyPDF
* NumPy

---

# RAG Workflow

```text
PDF Document
      ↓
Text Extraction
      ↓
Chunking
      ↓
Embedding Generation
      ↓
FAISS Vector Database
      ↓
User Question
      ↓
Question Rewriting
      ↓
Semantic Retrieval
      ↓
Context Retrieval
      ↓
LLM
      ↓
Answer
```

---

# Tool Calling Workflow

```text
User Question
      ↓
Tool Detection
      ↓
Execute Tool
      ↓
Tool Response
      ↓
Final Answer
```

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd conversational-rag-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

1. Place a PDF file inside:

```text
sample_data/sample.pdf
```

2. Open:

```text
Conversational_RAG_Assistant.ipynb
```

3. Run all cells sequentially.

4. Start chatting with the assistant.

5. Type:

```text
exit
```

to stop the chatbot.

---

# Sample Queries

### Retrieval-Based Questions

```text
What are input devices?
```

```text
Explain computer hardware.
```

```text
What is software?
```

---

### Follow-Up Questions

```text
What is RAG?
```

```text
Explain it more.
```

---

### Tool-Based Questions

```text
What is the current time?
```

```text
Tell me today's date and time.
```

---

# JSON Tool Schema

```python
tool_schema = {
    "name": "get_current_time",
    "description": "Returns the current date and time",
    "parameters": {
        "type": "object",
        "properties": {}
    }
}
```

---

# Key Concepts Demonstrated

* Conversational Memory
* Chat History Management
* History-Aware Retrieval
* Semantic Search
* Vector Databases
* Prompt Engineering
* Tool Calling
* Function Execution Loop
* Routing Logic
* Retrieval-Augmented Generation (RAG)

---

# Screenshots

The following screenshots are included:

1. Retrieval-based answer
2. Follow-up conversational question
3. Successful tool call

---

# Future Improvements

* Multiple tool support
* Weather API integration
* Calculator tool
* ChromaDB integration
* Persistent chat history using SQLite
* Streamlit web interface
* Source citation support
* Multi-document retrieval

---

# Conclusion

This project demonstrates a complete Conversational RAG Assistant capable of combining document retrieval, conversational memory, history-aware retrieval, and tool calling. It provides a practical introduction to the foundational concepts used in modern AI assistants and agent-based systems.

