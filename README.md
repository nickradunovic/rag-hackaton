# LLM Hackathon with Retrieval Augmented Generation (RAG)

## Overview

Welcome to the Large Language Model (LLM) Hackathon repository! This hackathon is organized as part of Bastiaan's LLM session at Future Facts. The primary focus is on implementing and utilizing Retrieval Augmented Generation (RAG) techniques for Large Language Models (LLMs). The ultimate goal is to integrate RAG into an existing LLM and showcase its application through a user-friendly interface developed with either Gradio or Streamlit.

### How RAG Works

Traditional language models generate text based on learned patterns and context. RAG takes this a step further by introducing a retrieval mechanism. Here's a simplified overview of how it works:

1. **Retrieval:** The model performs an initial retrieval step to gather contextually relevant information from a knowledge base or external documents.

2. **Augmentation:** The retrieved information is then seamlessly integrated into the generation process, augmenting the model's understanding and improving the quality of generated content.

3. **Generation:** The model generates text, now equipped with the additional knowledge obtained through retrieval, resulting in more informed and contextually rich output.

### Usage of LlamaIndex for RAG

[LlamaIndex](https://github.com/run-llama/llama_index) is a data framework for Large Language Models (LLMs) based applications. LLMs like GPT-4 come pre-trained on massive public datasets, allowing for incredible natural language processing capabilities out of the box. However, their utility is limited without access to your own private data.

LlamaIndex lets you ingest data from APIs, databases, PDFs, and more via flexible data connectors. This data is indexed into intermediate representations optimized for LLMs. LlamaIndex then allows natural language querying and conversation with your data via query engines, chat interfaces, and LLM-powered data agents. It enables your LLMs to access and interpret private data on large scales without retraining the model on newer data.

### How LlamaIndex Works?
LlamaIndex uses Retrieval Augmented Generation (RAG) systems that combine large language models with a private knowledge base. It generally consists of two stages: the indexing stage and the querying stage.

#### Indexing stage
LlamaIndex will efficiently index private data into a vector index during the indexing stage. This step helps create a searchable knowledge base specific to your domain. You can input text documents, database records, knowledge graphs, and other data types.

Essentially, indexing converts the data into numerical vectors or embeddings that capture its semantic meaning. It enables quick similarity searches across the content.

#### Querying stage
During the querying stage, the RAG pipeline searches for the most relevant information based on the user's query. This information is then given to the LLM, along with the query, to create an accurate response.

This process allows the LLM to have access to current and updated information that may not have been included in its initial training.

The main challenge during this stage is retrieving, organizing, and reasoning over potentially multiple knowledge bases.

### Before you start coding

Make sure to read the README fully, study the provided code in this repository, and have a look at the steps and information included in (this)[https://www.datacamp.com/tutorial/llama-index-adding-personal-data-to-llms] tutorial. 

## Hackathon Details

### Timeline

- **Start Date:** December 15th, 11:00 AM
- **End Date:** December 15th, 1:00 PM

### Objective

The primary objective of this hackathon is to enhance our understanding and practical skills in implementing Retrieval Augmented Generation (RAG) for Large Language Models. Participants will make teams of two and will be tasked with integrating RAG into a provided LLM and creating a user interface to demonstrate the application.

### Technologies/Frameworks

- **Language Models:** Utilize GPT-3.5 as the LLM for this assignment.
- **Retrieval Augmented Generation (RAG):** Implement RAG techniques to improve the LLM's performance on `<insert data source>`.
- **User Interface:** Choose between Gradio or Streamlit for creating an interactive UI.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/nickradunovic/llm-hackathon-rag.git
   cd llm-hackathon-rag
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv .env
   source .env/bin/activate
   ```

3. **Install Dependencies::**
   ```bash
   pip install -r requirements.txt
   ```