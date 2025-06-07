from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

statuses = ['SHIPPED', 'DELIVERED', 'IN_TRANSIT']

while True:
    shipment = {
        'order_id': random.randint(1000, 9999),
        'status': random.choice(statuses),
        'tracking_id': random.randint(50000, 99999),
        'timestamp': time.time()
    }
    producer.send('shipments', value=shipment)
    print("🚚 Shipment sent:", shipment)
    time.sleep(4)
