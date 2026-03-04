import json
import psycopg2
from kafka import KafkaConsumer

TOPIC = "transactions"
KAFKA_BOOTSTRAP = "localhost:9092"

POSTGRES_HOST = "localhost"
POSTGRES_DB = "fraud_db"
POSTGRES_USER = "fraud"
POSTGRES_PASSWORD = "fraud"
POSTGRES_PORT = 5432

print("Consumer starting...")

# Connect to Postgres
conn = psycopg2.connect(
    host=POSTGRES_HOST,
    database=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    port=POSTGRES_PORT
)
cur = conn.cursor()
print("[OK] Postgres connected!")

# Ensure table exists (so it never fails after restart)
cur.execute("""
CREATE TABLE IF NOT EXISTS fraud_predictions (
    id SERIAL PRIMARY KEY,
    event_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transaction_id INT,
    amount FLOAT,
    fraud_score FLOAT,
    fraud_label INT
);
""")
conn.commit()
print("[OK] fraud_predictions table ready!")

# Connect to Kafka
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)
print("[OK] Kafka connected! Waiting for messages...")

count = 0

for msg in consumer:
    data = msg.value
    count += 1

    tx_id = int(data.get("transaction_id", 0))
    amount = float(data.get("Amount", 0.0))

    # Demo fraud scoring (creates fraud for higher amounts)
    fraud_score = min(1.0, amount / 200.0)   # bigger amount => bigger score
    fraud_label = 1 if fraud_score > 0.7 else 0

    cur.execute(
        "INSERT INTO fraud_predictions (transaction_id, amount, fraud_score, fraud_label) VALUES (%s, %s, %s, %s)",
        (tx_id, amount, fraud_score, fraud_label)
    )
    conn.commit()

    print(f"Inserted {count}: tx={tx_id} amount={amount} score={fraud_score:.3f} label={fraud_label}")