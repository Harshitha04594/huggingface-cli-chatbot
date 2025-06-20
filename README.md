# huggingface-cli-chatbot
Local CLI chatbot using Hugging Face QA model

# 🤖 Hugging Face CLI Chatbot

This is a local command-line chatbot built using a Hugging Face **question-answering (QA) model**. It can answer factual questions like capital cities, and it runs fully offline using Python.


##  Features

- Uses **deepset/roberta-base-squad2** Hugging Face QA model
- Runs entirely **locally on CPU** (no internet needed during runtime)
- Maintains a simple **short-term memory** of previous conversation turns
- Easy-to-use **command-line interface (CLI)**
- Modular Python code (can be extended easily)


##  How to Set Up
 Step 1: Clone or Download the Repository

 Step 2: Install Required Packages
pip install transformers torch

How to Run the Chatbot
python interface.py

You'll see: Welcome to Hugging Face CLI Chatbot! Type /exit to quit.
User:

Sample Interaction
🤖 Welcome to Hugging Face CLI Chatbot! Type /exit to quit.

User: What is the capital of France?
Bot: Paris

User: What is the capital of Italy?
Bot: Rome

User: /exit
Bot: Exiting chatbot. Goodbye!


##  Demo Video
Watch the demo video here: [Click to View](https://drive.google.com/file/d/1c2I28n2vH_I7_fvUu2DPU3azk_-69ZBJ/view?usp=sharing)





