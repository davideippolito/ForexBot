import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments

def download_oanda_data(access_token, account_id, instrument="EUR_USD", granularity='M5', start_date='2022-01-01T00:00:00Z', end_date='2023-01-01T00:00:00Z'):
    """
    Download historical forex data from OANDA for a given instrument and timeframe.

    Args:
    access_token (str): OANDA API access token.
    account_id (str): OANDA account ID.
    instrument (str): Currency pair in OANDA format. Default is EUR/USD.
    granularity (str): Granularity of the candles. 'M5' for 5 minutes.
    start_date (str): Start date for the data in ISO8601 format.
    end_date (str): End date for the data in ISO8601 format.

    Returns:
    pd.DataFrame: DataFrame containing the historical data.
    """
    api = API(access_token=access_token)
    params = {
        "from": start_date,
        "to": end_date,
        "granularity": granularity,
        "price": "M"  # Midpoint prices
    }
    r = instruments.InstrumentsCandles(instrument=instrument, params=params)
    data = api.request(r)
    
    # Process the data to a DataFrame or another preferable format here

    return data

# Example usage (You need to replace 'YOUR_ACCESS_TOKEN' and 'YOUR_ACCOUNT_ID' with your actual OANDA API credentials)
access_token = 'YOUR_ACCESS_TOKEN'
account_id = 'YOUR_ACCOUNT_ID'
data = download_oanda_data(access_token, account_id)
print(data)
