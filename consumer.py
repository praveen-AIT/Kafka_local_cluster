# consumer.py
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='order-processor-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consumer started. Listening for orders...")

for message in consumer:
    order = message.value
    print(f"Received order from user {order['user_id']} for {order['product']} worth ${order['amount']}")
