from fastapi import FastAPI
# from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

app = FastAPI(
    title="FastAPI With Simple ML Model",
    description="ML Model Integration with FastAPI",
    version="0.0.0"
)

# Import the ml model and load
pickle_in = open("app/ml_model.pkl", "rb")
classifier=pickle.load(pickle_in)

# Root rount
@app.get("/", tags=['Root'])
def home():
    return {'message': 'Welcome to the Bank Note Authentication ML App'}