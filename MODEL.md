# SARIMA Model Architecture and Hyperparameters

This document provides an in-depth explanation of the Seasonal AutoRegressive Integrated Moving Average (SARIMA) model used in the Customizable Real Estate Market Forecasting Tool, including its architecture, hyperparameter selection, and performance metrics across different states.

## Model Architecture

The SARIMA model is a powerful time series forecasting technique that captures both trend and seasonality in the data. It combines the following components:

1. **Seasonal (S)**: The seasonal component accounts for the repeating patterns or seasonality in the data. In this project, the seasonal period is set to 12 to capture the yearly seasonality in the monthly ZHVI data.

2. **AutoRegressive (AR)**: The autoregressive component models the relationship between an observation and a certain number of lagged observations. The order of the AR term (p) determines the number of lag observations considered.

3. **Integrated (I)**: The integrated component involves differencing the time series data to remove the trend and achieve stationarity. The order of differencing (d) specifies the number of times the data needs to be differenced.

4. **Moving Average (MA)**: The moving average component models the relationship between an observation and the residual errors from a moving average model applied to lagged observations. The order of the MA term (q) determines the number of lagged forecast errors considered.

The SARIMA model is denoted as SARIMA(p,d,q)(P,D,Q,m), where:
- p, d, q: Non-seasonal AR, differencing, and MA orders
- P, D, Q: Seasonal AR, differencing, and MA orders
- m: Seasonal period (set to 12 for monthly data)

## Hyperparameter Selection

The hyperparameters of the SARIMA model are automatically selected using the `auto_arima` function from the `pmdarima` library. This function employs a stepwise approach to find the best combination of hyperparameters based on the Akaike Information Criterion (AIC). The `auto_arima` function is called with the following arguments:
- `seasonal=True`: Indicates that the model should consider seasonal components.
- `m=12`: Sets the seasonal period to 12 for monthly data.
- `suppress_warnings=True`: Suppresses any warnings generated during the hyperparameter search.
- `stepwise=True`: Enables the stepwise search for the best hyperparameters.

The `auto_arima` function returns the best SARIMA model with the optimized order and seasonal order. The selected hyperparameters for each state can be found in the respective state's log file. For example, in the `new-york_logs.txt` file, the selected model is SARIMAX(2, 2, 2) with the following coefficients:
- ar.L1: 1.7018
- ar.L2: -0.8726
- ma.L1: -1.6621
- ma.L2: 0.8217
- sigma2: 1.37e+05

## Model Fitting and Saving

Once the optimal hyperparameters are obtained, the SARIMA model is instantiated using the `SARIMAX` class from the `statsmodels` library. The model is then fit to the state-specific ZHVI data using the `fit()` method. The trained model is saved to disk using the `joblib` library, with the file named `{STATE_NAME}_sarima_model.joblib` for easy loading in future forecasting tasks.

## Performance Metrics

The performance of the SARIMA model is evaluated using several metrics calculated on the data from 2024 onwards. These metrics provide a quantitative assessment of the model's accuracy and explanatory power. The key metrics reported for each state include:

1. **Mean Absolute Percentage Error (MAPE)**: MAPE measures the average percentage difference between the predicted and actual ZHVI values. A lower MAPE indicates better predictive accuracy. For example, in the `new-york_logs.txt` file, the 2024 Onwards MAPE is reported as 0.0010, suggesting high accuracy.

2. **Root Mean Squared Error (RMSE)**: RMSE quantifies the average magnitude of the prediction errors. It provides a measure of the model's fit to the data, with lower values indicating better performance. In the `new-york_logs.txt` file, the 2024 Onwards RMSE is reported as 527.50.

3. **R-squared (R2)**: R2 represents the proportion of variance in the ZHVI values that can be explained by the SARIMA model. It ranges from 0 to 1, with higher values indicating better explanatory power. In the `new-york_logs.txt` file, the 2024 Onwards R-squared is reported as 0.9943, suggesting a strong fit to the data.

These performance metrics are consistently reported for each state in their respective log files, allowing for a comparative assessment of the SARIMA model's effectiveness across different states.

## Consistency Across States

The SARIMA model architecture and hyperparameter selection process remain consistent across all state models. The `auto_arima` function handles the selection of the best hyperparameters for each state based on the characteristics of the respective state's ZHVI data. This ensures that the model is optimized for each state while maintaining a consistent overall approach.

However, it's important to note that the specific hyperparameters and performance metrics may vary between states due to differences in the underlying data patterns and trends. The log files provide detailed information on the selected hyperparameters and evaluation metrics for each state, enabling a nuanced understanding of the model's performance in different contexts.

For a comprehensive view of the SARIMA model's performance across states, please refer to the individual state log files and the summary of accuracy rates and R-squared values in the project's README file.
