from fastapi import FastAPI, Request
from pydantic import BaseModel
from modeling.model import predict_transaction
from explainability.explain import explain_prediction
from hitl_feedback.feedback import submit_feedback

app = FastAPI()

class Transaction(BaseModel):
    transaction_id: int
    account_id: int
    amount: float
    type: str
    timestamp: float

@app.post('/predict')
async def predict(txn: Transaction):
    prediction = predict_transaction(txn.dict())
    explanation = explain_prediction(txn.dict())
    return {"prediction": prediction, "explanation": explanation}

@app.post('/feedback')
async def feedback(request: Request):
    data = await request.json()
    submit_feedback(data)
    return {"status": "received"}
