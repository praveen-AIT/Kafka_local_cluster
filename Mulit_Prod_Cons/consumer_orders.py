from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    group_id='order-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("📦 Waiting for orders...")
for msg in consumer:
    print("📦 Processing order:", msg.value)
