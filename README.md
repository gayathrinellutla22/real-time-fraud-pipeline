# Real-Time Fraud Streaming Pipeline

## Project Overview
This project simulates a real-time fraud detection pipeline using Kafka and PostgreSQL.

Flow:
CSV → Kafka → Consumer (Scoring) → PostgreSQL

## Tech Stack
- Python
- Kafka
- PostgreSQL
- Docker

## How to Run
1. docker compose up -d
2. Create Kafka topic
3. Run consumer
4. Run producer
5. Check Postgres table

## Output
Fraud predictions are stored in fraud_predictions table.