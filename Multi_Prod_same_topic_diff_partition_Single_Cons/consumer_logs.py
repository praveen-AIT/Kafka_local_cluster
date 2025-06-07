from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'logs',
    bootstrap_servers='localhost:9092',
    group_id='logging-group',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    key_deserializer=lambda k: k.decode('utf-8') if k else None
)

print("📥 Log consumer started...")
for msg in consumer:
    if msg.partition == 1:
        print("Message from Partition 1")
    elif msg.partition == 2:
        print("Message from Partition 2")
    
    print(f"📬 [Partition {msg.partition}] {msg.key}: {msg.value}")
