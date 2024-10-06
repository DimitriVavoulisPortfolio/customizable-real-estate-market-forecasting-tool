# Customizable Real Estate Market Forecasting Tool

## Project Overview

This project provides a customizable real estate market forecasting tool that uses SARIMA (Seasonal AutoRegressive Integrated Moving Average) models to predict Zillow Home Value Index (ZHVI) trends at different geographical levels, such as states and cities. The tool is designed to be a low-cost market research solution that offers the nuance of an actual market researcher, making it valuable for real estate businesses, investors, and analysts.

### Key Features

- Customizable SARIMA models for forecasting ZHVI trends
- Supports forecasting at different geographical levels (states, cities)
- Designed for low compute costs to maximize scalability
- Data processing and model training pipeline
- Comprehensive testing and evaluation of models
- Structured project for easy navigation and understanding

## Project Structure

1. **models**: Pre-trained SARIMA models for each geographic level
2. **state-documentation**: Documentation and guides for each state model
3. **state-outputs**: Forecast outputs and visualizations for each state
4. **state-scripts**: Data processing, model training, and forecasting scripts for each state
5. **README.md**: Overview and guide to using the forecasting tool
6. **ZHVI.csv**: Zillow Home Value Index dataset used for training and forecasting

## Documentation

- **README.md**: This file, providing an overview of the project and its usage
- **state-documentation**: Detailed documentation for each state model, including customization instructions and interpreting outputs
- **PROCESS.md**: Detailed explanation of the data processing and model training pipeline
- **MODEL.md**: In-depth description of the SARIMA model architecture and hyperparameters

## Model Performance

The project includes SARIMA models for several states, each demonstrating high accuracy in forecasting ZHVI trends. The accuracy rates and R-squared values for the state models, sorted from highest to lowest accuracy, are as follows:

1. New York: 99.43%
2. New Jersey: 99.02%
3. Pennsylvania: 98.99%
4. Massachusetts: 98.11%
5. Illinois: 97.41%
6. Washington: 96.36%
7. North Carolina: 95.55%
8. California: 91.84%
9. Florida: 87.48%
10. Texas: 83.41%

These accuracy rates and R-squared values are derived from the model's performance on the test set, which is a portion of the data held out during training to evaluate the model's ability to generalize to unseen data.

## Usage Guide

1. Clone the repository:
   ```
   git clone https://github.com/DimitriVavoulis/customizable-real-estate-market-forecasting-tool.git
   cd customizable-real-estate-market-forecasting-tool
   ```

2. Install dependencies:
   ```
   pip install pandas numpy matplotlib statsmodels joblib
   ```

3. Run the desired state's forecasting script. There are 10 state scripts available:
   - `california-zhvi-sarima-forecast-script.py`
   - `florida-zhvi-sarima-forecast-script.py`
   - `illinois-zhvi-sarima-forecast-script.py`
   - `massachusetts-zhvi-sarima-forecast-script.py`
   - `new-jersey-zhvi-sarima-forecast-script.py`
   - `new-york-zhvi-sarima-forecast-script.py`
   - `north-carolina-zhvi-sarima-forecast-script.py`
   - `pennsylvania-zhvi-sarima-forecast-script.py`
   - `texas-zhvi-sarima-forecast-script.py`
   - `washington-zhvi-sarima-forecast-script.py`

   For example, to run the California forecasting script:
   ```
   python california-zhvi-sarima-forecast-script.py
   ```

4. Follow the prompts to input the desired forecast horizon and view the output in the `state-outputs` directory.

For detailed usage instructions and customization options, refer to the state-specific documentation in the `state-documentation` directory.

## Future Enhancements

- Expand coverage to more states and cities
- Implement a user-friendly web interface for easier interaction
- Integrate additional data sources for more comprehensive forecasts
- Explore other forecasting models and techniques for comparison

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions, suggestions, or collaborations, please open an issue on the GitHub repository or contact [Dimitri Vavoulis](mailto:dimitrivavoulis3@gmail.com).
