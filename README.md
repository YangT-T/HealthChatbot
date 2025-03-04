# Health Chatbot
## Introduction
### APP
This directory is a web application developed by flask.

Partly based on LangChain, [reference](https://www.langchain.asia/use_cases/chatbots/quickstart) here.

Use ``all-MiniLM-L6-v2`` embeddings ans FAISS database

Uses Qwen LLM so you should get and set your API_KEY in ``.env`` file

### Scripts
Scripts used in data collection and cleansing

### Data
This includes a simple dataset example

## Setup

0 Try to install all required libs

1 Enter ``HealthChatBot/`` directory

2 Run ``python ./Scripts/updateDatabaseExample.py`` to get the embeddings of the DialMed dataset and store them into vector database

3 Run python ``./App/app.py``