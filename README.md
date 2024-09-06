
# Explore Ceylon ChatBot - AI Visa Assistant (RAG Model)

This repository contains the implementation of the AI-powered Visa Assistant for the "Explore Ceylon" travel guidance app. The assistant uses a Retrieval-Augmented Generation (RAG) model to provide accurate information about Sri Lankan tourism and visa procedures.


## Features

- **RAG Model:** Retrieval-Augmented Generation model that retrieves relevant information from documents and generates accurate responses.
- **Flask API:** A simple Flask API that serves the RAG model for querying visa-related information.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- `pip` (Python package installer)
- `virtualenv` (optional, but recommended)

### 1. Clone the Repository


`git clone https://github.com/yourusername/explore-ceylon-ai-visa-assistant.git
cd explore-ceylon-ai-visa-assistant `

### 2. Set Up Virtual Environment (Optional but Recommended)


```
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\\Scripts\\activate
# On MacOS/Linux:
source venv/bin/activate`
```

### 3. Install Required Python Packages

`pip install -r requirements.txt`

### 4. Create and Set Up .env File

`OPENAI_API_KEY=your_openai_api_key_here`

### 5. Add Documents for Retrieval

Place relevant documents inside the /data directory.

### 6. Run the Flask API

`python flask_rag_api.py`




