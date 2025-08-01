# Real-time MLOps Platform for Adaptive Financial Fraud Detection

## Objective
Build a robust, scalable, and real-time fraud detection platform that simulates and ingests financial transactions, applies anomaly detection models, and serves predictions via a deployable, monitored API — all following best practices in MLOps, Data Engineering, and Responsible AI.

## Features
- Real-time ingestion (Kafka)
- Streaming + batch processing
- Adaptive ML models
- Explainable outputs (XAI)
- Human-in-the-loop feedback (HITL)
- Modular pipelines
- API serving (FastAPI)
- Monitoring
- CI/CD and containerization (K8s-ready)
- Versioning and testability

## Directory Structure
- `data_simulation/`: Simulate financial transactions
- `ingestion/`: Kafka-based ingestion
- `processing/`: Streaming and batch processing
- `modeling/`: ML models and training
- `explainability/`: Explainable AI modules
- `hitl_feedback/`: Human-in-the-loop feedback
- `api/`: FastAPI serving
- `monitoring/`: Monitoring and logging
- `cicd/`: CI/CD pipelines
- `containerization/`: Docker/Kubernetes configs

## Getting Started
1. Install dependencies
2. Run data simulation and ingestion
3. Train and deploy models
4. Serve predictions via API
5. Monitor and iterate with feedback

## Requirements
- Python 3.8+
- Kafka
- FastAPI
- MLflow
- Docker
- Kubernetes

## License
MIT
