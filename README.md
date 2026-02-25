# EmoTalk – AI Emotional Assistant

Status: Under Active Development

An AI powered emotional assistant built during my internship at Emoneeds for mental health support.

EmoTalk is a conversational AI system designed to understand emotional conversations and respond in a meaningful and supportive way while keeping user data private.

This project was created to explore how real world AI applications work when they use their own knowledge base instead of relying only on pre trained model knowledge.

Unlike basic chatbots, EmoTalk retrieves relevant information from its own database and uses that context to generate better, more accurate, and more controlled responses.

This project represents my first complete end to end AI system built for a real world use case.

---

## Organization

This project was developed during my internship at Emoneeds, a mental health focused organization.

Website: https://www.emoneeds.com/

The goal was to explore how AI can assist in emotional and mental health related conversations while maintaining privacy and system control.

EmoTalk is currently under active development.

---

## Project Objective

The main objective of building EmoTalk was to understand how modern AI systems work internally, including:

• How language models generate responses  
• How private knowledge bases are used  
• How vector databases store and retrieve information  
• How Retrieval Augmented Generation works in real applications  
• How all components connect to form a complete AI product  

This project was built as both a learning experience and a real world implementation.

---

## How It Works

The system follows a Retrieval Augmented Generation architecture.

Step 1: User sends a message  
Step 2: System converts the message into embeddings  
Step 3: System searches the vector database for relevant context  
Step 4: Relevant information is retrieved  
Step 5: Both user query and retrieved context are sent to the language model  
Step 6: Language model generates a response  
Step 7: Response is sent back to the user  

This allows the assistant to use its own knowledge base to generate better responses.

---

## Features

• Real time emotional conversation support  

• Private knowledge base integration  

• Context aware response generation  

• Retrieval Augmented Generation (RAG) architecture  

• Modular and scalable backend  

• Voice support (currently in development)  

• Secure and controlled response system  

---

## Tech Stack

### Backend
Python  
Flask  

### AI / ML
LangChain  
Groq LLM  
HuggingFace Embeddings  

### Database
Pinecone Vector Database  

### Frontend
HTML  
CSS  
JavaScript  

---

## System Architecture

User Input  
↓  
Embedding Model  
↓  
Vector Database  
↓  
Context Retrieval  
↓  
Language Model  
↓  
Final Response  

---

## What I Learned

This project helped me gain practical understanding of real AI engineering.

I learned:

• How LLM based systems work  

• How vector databases work  

• How embeddings work  

• How Retrieval Augmented Generation works  

• How to build AI backend systems  

• How to connect frontend and backend  

• How real AI products are built  

This project helped me move from theory to real implementation.

---

## Current Status

Project is under active development.

Currently working on:

• Voice interaction  

• Performance optimization  

• Deployment  

• Improving response quality  

• Scalability  

---

## Future Plans

• Deploy as live web application  

• Add real time voice conversation  

• Improve emotional intelligence  

• Improve performance  

• Add authentication system  

• Make production ready  

---

## Screenshots

(Add screenshots here)

Example:

Chat Interface  

Voice Feature  

System Architecture  

---

## Installation and Setup

Clone repository

git clone https://github.com/Shailesh1811/Emoneeds-virtual-doctor

Go to folder

cd emotalk

Install dependencies

pip install -r requirements.txt

Run application

python app.py

---

## Why This Project Matters

This project demonstrates:

• LLM integration  

• RAG architecture  

• Vector database usage  

• AI backend development  

• Real world AI system building  

This is not just a chatbot. It is a complete AI system.

---

## Author

Shailesh Dwivedi

This project was built during my internship at Emoneeds.

This is my first and dream project in AI engineering.

I am continuously improving it.

---

## Contact

GitHub repo: https://github.com/Shailesh1811/Emoneeds-virtual-doctor

LinkedIn: https://www.linkedin.com/in/shailesh-dwivedi-184bb5214/
---