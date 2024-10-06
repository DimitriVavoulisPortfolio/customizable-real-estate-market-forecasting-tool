# Dataset Usage and License

The Zillow Home Value Index (ZHVI) dataset used in this project is sourced from Zillow and is licensed under the Creative Commons Public Domain Dedication (CC0 1.0 Universal) license. This document provides an overview of the dataset, its usage in the project, and the terms of the license.

## Dataset Overview

The ZHVI dataset contains historical home value data for various states in the United States. The dataset includes monthly ZHVI values, which represent the typical home value for a given state at a specific point in time. The data covers a wide range of states and spans multiple years, providing a comprehensive view of home value trends across the country.

## Usage in the Project

The ZHVI dataset serves as the foundation for the Customizable Real Estate Market Forecasting Tool. The dataset is used to train and evaluate Seasonal AutoRegressive Integrated Moving Average (SARIMA) models for each state. These models are designed to forecast future ZHVI trends based on historical patterns and seasonality.

The dataset is loaded from the `ZHVI.csv` file using the `load_and_preprocess_data()` function in the state-specific scripts. The relevant state data is extracted, cleaned, and preprocessed before being used for model training and evaluation.

The preprocessed data is used to train the SARIMA models, which are then employed to generate in-sample predictions and out-of-sample forecasts. The model's performance is evaluated using metrics such as Mean Absolute Percentage Error (MAPE), Root Mean Squared Error (RMSE), and R-squared (R2) on the data from 2024 onwards.

The forecasted ZHVI values are visualized using the `matplotlib` library and saved as PNG files for each state. Additionally, the forecasted values are saved to CSV files for further analysis and integration with other tools.

## Dataset License

The ZHVI dataset is licensed under the Creative Commons Public Domain Dedication (CC0 1.0 Universal) license. This license allows for the free use, modification, and distribution of the dataset without any restrictions or obligations.

The key terms of the CC0 1.0 Universal license are as follows:

1. The dataset is dedicated to the public domain, which means that the copyright holder has waived all rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by law.

2. You can copy, modify, distribute, and perform the work, even for commercial purposes, all without asking permission.

3. The license does not grant any trademark rights or rights to use the copyright holder's name for publicity purposes.

4. The dataset is provided "as is," without warranties of any kind, express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, and noninfringement.

For more details on the CC0 1.0 Universal license, please refer to the official license text: [https://creativecommons.org/publicdomain/zero/1.0/](https://creativecommons.org/publicdomain/zero/1.0/)

## Attribution

While not legally required, it is recommended to provide attribution to Zillow as the source of the ZHVI dataset when using it in the Customizable Real Estate Market Forecasting Tool or any derived works. Attribution helps acknowledge the original data provider and promotes transparency.

## Disclaimer

The ZHVI dataset is provided "as is" without any warranties or guarantees of its accuracy, completeness, or suitability for any particular purpose. The project maintainers and contributors shall not be liable for any errors, omissions, or damages arising from the use of the dataset or the Customizable Real Estate Market Forecasting Tool.

Users of the dataset and the forecasting tool are responsible for ensuring compliance with any applicable laws, regulations, or third-party rights when using the data for their specific purposes.

