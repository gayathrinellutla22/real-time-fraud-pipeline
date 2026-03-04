import json
import time
import random
from kafka import KafkaProducer

TOPIC = "transactions"
KAFKA_BOOTSTRAP = "localhost:9092"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

print("Producer running... sending 1 transaction/second to Kafka")

tx_id = 1

while True:
    # Simulate amount (some big amounts will trigger fraud)
    amount = round(random.uniform(1, 300), 2)

    event = {
        "transaction_id": tx_id,
        "Amount": amount
    }

    producer.send(TOPIC, value=event)
    producer.flush()

    print(f"Sent tx={tx_id}, amount={amount}")
    tx_id += 1
    time.sleep(1)