import json
import random
import time
from kafka import KafkaProducer
from datetime import datetime
from config.settings import KAFKA_TOPIC, KAFKA_BOOTSTRAP_SERVERS

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

interaction_types = ["click", "view", "purchase"]

def generate_event():
    return {
        "user_id": f"user_{random.randint(1, 100)}",
        "item_id": f"item_{random.randint(1, 50)}",
        "interaction_type": random.choice(interaction_types),
        "timestamp": datetime.utcnow().isoformat()
    }

def produce_events(rate_per_sec=10):
    while True:
        for _ in range(rate_per_sec):
            event = generate_event()
            producer.send(KAFKA_TOPIC, value=event)
        time.sleep(1)

if __name__ == "__main__":
    produce_events(rate_per_sec=20)