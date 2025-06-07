from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

users = [101, 102, 103]
products = ['Laptop', 'Phone', 'Tablet']

while True:
    order = {
        'user_id': random.choice(users),
        'product': random.choice(products),
        'timestamp': time.time()
    }
    producer.send('orders', value=order)
    print("🛒 Order sent:", order)
    time.sleep(2)
