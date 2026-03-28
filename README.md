# 🚀 Assignment 2 – Basic Backend API with Docker

## 📌 Overview

This project demonstrates the creation of a simple backend API using **FastAPI** and its deployment using **Docker**. The application is containerized to ensure consistent execution across different environments.

---

## 🛠️ Tech Stack

* Python 3.10
* FastAPI
* Uvicorn
* Docker

---

## 📂 Project Structure

```
assignment__2/
│── main.py
│── requirements.txt
│── Dockerfile
│── README.md
```

---

## 🔗 API Endpoints

| Endpoint     | Method | Description                   |
| ------------ | ------ | ----------------------------- |
| `/`          | GET    | Returns a Hello World message |
| `/data`      | GET    | Returns sample JSON data      |
| `/data/{id}` | GET    | Returns item by ID            |

---

## ⚙️ Running the Application with Docker

### 1️⃣ Build Docker Image

```
docker build -t iitm_assignment2 .
```

### 2️⃣ Run Docker Container

```
docker run -p 8000:8000 iitm_assignment2
```

---

## 🌐 Access the Application

Once the container is running, open your browser:

* http://localhost:8000
* http://localhost:8000/data
* http://localhost:8000/docs

---

## 🧠 Key Concepts Covered

* Building REST APIs using FastAPI
* Containerizing applications using Docker
* Port mapping between host and container
* Running applications inside isolated environments

---

## 📦 Dockerfile Explanation

* **FROM python:3.10** → Base image with Python installed
* **WORKDIR /usr/src/app** → Sets working directory inside container
* **COPY requirements.txt .** → Copies dependency file
* **RUN pip install -r requirements.txt** → Installs dependencies
* **COPY main.py .** → Copies application code
* **EXPOSE 8000** → Exposes application port
* **CMD** → Runs the FastAPI application using Uvicorn

---

## ✅ Conclusion

This project successfully demonstrates how to build and containerize a backend API, making it portable and easy to deploy in different environments.
