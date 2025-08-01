    # No changes needed as there are no indicators of AI agent or Copilot involvement.
import random
import time
from kafka import KafkaProducer
import json

TRANSACTION_TYPES = ['purchase', 'withdrawal', 'transfer']

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def generate_transaction():
    return {
        'transaction_id': random.randint(100000, 999999),
        'account_id': random.randint(1000, 9999),
        'amount': round(random.uniform(10, 10000), 2),
        'type': random.choice(TRANSACTION_TYPES),
        'timestamp': time.time()
    }

if __name__ == "__main__":
    while True:
        txn = generate_transaction()
        producer.send('transactions', txn)
        print(f"Sent: {txn}")
        time.sleep(0.5)
