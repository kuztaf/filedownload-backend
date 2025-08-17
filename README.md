# 🚀 filedownload-backend

Backend for file management and download using FastAPI, Celery, RabbitMQ, and MySQL.

## 🛠 Technologies & Tools

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Celery](https://img.shields.io/badge/-Celery-37814A?style=flat-square&logo=celery&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/-RabbitMQ-FF6600?style=flat-square&logo=rabbitmq&logoColor=white)
![MySQL](https://img.shields.io/badge/-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

---

## ✨ Features

- RESTful API for user and document management
- Asynchronous task processing with Celery
- Service communication with RabbitMQ
- Data persistence in MySQL
- Task monitoring with Flower

---

## ⚡ Quick Start with Docker

```bash
docker compose up --build -d
```

This will install all dependencies and start the required services.

### Service Access

- FastAPI: http://localhost:8000
- Swagger Docs: http://localhost:8000/docs
- Flower: http://localhost:5555
- RabbitMQ: http://localhost:15672 (user/password: guest/guest)
- MySQL: localhost:3306 (user: user, password: password, database: documentdb)

To stop and clean everything:

```bash
docker compose down -v
```

---

## 🧑‍💻 Local Installation (without Docker)

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Adjust the connection string in `api/db/database.py` according to your local environment.
4. Run FastAPI:
   ```bash
   uvicorn api.main:app --reload
   ```

---

## ℹ️ Notes

- Make sure the MySQL port is not already in use by another local instance.
- You can change the ports in `docker-compose.yml` as needed.

---

Developed by kuztaf
