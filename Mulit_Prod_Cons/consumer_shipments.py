from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'shipments',
    bootstrap_servers='localhost:9092',
    group_id='shipment-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("🚛 Waiting for shipments...")
for msg in consumer:
    print("🚛 Processing shipment:", msg.value)
