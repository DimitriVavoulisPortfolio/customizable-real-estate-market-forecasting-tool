import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
import warnings
import datetime
import joblib

warnings.filterwarnings("ignore")

STATE_NAME = "California"

def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def load_and_preprocess_data():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        log_message("Loading dataset...")
        file_path = os.path.join(parent_dir, 'customizable-real-estate-market-forecasting-tool/ZHVI.csv')
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"ZHVI.csv file not found at {file_path}")
        
        df = pd.read_csv(file_path, index_col=0, parse_dates=True)
        
        log_message("Preprocessing data...")
        state_data = df[STATE_NAME]
        state_data = state_data.dropna()
        state_data = state_data.sort_index()
        
        return state_data
    except Exception as e:
        log_message(f"An error occurred: {e}")
        return None

def plot_and_save(plt, filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    plt.savefig(os.path.join(script_dir, filename))
    plt.close()

def load_models():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    models_dir = os.path.join(parent_dir, 'customizable-real-estate-market-forecasting-tool/models/California')
    
    auto_arima_path = os.path.join(models_dir, 'California_auto_arima_model.joblib')
    sarima_path = os.path.join(models_dir, 'California_sarima_model.joblib')
    
    if not os.path.exists(auto_arima_path) or not os.path.exists(sarima_path):
        raise FileNotFoundError("One or both model files not found in the 'models' folder.")
    
    auto_arima_model = joblib.load(auto_arima_path)
    sarima_model = joblib.load(sarima_path)
    
    return auto_arima_model, sarima_model

def main():
    df = load_and_preprocess_data()
    if df is None:
        return

    # Get user input for forecast months
    while True:
        try:
            forecast_months = int(input("Enter the number of months to forecast: "))
            if forecast_months > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    log_message(f"Forecasting for {forecast_months} months")

    # Load pre-trained models
    try:
        auto_arima_model, sarima_model = load_models()
        log_message("Pre-trained models loaded successfully")
    except FileNotFoundError as e:
        log_message(f"Error: {e}")
        return

    # Use the loaded SARIMA model for forecasting
    log_message("Generating forecast...")
    forecast = sarima_model.get_forecast(steps=forecast_months)
    forecast_mean = forecast.predicted_mean
    forecast_ci = forecast.conf_int()

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(forecast_mean.index, forecast_mean, color='red', label='Forecast')
    plt.fill_between(forecast_ci.index, forecast_ci.iloc[:, 0], forecast_ci.iloc[:, 1], color='pink', alpha=0.3)
    plt.title(f'{STATE_NAME} ZHVI - {forecast_months} Month Forecast')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('ZHVI')
    plot_and_save(plt, f'zhvi_forecast_{forecast_months}_months.png')

    # Save forecast to CSV
    forecast_df = pd.DataFrame({
        'Date': forecast_mean.index,
        'Forecasted_ZHVI': forecast_mean.values
    })
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_filename = f'{STATE_NAME}_zhvi_forecast_{forecast_months}_months.csv'
    forecast_df.to_csv(os.path.join(script_dir, csv_filename), index=False)

    log_message(f"Forecast saved to {csv_filename}")
    log_message("Forecast summary:")
    log_message(str(forecast_mean))

if __name__ == "__main__":
    main()
