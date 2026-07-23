# Week 2: FastAPI App & Dockerization
<br>
Simple FastAPI application configured with tasks, environment variables, PostgreSQL database, and containerization.
<br>
## Files & Structure
* `.env`: Environment variables configuration<br>
* `main.py`: Combined application code containing Task 1 (Environment variables) and Task 2 (PostgreSQL database integration)<br>
* `main.py1`: Task 1 legacy reference code<br>
* `main.py2`: Task 2 legacy reference code<br>
* `Dockerfile`: Container configuration for the FastAPI application (Task 3)<br>
* `docker-compose.yml`: Multi-container orchestration for FastAPI and PostgreSQL (Task 4 & 5)<br>
* `requirements.txt`: Project dependencies<br>
## Completed Tasks
<br>
* **Task 1:** FastAPI route configured with environment variables (`main.py` / `main.py1`).<br>
* **Task 2:** Database integration with SQLAlchemy models and items creation endpoint (`main.py` / `main.py2`).<br>
* **Task 3:** Dockerfile created to containerize the FastAPI application.<br>
* **Task 4 & 5:** Docker Compose setup with multi-service architecture (FastAPI + PostgreSQL) and live-reload bind-mounts.<br>

## How to Run with Docker<br>
```bash
docker compose up --build
