from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=lambda k: k.encode('utf-8'),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    log = {
        'app': 'app1',
        'level': random.choice(['INFO', 'WARN', 'ERROR']),
        'message': f"App1 log {random.randint(1, 100)}",
        'timestamp': time.time()
    }
    key = log['app']  # Partitioning key
    producer.send('logs', key=key, value=log)
    print("🟢 App1 sent log:", log)
    time.sleep(2)
