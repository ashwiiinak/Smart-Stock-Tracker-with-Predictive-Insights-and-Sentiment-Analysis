import pandas as pd

def calculate_portfolio(portfolio, stock_data):
    """
    Calculate the total value of a stock portfolio based on the latest stock prices.
    
    Parameters:
        portfolio (dict): A dictionary where keys are stock symbols and values are dictionaries with 'purchase_price' and 'quantity'.
        stock_data (dict): A dictionary with stock symbols as keys and their current prices as values.
        
    Returns:
        pd.DataFrame: A DataFrame showing stock, current price, quantity, and gain/loss.
    """
    results = []
    for stock, details in portfolio.items():
        purchase_price = details['purchase_price']
        quantity = details['quantity']
        current_price = stock_data.get(stock, None)
        if current_price is not None:
            gain_loss = (current_price - purchase_price) * quantity
            results.append({'Stock': stock, 'Current Price': current_price, 'Quantity': quantity, 'Gain/Loss': gain_loss})
    
    return pd.DataFrame(results)
