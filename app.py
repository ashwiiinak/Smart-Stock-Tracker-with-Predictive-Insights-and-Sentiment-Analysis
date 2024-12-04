import streamlit as st
import pandas as pd
from data_fetcher import fetch_stock_data
from portfolio_manager import calculate_portfolio
from sentiment_analysis import get_stock_news, analyze_sentiment
from indicators import calculate_rsi

# Set up Streamlit app
st.title('Stock Market Tracker')

# Input for stock symbol and date range
stock_symbol = st.text_input('Enter Stock Symbol (e.g., AAPL, GOOGL)', 'AAPL')
start_date = st.date_input('Start Date', pd.to_datetime('2023-01-01'))
end_date = st.date_input('End Date', pd.to_datetime('2023-12-31'))

# Fetch stock data
st.write(f"Fetching data for {stock_symbol} from {start_date} to {end_date}...")
stock_data = fetch_stock_data(stock_symbol, str(start_date), str(end_date))

# Calculate RSI and show it
data_with_rsi = calculate_rsi(stock_data)
st.write("Stock Data with RSI:", data_with_rsi)

# Display Portfolio
portfolio = {'AAPL': {'purchase_price': 150, 'quantity': 10}}  # Example portfolio
latest_prices = {stock_symbol: stock_data['Close'].iloc[-1]}  # Latest price

portfolio_value = calculate_portfolio(portfolio, latest_prices)
st.write(f"Portfolio Value: ${portfolio_value['Gain/Loss'].sum()}")

# Sentiment Analysis on Stock News
api_key = st.text_input('Enter NewsAPI Key', type='password')
if api_key:
    news_articles = get_stock_news(stock_symbol, api_key)
    sentiments = analyze_sentiment(news_articles)
    st.write("Sentiment Analysis of Recent News:", pd.DataFrame(sentiments))
