# AI Agent

**Your perfect AI agent**

## Overview

AI Agent is a Python-based project designed to create an intelligent agent capable of processing and understanding documents. The agent utilizes various modules to load documents, plan actions, and retrieve relevant information.

## Features

- **Document Loading**: Efficiently loads and preprocesses documents for analysis.
- **Planning Module**: Determines the sequence of actions the agent should take based on the input.
- **Memory Management**: Stores and retrieves information to maintain context over time.
- **Retrieval-Augmented Generation (RAG)**: Enhances responses by retrieving relevant documents from a knowledge base.

## Project Structure

ai-agent/
├── app.py                 # Main application script
├── document_loader.py     # Module for loading and preprocessing documents
├── planner.py             # Planning module for action determination
├── rag_chroma.py          # RAG implementation using Chroma
├── memory/                # Directory for memory management components
└── __pycache__/           # Compiled Python files


## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages (see `requirements.txt`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/TrishKedi/ai-agent.git
   cd ai-agent
   ```

2. Install dependencies:
    
    ```pip install -r requirements.txt```

3. Run the application:
     
     ```python app.py```



