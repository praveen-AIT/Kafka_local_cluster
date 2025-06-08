Producer (raw text via REST/FastAPI) ───▶ Kafka Topic ───▶ Consumer:
                                                        └─▶ Preprocess
                                                        └─▶ Embed
                                                        └─▶ Classify
                                                        └─▶ Forward/Store

**Directory Structure (Simplified for Focus):**

text_classification_kafka/
├── docker-compose.yml
├── proto/
│   └── message.proto
├── generated/
│   └── message_pb2.py
├── producer/
│   └── producer.py
├── consumer/
│   └── consumer.py
├── processing/
│   ├── text_preprocessor.py
│   └── classifier.py

