from kafka import KafkaProducer
import time
import sys
import os
sys.path.append(os.path.abspath(".."))
from generated import text_pb2
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: v.SerializeToString()
)

if __name__ == "__main__":
    messages = [
        "Buy now! Limited offer.",
        "This is a normal user review.",
        "Win cash prize by clicking here!"
    ]

    for text in messages:
        msg = text_pb2.TextMessage()
        msg.text = text
        producer.send('text-topic', value=msg)
        print(f"[Producer] Sent: {text}")
        time.sleep(1)