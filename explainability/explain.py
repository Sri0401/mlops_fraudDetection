def explain_prediction(txn):
    # Dummy explanation for illustration
    return {
        "reason": "Transaction amount unusually high compared to account history.",
        "feature_importance": {"amount": 0.9, "account_id": 0.05, "transaction_id": 0.03, "timestamp": 0.02}
    }
