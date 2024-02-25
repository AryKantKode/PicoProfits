import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# Define the stocks and the initial investment in dollars for each stock
stocks = ['LUMN', 'MSFT', 'GOOGL']  # Example stocks
investments = [1000, 500, 10]  # Corresponding investments in dollars
market_index = '^GSPC'  # S&P 500 index as the market benchmark

# Fetch historical data for 2023 for both stocks and the market index
start_date = '2023-01-01'
end_date = '2023-12-31'
data = {stock: yf.download(stock, start=start_date, end=end_date) for stock in stocks}
data[market_index] = yf.download(market_index, start=start_date, end=end_date)

# Calculate the number of shares owned for each stock
shares_owned = {}
total_investment = sum(investments)
initial_market_price = data[market_index]['Open'].iloc[0]  # Price on the first trading day of 2023
market_shares_owned = total_investment / initial_market_price

for stock, investment in zip(stocks, investments):
    initial_price = data[stock]['Open'].iloc[0]  # Price on the first trading day of 2023
    shares_owned[stock] = investment / initial_price

# Calculate daily portfolio value
portfolio_value = pd.DataFrame(index=data[stocks[0]].index)
portfolio_value['Value'] = 0
for stock in stocks:
    portfolio_value['Value'] += data[stock]['Close'] * shares_owned[stock]

# Calculate daily market index value
market_value = pd.DataFrame(index=data[market_index].index)
market_value['Value'] = data[market_index]['Close'] * market_shares_owned

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(portfolio_value.index, portfolio_value['Value'], label='Portfolio Value')
plt.plot(market_value.index, market_value['Value'], label='Market Index Value', linestyle='--')

# Formatting the date axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))  # Month abbreviations
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Ensure each month is marked
plt.gcf().autofmt_xdate()  # Auto-format to improve readability

plt.title('Portfolio Value vs. Market Index Over Time (2023)')
plt.xlabel('Month')
plt.ylabel('Total Value in $')
plt.legend()
plt.grid(True)
plt.show()

# Print the final values
final_portfolio_value = portfolio_value['Value'].iloc[-1]
final_market_value = market_value['Value'].iloc[-1]
print(f'Final Portfolio Value on Dec 31, 2023: ${final_portfolio_value:.2f}')
print(f'Final Market Index Value on Dec 31, 2023: ${final_market_value:.2f}')
