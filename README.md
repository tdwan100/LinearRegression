# Housing Price Prediction using Linear Regression

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains a simple Python script to perform linear regression and predict housing prices based on the size of the house (lotsize). The dataset used in this example is stored in a CSV file named `Housing.csv`.

## Requirements

Make sure you have the following installed before running the script:
- Python (>= 3.x)
- NumPy
- Pandas
- Matplotlib
- scikit-learn

You can install the required packages using pip:

```
pip install numpy pandas matplotlib scikit-learn
```

## Getting Started

1. Clone this repository to your local machine or download the `Housing.csv` file from this repository.

```
git clone https://github.com/your-username/housing-price-prediction.git
cd housing-price-prediction
```

2. Make sure `Housing.csv` is placed in the same directory as the script.

## Usage

To run the housing price prediction script, execute the following command:

```
python predict_prices.py
```

## Description

The script performs the following steps:

1. Loads the housing dataset from `Housing.csv` using pandas.
2. Prepares the data by extracting the 'lotsize' column as the feature (X) and the 'price' column as the target (Y).
3. Splits the data into training and testing sets. The last 250 samples are kept for testing, while the remaining samples are used for training.
4. Creates a linear regression model using scikit-learn's `LinearRegression`.
5. Trains the model on the training data.
6. Predicts housing prices for the test data using the trained model.
7. Plots the original test data points along with the regression line for visualization.

## Results

Upon running the script, a scatter plot will be displayed showing the original test data points and the regression line representing the predicted housing prices. The plot will be saved as `housing_prices.png` in the same directory.

## Customization

You can customize the script to work with your own dataset by replacing the `Housing.csv` file with your data file and adjusting the columns used for feature (X) and target (Y) variables.

## Contributing

If you find any issues with the code or want to add improvements, feel free to create a pull request. Contributions are always welcome!

