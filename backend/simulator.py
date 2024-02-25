import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

def analyze_portfolio(stock_investments, market_index, start_date, end_date):
    # Fetch historical data for stocks and the market index
    data = {stock: yf.download(stock, start=start_date, end=end_date) for stock in stock_investments.keys()}
    data[market_index] = yf.download(market_index, start=start_date, end=end_date)
    
    # Calculate the number of shares owned for each stock
    shares_owned = {}
    total_investment = sum(stock_investments.values())
    initial_market_price = data[market_index]['Open'].iloc[0]  # Price on the first trading day
    market_shares_owned = total_investment / initial_market_price

    for stock, investment in stock_investments.items():
        initial_price = data[stock]['Open'].iloc[0]  # Price on the first trading day
        shares_owned[stock] = investment / initial_price

    # Calculate daily portfolio value
    portfolio_value = pd.DataFrame(index=data[next(iter(stock_investments))].index)
    portfolio_value['Value'] = 0
    for stock in stock_investments.keys():
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

    plt.title('Portfolio Value vs. Market Index Over Time')
    plt.xlabel('Month')
    plt.ylabel('Total Value in $')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Print the final values
    final_portfolio_value = portfolio_value['Value'].iloc[-1]
    final_market_value = market_value['Value'].iloc[-1]
    print(f'Final Portfolio Value on {end_date}: ${final_portfolio_value:.2f}')
    print(f'Final Market Index Value on {end_date}: ${final_market_value:.2f}')

# Example usage
stocks_and_investments_quantum = {'MSFT': 0.23924443681137084, 'CAT': 0.3760605743518982, 'GILD': 0.3387084436331177, 'ECL': 0.0, 'DLR': 0.03604862763783264, 'EFX': 2.866733703613281e-07, 'TTWO': 0.006930490650177002, 'ARE': 4.1439849853515627e-07, 'DPZ': 6.5171044921875e-06, 'FFIV': 2.4539999389648436e-07}
stocks_and_investments_classical = {'MSFT': 0, 'CAT': 0.0560, 'GILD': 0.2130, 'ECL': 0, 'DLR': 0.1047, 'EFX': 0.1497, 'TTWO': 0.0847, 'ARE': 0, 'DPZ': 0.2049, 'FFIV': 0.1429}
market_index = '^GSPC'
start_date = '2022-01-01'
end_date = '2022-12-31'
analyze_portfolio(stocks_and_investments_quantum, market_index, start_date, end_date)
analyze_portfolio(stocks_and_investments_classical, market_index, start_date, end_date)