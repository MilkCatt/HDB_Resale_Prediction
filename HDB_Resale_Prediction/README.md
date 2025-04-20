## Project Structure

```
streamlit-app
├── app.py                # Main entry point for the Streamlit application
├── data
│   └── data_macro.csv    # Dataset used in the application
├── requirements.txt      # Python packages required to run the app
└── README.md             # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd streamlit-app
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

The dataset `data_macro.csv` contains various macroeconomic indicators that are used for analysis and visualization within the app. Ensure that the data is properly formatted and cleaned before use.

## Features

- Interactive visualizations of macroeconomic data.
- User-friendly interface for data exploration.
- Ability to filter and analyze data based on user inputs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
