from kafka import KafkaConsumer
import json
import requests
import os

# File to store fraudulent transaction IDs
FRAUD_LOG_FILE = "fraudulent_transactions.txt"

# Get Kafka bootstrap servers from environment variable
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

# Create a Kafka consumer
consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Process transactions in real-timeyyyyy
for message in consumer:
    transaction = message.value
    print(f"Received transaction: {transaction}")

    # Call the fraud detection API
    response = requests.post('http://localhost:5000/predict', json={'features': [
        transaction['V17'],
        transaction['V14'],
        transaction['V12'],
        transaction['V10'],
        transaction['V16'],
        transaction['V3'],
        transaction['V7'],
        transaction['V11'],
        transaction['V4'],
        transaction['Amount'],
    ]})
    result = response.json()

    # Check if the transaction is fraudulent
    if result['prediction'] == 1:
        print(f"Fraud detected! Transaction ID: {transaction['transaction_id']}, Probability: {result['fraud_probability']}")

        # Log the fraudulent transaction ID to a file
        with open(FRAUD_LOG_FILE, "a") as f:
            f.write(f"{transaction['transaction_id']}\n")
    else:
        print(f"Transaction ID: {transaction['transaction_id']} is legitimate.")
        