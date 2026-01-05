# 🚀 DATA-PIPELINE-PYSPARK-FASTAPI

A scalable **Data Pipeline and REST API project** combining **Apache PySpark** for distributed data processing with **FastAPI** for serving results via HTTP. This project demonstrates a real-world data engineering workflow: ingesting, transforming, and serving data, fully containerized for easy setup using Docker.

---

## 🔍 Features

✔︎ Distributed Data Processing with PySpark
✔︎ REST API built with FastAPI (async & modern Python framework)
✔︎ Modular pipeline code under **pipeline/**
✔︎ API application under **app/**
✔︎ Automated tests under **tests/**
✔︎ Docker support for development & deployment

---

## 🧰 Tech Stack

| Component        | Technology              |
| ---------------- | ----------------------- |
| Data Engine      | Apache Spark (PySpark)  |
| Web API          | FastAPI                 |
| Language         | Python 3.x              |
| Containerization | Docker & Docker Compose |
| Testing          | PyTest / Unittest       |

---

## 📁 Project Structure

```
DATA-PIPELINE-PYSPARK-FASTAPI/
├── app/                       # FastAPI application
├── pipeline/                  # PySpark data pipeline logic
├── tests/                     # Automated tests
├── Dockerfile                 # Docker image build instructions
├── docker-compose.yml         # Docker Compose setup
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## 🛠️ Installation & Setup

### 🐳 Using Docker (Recommended)

1. Clone the repository

```bash
git clone https://github.com/divithraju/DATA-PIPELINE-PYSPARK-FASTAPI-.git
cd DATA-PIPELINE-PYSPARK-FASTAPI-
```

2. Start Docker containers

```bash
docker-compose up --build
```

3. Open your browser

* FastAPI API: `http://localhost:8000/docs`
  (Swagger UI for testing endpoints)

---

## 🧩 Running Without Docker

### Backend (FastAPI)

```bash
cd app
python3 -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Visit `http://localhost:8000/docs`

### Pipeline (PySpark)

```bash
cd pipeline
spark-submit pipeline_script.py
```

*(Replace pipeline_script.py with your main PySpark script)*

---

## 📌 API Endpoints (Sample)

| Method | Endpoint        | Description              |
| ------ | --------------- | ------------------------ |
| GET    | `/health`       | Check API status         |
| POST   | `/run_pipeline` | Trigger PySpark pipeline |
| GET    | `/data/results` | Fetch processed data     |

---

## 🧪 Tests

```bash
pytest
```

---

## 📄 Why This Project Matters

✔︎ Real-world data engineering workflow
✔︎ FastAPI + PySpark integration
✔︎ Dockerized for quick deployment

---

## 👨‍💻 Author

**Divith Raju**
Backend & Data Engineering Enthusiast 🇮🇳
GitHub: [https://github.com/divithraju](https://github.com/divithraju)

---

## 📝 License

Open-source under the **MIT License**.

---

⭐ *If you find this project useful, please give it a ⭐ on GitHub!*
