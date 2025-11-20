# 🛠️ Python ETL Pipeline (CSV + API)
👩‍💻 Author

Dharani
Python & Data Engineering enthusiast building real-world style projects.

GitHub: DharaniCA

Repo: python-etl

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-pytest-brightgreen.svg)](https://docs.pytest.org/)
[![Docker](https://img.shields.io/badge/container-Docker-blue.svg)](https://www.docker.com/)
[![Status](https://img.shields.io/badge/status-active-success.svg)](#)
[![Made with ❤️](https://img.shields.io/badge/made_with-❤️-ff69b4.svg)](#)

A clean, extensible, and production-style ETL (Extract–Transform–Load) pipeline built with Python.  
This project is part of my journey as a Python Data Engineer and showcases real-world patterns:
config-driven execution, modular ETL steps, logging, tests, Docker, and scheduling.

---

## 📚 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Running the Pipeline](#-running-the-pipeline)
  - [Locally](#run-locally)
  - [With Docker](#run-with-docker)
- [Tests](#-tests)
- [Scheduling](#-scheduling-optional)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

---

## ✨ Features

- ✅ Extracts data from **CSV** or **REST API** (switchable via config)
- ✅ Clean separation of **extract / transform / load** steps
- ✅ Centralized **config.json** (paths, source type, logging)
- ✅ Structured logging to both **console** and **log file**
- ✅ **Pytest** unit tests for transformation logic
- ✅ **Dockerized** for consistent, portable execution
- ✅ Can be scheduled with **Windows Task Scheduler** (or cron/Airflow later)

---

## 🧰 Tech Stack

- **Language:** Python 3  
- **Libraries:** `requests`, `pytest`, `logging`  
- **Packaging / Runtime:** Docker  
- **OS:** Windows 11 (dev), Linux inside Docker  

---

## 🏗 Architecture

High-level ETL flow:

```text
        +------------------+
        |   CSV or API     |
        +---------+--------+
                  |
                  v
            [ Extract ]
                  |
                  v
            [ Transform ]
        (add age_plus_1, etc.)
                  |
                  v
             [ Load ]
                  |
                  v
        +----------------------+
        |  JSON output file    |
        +----------------------+

Later, this same pattern can be extended to:

Read from databases / cloud storage

Write to data warehouses (Snowflake, BigQuery, Redshift)

Be orchestrated by Airflow

Project Structure:
python-etl/
├── data/
│   ├── input.csv           # Sample input data
│   └── output.json         # ETL output (generated)
├── etl/
│   ├── __init__.py         # Marks this as a package
│   ├── extract.py          # CSV / API extraction logic
│   ├── transform.py        # Business logic (adds age_plus_1)
│   └── load.py             # Writes JSON to disk
├── logs/
│   └── etl.log             # ETL run logs (generated)
├── tests/
│   └── test_transform.py   # Unit test for transform step
├── config.json             # Config (source type, paths, logging)
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker image definition
├── main.py                 # Orchestrates the ETL pipeline
└── README.md
Configuration
The entire pipeline is controlled by config.json
{
  "source": "csv",
  "input_path": "data/input.csv",
  "api_url": "https://jsonplaceholder.typicode.com/users",
  "output_path": "data/output.json",
  "log_path": "logs/etl.log",
  "log_level": "INFO"
}
Set "source": "csv" to read from the CSV file.

Set "source": "api" to fetch data from the REST API.

🔎 Note: JSON doesn’t support comments. Make sure your real config.json does not contain // comments.
🚀 Running the Pipeline <a name="running-the-pipeline"></a>
▶ Run Locally <a name="run-locally"></a>

Install dependencies:

pip install -r requirements.txt


Run the ETL:

python main.py
# or
python3 main.py


This will:

Load config.json

Extract data (CSV or API)

Transform records (e.g. add age_plus_1)

Write output to data/output.json

Log details to logs/etl.log

This project uses pytest for unit testing.

Run all tests:

pytest


Example output:

tests/test_transform.py .    [100%]


You can extend tests to cover more ETL steps (API extraction, error handling, etc.).


Build the Docker image:

docker build -t python-etl:latest .


Run the container:

docker run --rm python-etl:latest


The container will:

Use the included config.json

Execute python main.py

Produce the same logs/output as your local run