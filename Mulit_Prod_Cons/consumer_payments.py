from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'payments',
    bootstrap_servers='localhost:9092',
    group_id='payment-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("💳 Waiting for payments...")
for msg in consumer:
    print("💳 Processing payment:", msg.value)
