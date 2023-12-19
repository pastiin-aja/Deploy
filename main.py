import os
import tensorflow as tf
import pickle
from pydantic import BaseModel
from fastapi import FastAPI

# Load the CountVectorizer from the joblib file
loaded_vectorizer = pickle.load(open('./vectorizer.pickle', 'rb'))

# Initialize Model
# If you already put your model in the same folder as this main.py
# You can load .h5 model or any model below this line
model = tf.keras.models.load_model('./model_fraud_v1.h5')

class InputData(BaseModel):
    st: str

def model_predict(text_vectorized):
    # Make predictions using the loaded model
    predictions = model.predict(text_vectorized)

    return predictions

app = FastAPI()

@app.get("/")
def index():
    return {"msg": "mainpage"}

@app.post("/predict_text")
def predictor(data: InputData):
    # Vectorize the input text
    text_vectorized = loaded_vectorizer.transform([data.st])

    result = model_predict(text_vectorized)
    return {"msg": result.tolist()}  # Convert predictions to a list

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8080)

## python -m uvicorn main:app --reload
