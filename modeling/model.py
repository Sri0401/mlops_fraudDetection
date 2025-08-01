import numpy as np
from sklearn.ensemble import IsolationForest
import mlflow

# Dummy model for illustration
model = IsolationForest()
mlflow.set_tracking_uri('sqlite:///mlruns.db')

# Train with random data for demo
X_train = np.random.rand(100, 4)
model.fit(X_train)
mlflow.sklearn.log_model(model, "fraud_model")

def predict_transaction(txn):
    features = np.array([[txn['amount'], txn['account_id'], txn['transaction_id'], txn['timestamp']]])
    pred = model.predict(features)
    return 'fraud' if pred[0] == -1 else 'legit'

if __name__ == "__main__":
    test_txn = {
        'amount': 5000.0,
        'account_id': 1234,
        'transaction_id': 567890,
        'timestamp': 1722595200.0
    }
    result = predict_transaction(test_txn)
    print(f"Test transaction prediction: {result}")
