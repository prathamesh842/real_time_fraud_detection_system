from kafka import KafkaProducer
import json
import pandas as pd
import time
import os

# Get Kafka bootstrap servers from environment variable
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

# Read the dataset
df = pd.read_csv('/app/DATASET/creditcard.csv')

important_feature = ['V17', 'V14', 'V12', 'V10', 'V16', 'V3', 'V7', 'V11', 'V4', 'Amount', 'Class']
df = df[important_feature]
#print(df.head())

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)
for i in range(100):
    transaction_data = df.sample(1).iloc[0]
    transaction = {
        'transaction_id': i + 1,  # Unique ID for the transaction
        'V17': transaction_data['V17'],
        'V14': transaction_data['V14'],
        'V12': transaction_data['V12'],
        'V10': transaction_data['V10'],
        'V16': transaction_data['V16'],
        'V3': transaction_data['V3'],
        'V7': transaction_data['V7'],
        'V11': transaction_data['V11'],
        'V4': transaction_data['V4'],
        'Amount': transaction_data['Amount'],
        'Class': transaction_data['Class'],  # Fraud (1) or Legitimate (0)
        'time': int(time.time()),  # Current timestamp
    }
    producer.send("transactions", transaction)
    print(f"Sent transaction {i + 1}: {transaction}")
    time.sleep(1)
producer.flush()    
