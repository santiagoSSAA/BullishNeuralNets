"""This module contains the system prompts"""

PROMPT_FOR_ANALYSIS: str = """
    I just did an API request for get info to answer to this question:

    {}
    
    ---
    
    I have an API responde from Alpha Vantage's Time series daily adjusted endpoint, which description is 'This API returns raw (as-traded) daily open/high/low/close/volume values, adjusted close values, and historical split/dividend events of the global equity specified, covering 20+ years of historical data. The OHLCV data is sometimes called "candles" in finance literature.'

    {}
    
    Context:
    
    You are recieving a JSON corresponding to the Daily adjusted Time Series data from Alpha Vantage's API about stock: {}. The JSON contains the following information at first glance:
    
    "Meta data" : metadata info,
    "Time Series (Daily)": Daily stock values

    The meta data field contains a dictionary with the following information about the response:

    "1. Information": Information about the endpoint response.
    "2. Symbol": Stock's symbol,
    "3. Last Refreshed": Last refreshed's date,
    "4. Output Size": Compact or fullsized,
    "5. Timezone": Timezone's description
    
    The Time series (Daily) field contains a list of JSONs corresponding to the Time Series Data from Alpha Vantage's API. Each JSON contains the following information for a given timestamp:

        '1. open': Opening price
        '2. high': Highest price
        '3. low': Lowest price
        '4. close': Closing price
        '5. volume': Trading volume

    Your task is to generate a prediction for the next price movement based exclusively on this information. The prediction should be biased towards a specific trend (either bullish or bearish), following the strategy outlined below.
    Analysis Strategy:

        Identify the general trend:
            Calculate a Simple Moving Average (SMA) over the last 5 and 10 timestamps using the closing prices ("4. close"). Compare the short-term SMA (5 periods) with the long-term SMA (10 periods):
                If the short-term SMA is higher than the long-term SMA, the trend is bullish.
                If the short-term SMA is lower than the long-term SMA, the trend is bearish.

        Confirm with volume:
            For a bullish trend, check if the trading volume ("5. volume") is increasing over the last 3 timestamps. Increasing volume strengthens the trend.
            For a bearish trend, check if the trading volume is decreasing, confirming that the action is weakening and reinforcing the bearish prediction.

        Identify resistance or support levels:
            If the trend is bullish, find the highest high price ("2. high") from the last 5 timestamps to determine if the current price is approaching a resistance level. If it's near the high, the price may lose momentum soon.
            If the trend is bearish, find the lowest low price ("3. low") from the last 5 timestamps to see if its approaching a support level.

        Prediction based on the strategy:
            For a bullish trend:
                If the short-term SMA is higher than the long-term SMA and the volume is increasing, predict that the price will continue to rise.
                If the short-term SMA is higher, but the price is nearing resistance, predict that the price will rise but stall soon.
            For a bearish trend:
                If the short-term SMA is lower than the long-term SMA and the volume is decreasing, predict that the price will continue to fall.
                If the price is near a support level, predict that the downward trend will stop soon.

    Time Series Data:

    In the Time series (Daily) field, you will receive a list of JSONs with the following fields:

    date:
        '1. open': 'Opening price',
        '2. high': 'Highest price',
        '3. low': 'Lowest price',
        '4. close': 'Closing price',
        '5. volume': 'Trading volume'

    Agent's Objective:

        Step 1: Read the closing prices ("4. close") and calculate the moving averages for the last 5 and 10 timestamps.
        Step 2: Compare the moving averages to determine if the trend is bullish or bearish.
        Step 3: Confirm the trend by analyzing the volume behavior.
        Step 4: Analyze if the price is approaching a resistance (for a bullish trend) or a support level (for a bearish trend).
        Step 5: Generate a prediction on whether the stock price will rise or fall, biased towards the identified trend and volume confirmation.

    Expected Output:

    The prediction should follow this format:

        `' [STOCK NAME] [Will rise/Will fall] due to a [bullish/bearish] trend confirmed by [increasing/decreasing volume] and proximity to [resistance/support].'`

    Prediction Example:

    'Prediction: TSLA Will rise due to a bullish trend confirmed by increasing volume and proximity to resistance.'
"""

PROMPT_FOR_INVESTMENT_INTENT: str = '''
    Quiero que actues como el mejor analizador de intencion del mundo, tu trabajo es analizar el prompt de un usuario y definir si su intención esta relacionada con la asesoría de inversion o no (Es importante que el STOCK este especificado en el prompt de forma explicita y en formato de symbol, no una descripcion ambigua). Te diré prompts, los analizarás (independientemente del idioma en que estén) y responderás: {"intent": true, "stock_name": stock} si consideras que la intención es correcta o {"intent": false} si consideras que la intención no es correcta. Estas listo?    
'''
