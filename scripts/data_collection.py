from alpha_vantage.timeseries import TimeSeries
from dotenv import load_dotenv
import os

# Import environment    
load_dotenv()

api_key = os.environ.get("ALPHA_VANTAGE_API_KEY")
ts = TimeSeries(key=api_key, output_format='pandas')
stock_symbol = 'GOOG'
data, metadata= ts.get_daily(symbol=stock_symbol, outputsize='full')

print(data)