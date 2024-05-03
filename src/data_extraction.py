import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd

def get_data_for_scalping(symbol, timeframe=mt5.TIMEFRAME_M5, look_back_days=30):
    """
    Collects historical data for scalping.

    Args:
    symbol (str): The symbol for which to collect data, e.g., 'EURUSD'.
    timeframe (uint): The timeframe for the data in MT5 terms.
    look_back_days (int): How many days back to collect data.

    Returns:
    pd.DataFrame: DataFrame containing the historical data.
    """
    # Set the timezone to UTC for consistency
    timezone = pytz.UTC
    utc_from = datetime.now(timezone) - pd.Timedelta(days=look_back_days)
    utc_to = datetime.now(timezone)
    
    # Enable the display of floating point values with two decimal places
    pd.set_option('display.float_format', '{:.2f}'.format)
    
    # Check if the desired symbol is available in MT5
    if not symbol in mt5.symbols_get():
        print(f"Symbol {symbol} not found, can't get history.")
        return None

    # Set the symbol
    mt5.symbol_select(symbol, True)
    
    # Get the historical data
    rates = mt5.copy_rates_range(symbol, timeframe, utc_from, utc_to)
    
    # Shutdown the MT5 connection
    mt5.shutdown()

    # Create a DataFrame from the obtained data
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    
    # Return the DataFrame with the historical data
    return df

# Example usage:
data = get_data_for_scalping("EURUSD")
print(data.head())
