# ML Model Serving API with FastAPI

## Project Overview

This project demonstrates how to serve a machine learning model using FastAPI.

A Random Forest classifier is trained on the Iris dataset using Scikit-Learn and exposed through a REST API. Users can send feature values to the API and receive model predictions in real time.

The project demonstrates core concepts used in MLOps and OpenShift AI environments, including:

- Machine Learning Model Training
- Model Serialization with Joblib
- REST API Development with FastAPI
- Request Validation using Pydantic
- Real-Time Model Inference
- Interactive API Documentation with Swagger UI
- Containerization Readiness with Docker

---

## Technologies Used

- Python
- FastAPI
- Scikit-Learn
- Joblib
- Pydantic
- Uvicorn

---

## Project Structure

```text
model-api/
│
├── train.py
├── app.py
├── requirements.txt
├── model.pkl
└── README.md
```

---

## Model Training

The machine learning model is trained using the Iris dataset.

Algorithm used:

- Random Forest Classifier

The trained model is saved as:

```text
model.pkl
```

Run training:

```bash
python train.py
```

Expected output:

```text
Model saved successfully
```

---

## Running the API

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

## Root Endpoint

Navigate to:

```text
http://127.0.0.1:8000
```

Response:

```json
{
  "message": "ML Model Serving API"
}
```

---

## Interactive API Documentation

FastAPI automatically generates Swagger UI documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Testing the Prediction Endpoint

### Step 1

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

### Step 2

Expand:

```text
POST /predict
```

### Step 3

Click:

```text
Try it out
```

### Step 4

Enter the following sample request:

```json
{
  "feature1": 5.1,
  "feature2": 3.5,
  "feature3": 1.4,
  "feature4": 0.2
}
```

### Step 5

Click:

```text
Execute
```

### Response

```json
{
  "prediction": 0
}
```

This confirms that the trained machine learning model is successfully loaded and serving predictions through the API.

---

## Screenshots

### Swagger UI Prediction Test

![Prediction Endpoint](screenshots/predict-endpoint.png)


This screenshot demonstrates:

- FastAPI Swagger documentation
- Request payload submission
- Successful API execution
- Returned machine learning prediction

---

## Key Learning Outcomes

This project demonstrates:

- Machine Learning Model Serving
- API Development using FastAPI
- REST Endpoint Design
- Request Validation using Pydantic
- Model Serialization and Loading
- Real-Time Inference
- MLOps Fundamentals