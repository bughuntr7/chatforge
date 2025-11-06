# 🔥 ChatForge
> Scalable AI Chatbot API built with Flask, OpenAI, and vector memory — designed for modular full-stack integration.

[![Build Status](https://img.shields.io/github/actions/workflow/status/bughuntr7/chatforge/ci.yml?branch=main)](https://github.com/bughuntr7/chatforge/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 🧠 Overview
ChatForge is an intelligent conversational backend built for developers who want to integrate AI chat capabilities into any application.  
It supports hybrid LLMs, contextual memory, modular API routes, and can be easily containerized for scalable deployment.

> 🧩 Originally inspired by [@legendarystar143590](https://github.com/legendarystar143590)'s chatbot architecture.  
> Re-engineered and extended by **[@bughuntr7](https://github.com/bughuntr7)**.

---

## ⚙️ Features
- Modular Flask API for chat endpoints  
- Contextual memory layer (FAISS or Chroma)  
- Switch between local and cloud LLMs  
- Logging and analytics middleware  
- Dockerized for scalable deployment  
- CI/CD ready with GitHub Actions  

---

## 🧩 Setup & Environment

### 1️⃣ Install Dependencies
Make sure you're using **Python 3.10+**, run:
```bash
pip install -r requirements.txt
```

### 2️⃣ Environment Variables
Create a `.env` file in the project root and set your API keys:

```bash
OPENAI_API_KEY=
UPLOAD_FOLDER=
SERPER_API_KEY=
STORM_GLASS_API_KEY=
```

> 💡 You can also use `.env.example` as a template — included in the repo.

---

## 💻 Running Locally
After setting up your environment variables, run this:

```bash
python app.py
```

Your ChatForge backend will be available at:
➡️ **http://localhost:5000**

---

## 🚀 Running in Production
For a production-grade deployment with multiple workers:

```bash
pm2 start "gunicorn -w 8 -t 16 -b 0.0.0.0:5000 --timeout 600 app:app"
```

This runs Gunicorn with 8 workers and a 600-second timeout, managed by PM2 for reliability and monitoring.

---

## 🧩 Example Request

```bash
POST /api/chat
Content-Type: application/json

{
  "session_id": "user_1234",
  "message": "Tell me a joke about engineers."
}
```

## 📚 API Documentation

Interactive API documentation is available at:
➡️ **http://localhost:5000/api/docs/**

The Swagger UI provides:
- Complete API endpoint documentation
- Request/response schemas
- Try-it-out functionality
- Authentication support

---

## 🧱 Tech Stack
- **Backend**: Flask (Python 3.10+)
- **AI**: OpenAI API, LangChain, FAISS
- **Infra**: Docker, GitHub Actions, .env config

---

## 🛠️ Roadmap
- [ ] Vector memory integration
- [ ] Async WebSocket streaming
- [ ] Custom LLM fine-tuning support
- [ ] Frontend demo with React

---

<p align="center"><em>Built to forge conversations — intelligent, scalable, and yours.</em></p>
