# Real-Time Fraud Detection Pipeline

## Project Overview
This project demonstrates a real-time fraud detection data pipeline that processes streaming transaction data, applies fraud scoring logic, stores predictions in a database, and visualizes fraud metrics through a live monitoring dashboard.

The system simulates financial transactions and processes them through a streaming architecture to detect potentially fraudulent activity in near real-time.

## Architecture
CSV Dataset  
↓  
Kafka Producer (Simulated Transactions)  
↓  
Kafka Topic (Transaction Stream)  
↓  
Consumer Service (Fraud Scoring Logic)  
↓  
PostgreSQL Database  
↓  
Streamlit Dashboard (Real-Time Monitoring)

## Tech Stack
Python – Data processing and pipeline logic  
Apache Kafka – Real-time event streaming  
PostgreSQL – Storage for fraud prediction results  
Docker – Containerized services (Kafka, Zookeeper, PostgreSQL)  
Streamlit – Real-time data visualization dashboard  
Pandas – Data processing and analysis

## Project Workflow
1. A producer service reads transaction data and streams events into a Kafka topic.  
2. Kafka acts as a message broker to handle real-time transaction streams.  
3. A consumer service processes each transaction and applies fraud scoring logic.  
4. Fraud predictions are inserted into a PostgreSQL database.  
5. A Streamlit dashboard visualizes transaction metrics and fraud detection results.

## How to Run

### Prerequisites
- Python 3.10+
- Docker Desktop installed and running
- Git installed

### Step 1: Clone the Repository
git clone https://github.com/yourusername/real-time-fraud-pipeline.git  
cd real-time-fraud-pipeline

### Step 2: Start Infrastructure Services
docker compose up -d

Verify services are running:
docker ps

### Step 3: Create Kafka Topic
docker exec -it real-time-fraud-pipeline-kafka-1 bash

kafka-topics --create \
--topic transactions \
--bootstrap-server localhost:9092 \
--partitions 1 \
--replication-factor 1

exit

### Step 4: Run Fraud Scoring Consumer
python consumer/consumer_score.py

This service:
- Reads transactions from Kafka
- Applies fraud scoring logic
- Stores results in PostgreSQL

### Step 5: Run Transaction Producer
python producer/producer.py

This simulates transaction events and sends them to Kafka.

### Step 6: Launch Monitoring Dashboard
streamlit run dashboard.py

Open the dashboard in your browser:
http://localhost:8501

## Output
The pipeline processes streaming transaction data and generates fraud predictions in real time.

Each transaction is stored in the **fraud_predictions** PostgreSQL table with the following attributes:
- transaction_id
- amount
- fraud_score
- fraud_label
- event_time

The dashboard displays:
- Total transactions processed
- Number of fraud transactions detected
- Fraud rate percentage
- Fraud score distribution
- Recent transaction monitoring table

## Dashboard Preview

### Real-Time Monitoring Dashboard
![Dashboard](ss/dashboard_overview.png)

### Fraud Score Distribution
![Fraud Distribution](ss/fraud_score_distribution.png)

### Transactions Over Time
![Transactions Over Time](ss/transcation_over_time.png)

### Latest Transactions Table
![Latest Transactions](ss/latest_transactions.png)

