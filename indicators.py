import pandas as pd

def calculate_rsi(data, window=14):
    """
    Calculate the Relative Strength Index (RSI) of a given dataset.

    Parameters:
        data (pd.Series): The closing price series.
        window (int): The lookback period for RSI calculation.

    Returns:
        pd.Series: The RSI values.
    """
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
