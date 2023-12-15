import pandas as pd

import plotly.graph_objects as go

# Read the stock data
stockData = pd.read_csv("/home/needjobcoder/devlopment/python/dataSciencePractice/practice/stockMarket/indexProcessed.csv")

# Convert 'Date' column to datetime
stockData = stockData.tail(1200)
# Extract columns
dates = stockData['Date']
high = stockData['High']
low = stockData['Low']
_open = stockData['Open']
close = stockData['Close']

cumulative_line = stockData['Close'].cumsum()
window_size = 50
moving_average = close.rolling(window=window_size).mean()
moving_average_open = _open.rolling(window=window_size).mean()

fig = go.Figure(data=[go.Candlestick(x=dates,
                open=_open,
                high=high,
                low=low,
                close=close)])

fig.add_trace(go.Scatter(x=dates,
                         y=cumulative_line,
                         mode='lines',
                         name='Cumulative Line'))

fig.add_trace(go.Scatter(x=dates,
                         y=moving_average,
                         mode='lines',
                         name=f'{window_size}-Day Moving Average'))

fig.add_trace(go.Scatter(x=dates,
                         y=moving_average_open,
                         mode='lines',
                         name=f'{window_size}-Day Moving Average Open'))

fig.update_layout(xaxis_title='Year',
                  yaxis_title='Stock Price Dollars',
                  title='Stock Price Candlestick Chart')

fig.show()
