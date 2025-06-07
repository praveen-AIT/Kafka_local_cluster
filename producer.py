# producer.py
from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

products = ['Shoes', 'Book', 'Laptop', 'Watch', 'Phone']
user_ids = [101, 102, 103, 104, 105]

def generate_order():
    return {
        'user_id': random.choice(user_ids),
        'product': random.choice(products),
        'amount': round(random.uniform(20.0, 500.0), 2),
        'timestamp': time.time()
    }

topic = 'orders'

print("Producing messages to topic:", topic)
while True:
    order = generate_order()
    producer.send(topic, value=order)
    print("Sent:", order)
    time.sleep(2)
