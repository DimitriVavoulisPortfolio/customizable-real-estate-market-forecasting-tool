import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from pmdarima import auto_arima
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error, r2_score
import warnings
import datetime
import joblib

warnings.filterwarnings("ignore")

STATE_NAME = "Texas"

def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def load_and_preprocess_data():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        log_message("Loading dataset...")
        file_path = os.path.join(script_dir, 'ZHVI.csv')
        
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

def evaluate_model(y_true, y_pred):
    mape = mean_absolute_percentage_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    return mape, rmse, r2

def save_model(model, filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    joblib.dump(model, os.path.join(script_dir, filename))
    log_message(f"Model saved as {filename}")

def main():
    df = load_and_preprocess_data()
    if df is None:
        return

    log_message("Running Auto ARIMA...")
    auto_model = auto_arima(df, seasonal=True, m=12, suppress_warnings=True, stepwise=True)
    log_message(str(auto_model.summary()))
    
    # Save auto_arima model
    save_model(auto_model, f'{STATE_NAME}_auto_arima_model.joblib')
    
    order = auto_model.order
    seasonal_order = auto_model.seasonal_order
    
    log_message("Fitting SARIMA model...")
    model = SARIMAX(df, order=order, seasonal_order=seasonal_order)
    results = model.fit()
    
    # Save SARIMA model
    save_model(results, f'{STATE_NAME}_sarima_model.joblib')
    
    log_message("Generating predictions...")
    # Generate in-sample predictions
    in_sample_pred = results.get_prediction(start=df.index[0], end=df.index[-1])
    in_sample_mean = in_sample_pred.predicted_mean

    # Generate out-of-sample forecast
    forecast_steps = 12  # 12 additional months
    forecast = results.get_forecast(steps=forecast_steps)
    forecast_mean = forecast.predicted_mean
    forecast_ci = forecast.conf_int()

    # Combine in-sample and out-of-sample predictions
    all_predictions = pd.concat([in_sample_mean, forecast_mean])

    # Evaluate model on 2024 data
    df_2024 = df[df.index >= '2024-01-01']
    pred_2024 = in_sample_mean[in_sample_mean.index >= '2024-01-01']
    mape, rmse, r2 = evaluate_model(df_2024, pred_2024)
    log_message(f"2024 Onwards MAPE: {mape:.4f}")
    log_message(f"2024 Onwards RMSE: {rmse:.2f}")
    log_message(f"2024 Onwards R-squared: {r2:.4f}")

    # Plotting (focus on 2024 onwards)
    plt.figure(figsize=(12, 6))
    plt.plot(df[df.index >= '2024-01-01'].index, df[df.index >= '2024-01-01'], label='Observed', color='blue')
    plt.plot(all_predictions[all_predictions.index >= '2024-01-01'].index, 
             all_predictions[all_predictions.index >= '2024-01-01'], 
             color='red', label='Predicted/Forecast')
    plt.fill_between(forecast_mean.index, forecast_ci.iloc[:, 0], forecast_ci.iloc[:, 1], color='pink', alpha=0.3)
    plt.title(f'{STATE_NAME} ZHVI - Observed, Predicted, and Forecast (2024 onwards)')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('ZHVI')
    plot_and_save(plt, f'{STATE_NAME}_zhvi_forecast_2024_onwards.png')
    
    log_message("Saving forecast to CSV...")
    forecast_df = pd.DataFrame({
        'Date': forecast_mean.index,
        'Forecasted_ZHVI': forecast_mean.values
    })
    script_dir = os.path.dirname(os.path.abspath(__file__))
    forecast_df.to_csv(os.path.join(script_dir, f'{STATE_NAME}_zhvi_forecast_2024_onwards.csv'), index=False)

    log_message("Forecast for the next 12 months after available data:")
    log_message(str(forecast_mean))

if __name__ == "__main__":
    main()
