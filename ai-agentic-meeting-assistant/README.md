# AI Meeting Preparation Agent

## Overview

The AI Meeting Preparation Agent is an agentic AI application designed to help users prepare for upcoming client meetings by automatically gathering relevant information from multiple sources and generating a concise meeting brief.

Instead of manually searching through documents, meeting notes, and historical information, users can simply ask the agent to prepare them for a meeting. The agent reasons about the request, retrieves relevant information using tools and a vector database, accesses memory, and generates a structured meeting brief.

---

## Objective

Build an AI agent capable of:

* Retrieving client information using RAG (Retrieval-Augmented Generation)
* Maintaining short-term conversational memory
* Accessing long-term memory across sessions
* Using multiple tools to gather information
* Generating a meeting preparation brief
* Demonstrating an agentic workflow involving reasoning, planning, retrieval, and tool execution

---

## Features

### RAG-Based Retrieval

* Uses Sentence Transformers to generate embeddings.
* Stores document embeddings in FAISS.
* Retrieves relevant information using semantic similarity search.

### Short-Term Memory

Maintains chat history during the current session to preserve conversation context.

Example:

```text
User: Prepare me for my meeting with Acme Corp

User: What are their current priorities?
```

The agent remembers the previous conversation context.

### Long-Term Memory

Stores client-specific information in a JSON file and retrieves it across sessions.

Example:

```json
{
  "Acme Corp": {
    "priority": "High",
    "last_meeting": "2026-05-10",
    "relationship_status": "Active Client"
  }
}
```

### Agentic Workflow

The system follows a plan-and-execute approach:

```text
User Goal
    ↓
Agent Planning
    ↓
Tool Selection
    ↓
Information Retrieval
    ↓
Memory Retrieval
    ↓
Meeting Brief Generation
```

### Multiple Tools

The agent uses the following tools:

1. Client Profile Retrieval
2. Meeting Notes Retrieval
3. Long-Term Memory Retrieval
4. Action Items Retrieval

---

## Project Structure

```text
client-meeting-agent/
│
├── Meeting_Preparation_Agent.ipynb
├── tools.py
├── memory.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── acme_profile.txt
│   ├── acme_meeting_notes.txt
│   └── acme_action_items.txt
│
├── memory/
│   └── long_term_memory.json
│
└── screenshots/
```

---

## Technologies Used

* Python
* FAISS
* Sentence Transformers
* Hugging Face Transformers
* NumPy
* JSON

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd client-meeting-agent
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
transformers
torch
numpy
```

---

## Sample Dataset

### Client Profile

Contains:

* Client name
* Industry
* Contract value
* Contact information
* Business challenges

### Meeting Notes

Contains:

* Previous meeting discussions
* Client feedback
* Upcoming review meetings

### Action Items

Contains:

* Pending tasks
* Deliverables
* Follow-up activities

### Long-Term Memory

Contains:

* Relationship status
* Priority level
* Historical client information

---

## Workflow

### Step 1: Load Documents

The system loads client-related documents.

```text
Client Profile
Meeting Notes
Action Items
```

### Step 2: Generate Embeddings

The Sentence Transformer model converts documents into vector embeddings.

Model Used:

```text
all-MiniLM-L6-v2
```

### Step 3: Store Embeddings in FAISS

Embeddings are indexed in a FAISS vector database for efficient retrieval.

### Step 4: Agent Planning

Example Query:

```text
Prepare me for my meeting with Acme Corp
```

Generated Plan:

```text
[
 'client_profile',
 'meeting_notes',
 'memory',
 'action_items'
]
```

### Step 5: Tool Execution

The agent executes the required tools and gathers information.

### Step 6: Meeting Brief Generation

The agent generates a structured meeting preparation summary.

---

## Sample Output

### User Query

```text
Prepare me for my meeting with Acme Corp
```

### Agent Plan

```text
[
 'client_profile',
 'meeting_notes',
 'memory',
 'action_items'
]
```

### Generated Brief

```text
MEETING BRIEF

CLIENT PROFILE
- Manufacturing company
- Contract value: $200,000
- Interested in predictive maintenance

KEY TALKING POINTS
- Analytics dashboard
- Faster onboarding
- Equipment downtime

OPEN ACTION ITEMS
- Share dashboard demo
- Send pricing proposal
- Schedule workshop

NEXT STEPS
- Review client requirements
- Confirm onboarding timeline
- Schedule follow-up meeting
```

---

## Screenshots

Include screenshots demonstrating:

### 1. FAISS Index Creation

```text
faiss_index.png
```

### 2. Agent Planning

```text
agent_plan.png
```

### 3. Tool Execution

```text
tool_execution.png
```

### 4. Meeting Brief Generation

```text
meeting_brief.png
```

### 5. Memory Retrieval

```text
memory_retrieval.png
```

---

## Assignment Requirements Mapping

| Requirement              | Implementation       |
| ------------------------ | -------------------- |
| RAG                      | FAISS Retrieval      |
| Vector Database          | FAISS                |
| Short-Term Memory        | chat_history         |
| Long-Term Memory         | JSON Memory Store    |
| Multiple Tools           | 4 Retrieval Tools    |
| Agentic Workflow         | Planner + Executor   |
| Tool Usage               | Tool-Based Retrieval |
| Meeting Brief Generation | Structured Summary   |

---

## Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Agentic Workflows
* Tool Calling
* Memory Management
* Information Retrieval
* AI-Based Meeting Preparation

---

## Future Improvements

Potential enhancements include:

* Support for multiple clients
* ChromaDB integration
* Streamlit web interface
* Email integration
* Calendar integration
* Real-time web search
* LLM-based planning
* Persistent database storage

---

## Conclusion

This project demonstrates how an AI agent can perform a business task through reasoning, retrieval, memory, and tool usage. By combining FAISS-based retrieval, memory systems, and agentic planning, the assistant can efficiently prepare users for client meetings and reduce the effort required to gather relevant information manually.

