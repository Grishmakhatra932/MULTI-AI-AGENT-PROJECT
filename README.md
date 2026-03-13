# Multi-AI Agent using Groq and Tavily

An end-to-end **LLM-powered Multi-AI Agent application** built from scratch using **Python** and **Streamlit**, with a complete **CI/CD and cloud deployment pipeline** using **GitHub, Jenkins, SonarQube, Docker, AWS ECR, and AWS ECS**.

This project allows users to define an AI agent role, select an LLM model, optionally enable web search, and ask queries through an interactive web interface.

---

## Project Overview

The **Multi-AI Agent** project is an AI-based application that enables users to interact with intelligent agents powered by large language models. The frontend is developed using **Streamlit**, while the backend integrates **Groq API** for LLM inference and **Tavily API** for web search capabilities.

In addition to AI functionality, this project demonstrates a complete **DevOps workflow**:

- Source code management with **GitHub**
- Automated pipeline execution with **Jenkins**
- Static code quality analysis with **SonarQube**
- Application containerization with **Docker**
- Image storage in **AWS ECR**
- Container deployment on **AWS ECS**

---

## Features

- Create a custom AI agent by defining its role
- Select from multiple LLM models
- Enable or disable web search
- Ask natural language queries through a simple UI
- Integrate real-time web results using Tavily
- Automate build and deployment using Jenkins CI/CD
- Analyze code quality using SonarQube
- Deploy containerized app on AWS ECS

---

## Tech Stack

### Programming & Frontend
- Python
- Streamlit

### AI / LLM Integration
- Groq API
- Tavily API
- Prompt-based AI Agent workflow

### DevOps & Cloud
- GitHub
- Jenkins
- SonarQube
- Docker
- AWS ECR
- AWS ECS

---

## CI/CD Workflow

The project follows this pipeline:

**GitHub → Jenkins → SonarQube → Docker Build → AWS ECR → AWS ECS → Live Streamlit App**

### Pipeline Steps
1. Code is pushed to GitHub
2. Jenkins pulls the latest source code
3. SonarQube performs static code quality analysis
4. Docker builds the application image
5. The image is pushed to AWS ECR
6. AWS ECS runs the latest containerized version of the application

---

## Project Architecture

```text
User
  |
  v
Streamlit Frontend
  |
  v
Multi-AI Agent Logic
  |
  +--> Groq API (LLM response generation)
  |
  +--> Tavily API (web search)
  |
  v
Jenkins CI/CD Pipeline
  |
  +--> SonarQube Quality Analysis
  +--> Docker Image Build
  +--> AWS ECR Image Push
  +--> AWS ECS Deployment
