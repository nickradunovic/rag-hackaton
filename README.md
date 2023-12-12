# LLM Hackathon with Retrieval Augmented Generation (RAG)

## Overview

Welcome to the Large Language Model (LLM) Hackathon repository! This hackathon is organized as part of Bastiaan's LLM session at Future Facts and focuses on integrating Retrieval Augmented Generation (RAG) in Large Language Models. In three hours, this session wil help enhance our understanding and practical skills in implementing Retrieval Augmented Generation (RAG) for LLMs while getting hands-on experience with UI building tools like Streamlit. Each made application shall be demonstrated with a user-friendly interface developed with either Gradio or Streamlit.

### How RAG Works

Traditional language models generate text based on learned patterns and context. RAG takes this a step further by introducing a retrieval mechanism. Here's a simplified overview of how it works:

1. **Retrieval:** The model performs an initial retrieval step to gather contextually relevant information from a knowledge base or external documents.

2. **Augmentation:** The retrieved information is then seamlessly integrated into the generation process, augmenting the model's understanding and improving the quality of generated content.

3. **Generation:** The model generates text, now equipped with the additional knowledge obtained through retrieval, resulting in more informed and contextually rich output.

### Usage of LlamaIndex for RAG

[LlamaIndex](https://github.com/run-llama/llama_index) is a data framework for Large Language Models (LLMs) based applications. LLMs like GPT-4 come pre-trained on massive public datasets, allowing for incredible natural language processing capabilities out of the box. However, their utility is limited without access to your own private data.

LlamaIndex lets you ingest data from APIs, databases, PDFs, and more via flexible data connectors. This data is indexed into intermediate representations optimized for LLMs. LlamaIndex then allows natural language querying and conversation with your data via query engines, chat interfaces, and LLM-powered data agents. It enables your LLMs to access and interpret private data on large scales without retraining the model on newer data.

### Before you start coding

Make sure to read the README fully, study the provided code in this repository, and have a look at the steps and information included in (this)[https://www.datacamp.com/tutorial/llama-index-adding-personal-data-to-llms] tutorial. **TIP:** LlamaIndex has built-in functionality to utilize the GPT-series models.

## Hackathon Details

### Timeline

- **Start Date:** December 15th, 11:00 AM
- **End Date:** December 15th, 1:00 PM

### Objective

Participants will form teams of two and will be tasked with incorporating RAG into a LLM of their choice using LlamaIndex. Additionally, each team is empowered to select their preferred data sources, such as documents, books, Wiki pages, and LinkedIn-generated resumes, to enhance the LLM's knowledge base.

Once RAG is successfully implemented, the model should demonstrate its capability to answer questions related to the material exclusively provided in the external documents. To showcase the application, participants are required to construct a user interface using Streamlit (or Gradio based on individual preferences).


### Technologies/Frameworks

- **Language Models:** Utilize a LLM of choice (e.g., GPT-3.5) for this assignment.
- **Retrieval Augmented Generation (RAG):** Use LlamaIndex to implement RAG techniques to improve the LLM's performance on `<insert data source>`.
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