import streamlit as slt
import pickle
import numpy as np
from mlr_model import MLR   

PATH = 'model.pkl'

# Load the full model object
@slt.cache_resource
def load_model():
    with open(PATH, "rb") as f:
        model = pickle.load(f)
    return model


model = load_model()

slt.title("Sales Prediction")

tv = slt.slider("TV Advertising Expenses", 0, 296)
radio = slt.slider("Radio Advertising Expenses", 0, 50)
newspaper = slt.slider("Newspaper Advertising Expenses", 0, 115)

if slt.button("Predict Sales"):
    features = np.array([[tv, radio, newspaper]])
    prediction = model.predict(features)
    slt.success(f"Predicted Sales: {prediction[0]:.2f}")
