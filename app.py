# app.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load trained model
model = joblib.load("model.pkl")

app = FastAPI(
    title="Iris Prediction API",
    description="Machine Learning Model Serving API",
    version="1.0"
)

# Request schema
class IrisInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float


@app.get("/")
def home():
    return {
        "message": "ML Model Serving API"
    }


@app.post("/predict")
def predict(data: IrisInput):

    features = [[
        data.feature1,
        data.feature2,
        data.feature3,
        data.feature4
    ]]

    prediction = model.predict(features)

    return {
        "prediction": int(prediction[0])
    }