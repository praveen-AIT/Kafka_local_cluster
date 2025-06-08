from kafka import KafkaConsumer
from generated import text_pb2
from processing.text_preprocessor import preprocess_text
from processing.classifier import classify_text
import os
import sys
sys.path.append(os.path.abspath(".."))

consumer = KafkaConsumer(
    'text-topic',
    bootstrap_servers='localhost:9092',
    group_id='text-group',
    value_deserializer=lambda m: text_pb2.TextMessage.FromString(m)
)

print("[Consumer] Listening for messages...")
for msg in consumer:
    raw_text = msg.value.text
    print(f"[Consumer] Received: {raw_text}")

    preprocessed = preprocess_text(raw_text)
    prediction = classify_text(preprocessed)

    print(f"[Processed] => Cleaned: '{preprocessed}' | Classified as: {prediction}")
