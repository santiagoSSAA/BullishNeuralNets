# 3. Data Collection

One of the key components of this project is obtaining reliable historical stock price data, which will be used to train our machine learning model. In this section, we'll explore how to retrieve this data using a financial data API and how to preprocess it for use in our AI model.

## Explain how to obtain historical stock price data using a financial data API (e.g. Alpha Vantage)

There are various APIs available that provide access to historical stock price data. For this tutorial, we'll use the Alpha Vantage API, which offers a free tier with limited access to stock data. Here's how you can use Alpha Vantage to retrieve historical stock prices:

1. **Sign up for an API key** Visit the Alpha Vantage website (https://www.alphavantage.co/) and sign up for a free API key.
    
2. **Install the Alpha Vantage Python library** In your terminal or command prompt, run the following command to install the Alpha Vantage Python library:

        pip install alpha-vantage

3. Fetch historical stock data Create a new Python file (e.g., `data_collection.py`) and add the following code:

    ```python
    from alpha_vantage.timeseries import TimeSeries

    # Replace with your API key
    api_key = 'YOUR_API_KEY'

    # Initialize the TimeSeries object
    ts = TimeSeries(key=api_key, output_format='pandas')

    # Retrieve historical data for a stock symbol
    stock_symbol = 'AAPL'  # Replace with the desired stock symbol
    data, meta_data = ts.get_daily(symbol=stock_symbol, outputsize='full')

    # Print the data
    print(data)
    ```
    Replace `'YOUR_API_KEY'` with the API key you obtained from Alpha Vantage, and `'AAPL'` with the stock symbol you want to retrieve data for. When you run this code, it will fetch and print the historical daily stock prices for the specified stock symbol.

## Show how to structure and clean data for use in the AI model

The data retrieved from the Alpha Vantage API will be in a Pandas DataFrame format, which makes it easy to manipulate and clean the data. Here are some common steps you may need to perform:

1. **Handle missing data** Check for and handle any missing values in the data using Pandas' built-in functions like `dropna()` or `fillna()`.

2. **Convert data types** Ensure that the data types of the columns are correct (e.g., convert the date column to a datetime format).

3. **Feature engineering** Create new features or transformations of the existing data that may be useful for training the machine learning model (e.g., calculate moving averages, technical indicators, etc.).

4. **Split the data** into training and testing sets to evaluate the performance of your machine learning model.

    ```Python
    import pandas as pd

    # Assuming 'data' is the DataFrame containing historical stock data

    # Convert the date column to datetime format
    data['date'] = pd.to_datetime(data['date'])

    # Set the date column as the index
    data = data.set_index('date')

    # Handle missing values
    data = data.dropna()

    # Create a new feature 'daily_return'
    data['daily_return'] = data['close'].pct_change()

    # Split the data into training and testing sets
    train_data = data.loc[:train_end_date]
    test_data = data.loc[train_end_date:]
    ```

In this example, we convert the date column to datetime format, set it as the index, drop any rows with missing values, create a new feature `'daily_return'` representing the daily percentage change in closing prices, and split the data into training and testing sets based on a specified `train_end_date`.

***After completing this section, you'll have historical stock price data retrieved from the Alpha Vantage API, cleaned and structured in a way that can be used to train your machine learning model in the next step.***