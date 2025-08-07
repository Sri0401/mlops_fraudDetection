import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.ensemble import IsolationForest
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generate dummy training data
X, _ = make_classification(n_samples=100, n_features=4, random_state=42)
x_train, x_test = train_test_split(X, test_size=0.2, random_state=42)

# Define and train model
model = IsolationForest(random_state=42)
model.fit(x_train)

# Log model to MLflow
mlflow.sklearn.log_model(model, "fraud_model")

# Prediction function
def predict_transaction(txn):
    features = np.array([[txn['amount'], txn['account_id'], txn['transaction_id'], txn['timestamp']]])
    pred = model.predict(features)
    return 'fraud' if pred[0] == -1 else 'legit'

# Main test case
if __name__ == "__main__":
    test_txn = {
        'amount': 5000.0,
        'account_id': 1234,
        'transaction_id': 567890,
        'timestamp': 1722595200.0
    }
    result = predict_transaction(test_txn)
    print(f"Test transaction prediction: {result}")
