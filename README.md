# 🚀 Assignment 2 – Basic Backend API with Docker

## 📌 Overview

This project demonstrates the development of a simple backend API using **FastAPI** and its containerization using **Docker**. The application runs inside a Docker container and can be accessed through mapped ports.

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
│── video.mp4
```

---

## 🎥 Screencast Video

The complete working demonstration of the project is included below:

👉 Download and watch:

```
video.mp4
```

---

## 🔗 API Endpoints

| Endpoint     | Method | Description                 |
| ------------ | ------ | --------------------------- |
| `/`          | GET    | Returns Hello World message |
| `/data`      | GET    | Returns sample JSON data    |
| `/data/{id}` | GET    | Returns item by ID          |

---

## ⚙️ Running the Application

### 1️⃣ Build Docker Image

```
docker build -t iitm_assignment2 .
```

### 2️⃣ Run Docker Container

```
docker run -p 8000:8000 iitm_assignment2
```

---

## 🌐 Access the API

* http://localhost:8000
* http://localhost:8000/data
* http://localhost:8000/docs

---

## 📦 Dockerfile Explanation

* **FROM python:3.10** → Base image with Python
* **WORKDIR /usr/src/app** → Working directory inside container
* **COPY requirements.txt .** → Copy dependencies
* **RUN pip install -r requirements.txt** → Install dependencies
* **COPY main.py .** → Copy application code
* **EXPOSE 8000** → Expose port
* **CMD** → Run FastAPI app using Uvicorn

---

## 🧠 Key Concepts

* REST API development using FastAPI
* Docker containerization
* Port mapping between host and container
* Running applications in isolated environments

---

## ✅ Conclusion

This project successfully demonstrates how to build, containerize, and run a backend API using Docker.
