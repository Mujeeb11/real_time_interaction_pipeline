from kafka import KafkaConsumer
from pymongo import MongoClient, UpdateOne
from config.settings import KAFKA_TOPIC, KAFKA_BOOTSTRAP_SERVERS, MONGO_URI
import json

client = MongoClient(MONGO_URI)
db = client["user_metrics"]
collection = db["aggregated"]

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

for message in consumer:
    event = message.value
    user_id = event["user_id"]
    item_id = event["item_id"]

    collection.update_one(
        {"user_id": user_id},
        {"$inc": {"interaction_count": 1}},
        upsert=True
    )

    collection.update_one(
        {"item_id": item_id},
        {"$inc": {"interaction_count": 1}},
        upsert=True
    )