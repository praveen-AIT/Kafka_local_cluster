from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=lambda k: k.encode('utf-8'),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    log = {
        'app': 'app2',
        'level': random.choice(['INFO', 'WARN', 'ERROR']),
        'message': f"App2 log {random.randint(1, 100)}",
        'timestamp': time.time()
    }
    key = log['app']
    producer.send('logs', key=key, value=log)
    print("🔵 App2 sent log:", log)
    time.sleep(3)
