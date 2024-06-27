# Build an LLM RAG Chatbot With LangChain

This project builds a Retrieval-Augmented Generation (RAG) chatbot using LangChain, as detailed in the [Real Python tutorial](https://realpython.com/build-llm-rag-chatbot-with-langchain/).

## Project Overview

This project demonstrates how to create a chatbot that leverages large language models (LLMs) and Neo4j graph databases to provide insightful responses based on complex medical data. The chatbot can understand and generate human-like text, thanks to OpenAI's GPT-3.5 models, and efficiently retrieve relevant information from a Neo4j AuraDB instance.

## Features

- **Language Model Integration:** Utilizes OpenAI's GPT-3.5 models for natural language understanding and generation.
- **Graph Database Querying:** Connects to a Neo4j AuraDB instance to fetch and analyze structured data.
- **Dockerized Deployment:** Simplifies setup and deployment using Docker Compose.
- **Streamlit UI:** Provides a user-friendly interface for interacting with the chatbot.

## Setup

### Prerequisites

1. **OpenAI API Key:** Create an [OpenAI API key](https://realpython.com/generate-images-with-dalle-openai-api/#get-your-openai-api-key) and store it as `OPENAI_API_KEY`.
2. **Neo4j AuraDB Instance:** Set up a free instance of Neo4j AuraDB by following [these instructions](https://neo4j.com/cloud/platform/aura-graph-database/?ref=docs-nav-get-started).

### Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

```.env
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>

NEO4J_URI=<YOUR_NEO4J_URI>
NEO4J_USERNAME=<YOUR_NEO4J_USERNAME>
NEO4J_PASSWORD=<YOUR_NEO4J_PASSWORD>

HOSPITALS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/hospitals.csv
PAYERS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/payers.csv
PHYSICIANS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/physicians.csv
PATIENTS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/patients.csv
VISITS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/visits.csv
REVIEWS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/reviews.csv

HOSPITAL_AGENT_MODEL=gpt-3.5-turbo-1106
HOSPITAL_CYPHER_MODEL=gpt-3.5-turbo-1106
HOSPITAL_QA_MODEL=gpt-3.5-turbo-0125

CHATBOT_URL=http://host.docker.internal:8000/hospital-rag-agent
```

### Running the Project

Ensure you have Docker Compose installed by following [these directions](https://docs.docker.com/compose/install/). After setting up the environment variables and the Neo4j AuraDB instance, you can run the project with the following commands:

```console
$ docker-compose up --build
```

After the containers have been built and started, you can access the chatbot API at `http://localhost:8000/docs` and the Streamlit app at `http://localhost:8501/`.

This project showcases how advanced language models and graph databases can be integrated to build intelligent applications capable of understanding and processing complex datasets.