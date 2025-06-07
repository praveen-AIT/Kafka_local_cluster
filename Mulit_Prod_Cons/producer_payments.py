from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

statuses = ['SUCCESS', 'FAILED', 'PENDING']

while True:
    payment = {
        'order_id': random.randint(1000, 9999),
        'status': random.choice(statuses),
        'amount': round(random.uniform(10, 500), 2),
        'timestamp': time.time()
    }
    producer.send('payments', value=payment)
    print("💰 Payment sent:", payment)
    time.sleep(3)
