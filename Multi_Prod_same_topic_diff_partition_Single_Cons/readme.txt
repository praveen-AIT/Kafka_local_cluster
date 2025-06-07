🧠 What’s a Partition Key?

When producing a message, if you provide a key, Kafka uses it to determine which partition the message should go to (using a hash function).

This helps ensure that all messages with the same key go to the same partition, which preserves order per key.
🎯 Updated Use Case

Let’s say:

    Each log message has a service_name as key

    We want logs from the same service to always go to the same partition

🧾 Topic Setup with Multiple Partitions

First, make sure your topic is created like this (with 3 partitions):

docker exec -it <kafka-container-name> \
  kafka-topics --create --topic logs --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1

Or if it already exists with 1 partition, delete and recreate it with 3.


Extra: How Kafka Chooses Partitions

Kafka chooses the partition like this:

partition = hash(key) % num_partitions

So app1 will always go to the same partition unless the number of partitions changes.
