import pandas as pd
import streamlit as st
import numpy as np
from xgboost import XGBRegressor
import joblib

# Streamlit app title
st.title("HDB Resale Price Prediction")

# === Step 1: Load expected features used during model training ===
expected_features = [
    'storey_range', 'floor_area_sqm', 'flat_type', 'date', 
    'gdp in chained (2015) dollars', 'assets', 'liabilities',
    'total unemployment rate, (sa)', 'mas core inflation measure', 'm_from2017',
    'lease_months_left',
    'town_jurong west', 'town_sengkang', 'town_woodlands', 'town_punggol', 'town_tampines',
    'town_yishun', 'town_bedok', 'town_hougang', 'town_ang mo kio', 'town_bukit merah',
    'town_choa chu kang', 'town_toa payoh', 'town_bukit batok', 'town_bukit panjang',
    'town_kallang/whampoa', 'town_pasir ris', 'town_geylang', 'town_queenstown', 'town_sembawang',
    'town_jurong east', 'town_bishan', 'town_clementi', 'town_serangoon', 'town_central area',
    'town_marine parade', 'town_bukit timah',
    'flat_model_Model A', 'flat_model_Improved', 'flat_model_New Generation',
    'flat_model_Premium Apartment', 'flat_model_Simplified', 'flat_model_Apartment',
    'flat_model_Maisonette', 'flat_model_Standard', 'flat_model_DBSS', 'flat_model_Model A2',
    'flat_model_Model A-Maisonette', 'flat_model_Adjoined flat', 'flat_model_Type S1',
    'flat_model_2-room', 'flat_model_Type S2', 'flat_model_Premium Apartment Loft',
    'flat_model_Terrace', 'flat_model_Multi Generation', 'flat_model_3Gen',
    'flat_model_Improved-Maisonette', 'flat_model_Premium Maisonette'
]

# === Step 2: Load economic data for macro indicators ===
econ_data = pd.read_csv('indicators.csv', parse_dates=['Date'])
econ_data.set_index('Date', inplace=True)

# === Step 3: User Input ===
user_date = pd.to_datetime("2023-08-01")

# === Step 4: Fetch macro data ===
def fetch_macro_indicators(date, econ_df):
    closest_date = econ_df.index[econ_df.index <= date].max()
    if pd.isna(closest_date):
        raise ValueError("No economic data available before this date.")
    return econ_df.loc[closest_date]

macro = fetch_macro_indicators(user_date, econ_data)

# === Step 5: Default values for static fields ===
default_values = {
    'storey_range': '04 TO 06',
    'floor_area_sqm': 90,
    'flat_type': '4 ROOM',
    'date': user_date,
    'm_from2017': 1 if user_date >= pd.to_datetime("2017-01-01") else 0,
    'lease_months_left': 900,
    'assets': macro['    Assets'],
    'liabilities': macro['    Liabilities'],
    'gdp in chained (2015) dollars': macro['GDP In Chained (2015) Dollars'],
    'total unemployment rate, (sa)': macro['Total Unemployment Rate, (SA)'],
    'mas core inflation measure': macro['MAS Core Inflation Measure']
}

# Extract dropdown options
town_options = sorted([col.replace('town_', '') for col in expected_features if col.startswith('town_')])
flat_model_options = sorted([col.replace('flat_model_', '') for col in expected_features if col.startswith('flat_model_')])

# Streamlit Inputs
selected_town = st.selectbox("Select Town", town_options)
selected_model = st.selectbox("Select Flat Model", flat_model_options)

# Generate one-hot encodings
one_hot_features = {key: 0 for key in expected_features if key.startswith('town_') or key.startswith('flat_model_')}
one_hot_features[f'town_{selected_town}'] = 1
one_hot_features[f'flat_model_{selected_model}'] = 1


# === Step 7: Combine all inputs ===
full_input_dict = {**default_values, **one_hot_features}

# === Step 8: Ensure all expected features are present ===
for col in expected_features:
    if col not in full_input_dict:
        full_input_dict[col] = 0  # default to 0 if missing

# === Step 9: Create input DataFrame ===
input_data = pd.DataFrame([full_input_dict])[expected_features]

input_data['storey_range'] = input_data['storey_range'].astype('category').cat.codes
input_data['flat_type'] = input_data['flat_type'].astype('category').cat.codes
input_data['date'] = input_data['date'].dt.year  # or extract month, etc., depending on model training
input_data['lease_months_left'] = input_data['lease_months_left'].astype('int')
input_data['floor_area_sqm'] = input_data['floor_area_sqm'].astype('int')
input_data['m_from2017'] = input_data['m_from2017'].astype('int')

# === Step 10: Streamlit app ===

# Load the trained model (assuming you have saved it after training)
# For example, you can use joblib or pickle to load the model
from joblib import load
# Load the model
xgb_best_model = joblib.load('xgb_best_model.pkl')


# Input for date
input_date = st.date_input("Select the date", pd.to_datetime("2023-01-01"))

# Convert the date to the required format
input_date_numeric = pd.to_datetime(input_date).timestamp() # Convert to timestamp

# Input for other features (you can add more inputs as needed)
# For example, let's assume you have features like 'location', 'size', etc.
# location = st.selectbox("Select Location", options=["Location1", "Location2", "Location3"])
# size = st.number_input("Enter Size (in sqft)", min_value=0)

# Make prediction
if st.button("Predict"):
    prediction = xgb_best_model.predict(input_data)
    st.write(f"Predicted Resale Price: ${prediction[0]:,.2f}")