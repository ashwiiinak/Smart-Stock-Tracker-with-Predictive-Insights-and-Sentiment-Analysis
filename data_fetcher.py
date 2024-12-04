import yfinance as yf

def fetch_stock_data(stock_symbol, start_date, end_date):
    """
    Fetch stock data from Yahoo Finance.
    
    Parameters:
        stock_symbol (str): The stock symbol.
        start_date (str): Start date for the data.
        end_date (str): End date for the data.
        
    Returns:
        pd.DataFrame: The stock data.
    """
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    return stock_data
