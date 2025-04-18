# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
import joblib


# Load the model
xgb_best_model = joblib.load('xgb_best_model.pkl')



# Streamlit app title
st.title("HDB Resale Price Prediction")

# Input for date
input_date = st.date_input("Select the date", pd.to_datetime("2023-01-01"))

# Convert the date to the required format
input_date_numeric = pd.to_datetime(input_date).timestamp() # Convert to timestamp

# Input for other features (you can add more inputs as needed)
# For example, let's assume you have features like 'location', 'size', etc.
# location = st.selectbox("Select Location", options=["Location1", "Location2", "Location3"])
# size = st.number_input("Enter Size (in sqft)", min_value=0)

# Prepare the input data for prediction
input_data = pd.DataFrame({
    'date': [input_date_numeric],
    #'location': [location],
    #'size': [size],
    # Add other features as necessary
})

# Make prediction
if st.button("Predict"):
    prediction = xgb_best_model.predict(input_data)
    st.write(f"Predicted Resale Price: ${prediction[0]:,.2f}")