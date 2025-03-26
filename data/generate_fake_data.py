import os
from faker import Faker
import random
import pandas as pd
from datetime import datetime

# 👇 Set full data path
data_folder = "C:\\Users\\user\\OneDrive\\Desktop\\FraudDetectionProject\\data"
os.makedirs(data_folder, exist_ok=True)

fake = Faker()
names = ['Serena', 'Blair', 'Chuck', 'Nate', 'Dan']
locations = ['New York', 'Paris', 'London', 'Dubai', 'Tokyo']

def generate_transaction(transaction_id):
    name = random.choice(names)
    amount = round(random.uniform(5.0, 5000.0), 2)
    location = random.choice(locations)
    timestamp = datetime.now().isoformat()

    return {
        "transaction_id": transaction_id,
        "name": name,
        "amount": amount,
        "location": location,
        "timestamp": timestamp
    }

transactions = [generate_transaction(i) for i in range(1, 101)]
df = pd.DataFrame(transactions)

# ✅ Save the file in the proper folder
file_path = os.path.join(data_folder, "fake_transactions.csv")
df.to_csv(file_path, index=False)

print(f"✅ Drama saved: {file_path}")
