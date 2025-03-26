import csv
import json
import time
from kafka import KafkaProducer

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Path to your fake transaction file
csv_file = 'data/fake_transactions.csv'
topic_name = 'transactions'

with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Convert strings to proper types if needed
        row['amount'] = float(row['amount'])

        # Send to Kafka topic
        producer.send(topic_name, value=row)
        print(f"📤 Sent transaction to Kafka: {row['transaction_id']} | {row['name']} | ${row['amount']}")

        # Add slight delay to simulate streaming
        time.sleep(0.5)

producer.flush()
producer.close()
