# Data Processing and Model Training Pipeline

This document provides a detailed overview of the data processing and model training pipeline for the Customizable Real Estate Market Forecasting Tool. The pipeline is designed to be consistent across all state models, ensuring a standardized approach while accommodating state-specific data.

## Data Processing

1. **Data Loading**: The Zillow Home Value Index (ZHVI) dataset is loaded from the `ZHVI.csv` file using the `load_and_preprocess_data()` function. The function reads the CSV file into a pandas DataFrame, with the index column set to the date and parsed as dates.

2. **State Selection**: The ZHVI data for the specific state is extracted from the DataFrame based on the `STATE_NAME` variable defined in the script. This allows for easy customization of the pipeline for different states.

3. **Data Cleaning**: Missing values in the state-specific ZHVI data are removed using the `dropna()` function to ensure data integrity.

4. **Data Sorting**: The state-specific data is sorted by the index (date) using the `sort_index()` function to maintain chronological order.

## Model Training

1. **SARIMA Model Selection**: A Seasonal AutoRegressive Integrated Moving Average (SARIMA) model is chosen for forecasting the ZHVI trends. The SARIMA model is capable of capturing both trend and seasonality in the data.

2. **Hyperparameter Tuning**: The optimal hyperparameters for the SARIMA model are determined using the `auto_arima` function from the `pmdarima` library. The function automatically selects the best order and seasonal order for the SARIMA model based on the Akaike Information Criterion (AIC). The `auto_arima` function is called with `seasonal=True`, `m=12` (for monthly seasonality), `suppress_warnings=True`, and `stepwise=True` to enable the stepwise search for the best hyperparameters.

3. **Model Fitting**: The SARIMA model is instantiated with the optimal order and seasonal order obtained from the `auto_arima` function using the `SARIMAX` class from the `statsmodels` library. The model is then fit to the state-specific ZHVI data using the `fit()` method.

4. **Model Saving**: The trained SARIMA model is saved to disk using the `joblib` library. The model file is named `{STATE_NAME}_sarima_model.joblib`, allowing for easy loading of the pre-trained model for future forecasting tasks.

## Model Evaluation

1. **In-sample Prediction**: In-sample predictions are generated using the `get_prediction()` method of the fitted SARIMA model. These predictions cover the same period as the training data and provide an assessment of the model's fit to the historical data.

2. **Out-of-sample Forecast**: Out-of-sample forecasts are generated using the `get_forecast()` method of the fitted SARIMA model. The forecast is made for the next 12 months beyond the available data, providing insights into future ZHVI trends.

3. **Model Evaluation Metrics**: The model's performance is evaluated using several metrics calculated on the data from 2024 onwards:
   - Mean Absolute Percentage Error (MAPE): Measures the average percentage difference between the predicted and actual values. Lower MAPE indicates better performance.
   - Root Mean Squared Error (RMSE): Quantifies the average magnitude of the prediction errors. Lower RMSE suggests better fit.
   - R-squared (R2): Represents the proportion of variance in the dependent variable explained by the model. Higher R2 indicates better explanatory power.

   The specific evaluation metrics for each state can be found in the respective state's log file. For example, in the `new-york_logs.txt` file, the following metrics are reported:
   - 2024 Onwards MAPE: 0.0010
   - 2024 Onwards RMSE: 527.50
   - 2024 Onwards R-squared: 0.9943

   These metrics provide a quantitative assessment of the model's performance and can be used to compare models across different states.

## Visualization and Saving Results

1. **Plotting**: The observed ZHVI values, in-sample predictions, and out-of-sample forecasts are plotted using the `matplotlib` library. The plot focuses on the data from 2024 onwards and includes the forecast confidence intervals. The plot is saved as `{STATE_NAME}_zhvi_forecast_2024_onwards.png` using the `plot_and_save()` function.

2. **Saving Forecast**: The forecasted ZHVI values for the next 12 months are saved to a CSV file named `{STATE_NAME}_zhvi_forecast_2024_onwards.csv` using the `to_csv()` function from pandas.

3. **Logging**: Key information and results are logged throughout the script using the `log_message()` function, which includes a timestamp for each message. The log messages provide insights into the progress of the pipeline and any relevant model details.

This standardized pipeline is applied to each state, with the only difference being the `STATE_NAME` variable and the corresponding state-specific data in the `ZHVI.csv` file. The consistent structure and use of functions ensure reproducibility and ease of customization for different states.

For more details on the specific implementation and code, please refer to the individual state scripts in the `state-scripts` directory.
