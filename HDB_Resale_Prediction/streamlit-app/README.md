# Streamlit App

This project is a Streamlit application designed for data analysis and visualization using a dataset of macroeconomic indicators.

## Project Structure

```
streamlit-app
├── app.py                    # Main Streamlit application
├── indicators.csv        # Macroeconomic dataset used by the app
├── xgb_best_model.pkl        # Trained XGBoost regression model
├── requirements.txt          # Python packages required to run the app
└── README.md                 # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd HDB Resale Prediction
   ```

2. **Install the required packages**:
   It is recommended to create a virtual environment before installing the dependencies. You can use `venv` or `conda` for this purpose.

   Using pip:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```
   streamlit run app.py
   ```

4. **Access the app**:
   After running the command, a new tab will open in your default web browser displaying the Streamlit app.

## Dataset Information

The dataset `indicators.csv` contains various macroeconomic indicators such as:
GDP

Assets & Liabilities

MAS Core Inflation Measure

Unemployment Rate (SA)

These indicators are automatically integrated based on the resale date selected by the user.

## Features

- Predict resale price using an XGBoost regression model.

User inputs include:

Town

Flat Model

Floor Area (sqm)

Storey Range

Lease Months Left

Resale Date

Auto-fetches macroeconomic indicators corresponding to the selected date.

Encodes user input dynamically to match model expectations.

Displays predicted resale price clearly and accurately.

## Model

Trained using historical HDB resale data and aligned with macroeconomic conditions.

Uses one-hot encoding for categorical features like town and flat model.

Model is saved as xgb_best_model.pkl and loaded during runtime for predictions.

## Requirements

Make sure the following Python libraries are included in requirements.txt:

streamlit

pandas

numpy

xgboost

joblib
