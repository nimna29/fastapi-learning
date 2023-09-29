from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle
import pandas as pd

app = FastAPI(
    title="FastAPI with Simple ML Model",
    description="ML Model Integration with FastAPI",
    version="0.0.0"
)

# Import the ml model and load
pickle_in = open("app/ml_model.pkl", "rb")
classifier=pickle.load(pickle_in)

# Create object with feature names 
# ['variance', 'skewness', 'curtosis', 'entropy']
class BankNotes(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float


# Root rount
@app.get("/", tags=['Root'])
def home():
    return {'message': 'Welcome to the Bank Note Authentication ML App'}


# Expose the prediction functionality:
# Make a presdiction from the pass JSON date and return the predicted Bank Note with Confidence value
@app.post("/predict", tags=['Prediction'])
def predict_bank_note(data:BankNotes):
    data = data.model_dump()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction="Fake note"
    else:
        prediction="Its a Bank note"
    return {
        'prediction': prediction
    }
