import pandas_datareader as web 
from matplotlib import pyplot as plt
from datetime import datetime

plt.close('all')

# Gets information from yahoo finances about stock information

symbols = ['MSFT', 'AMZN', 'AAPL', 'GOOG', 'META']
start_date = datetime(2022, 6, 1)
end_date = datetime(2022, 12, 1)
stock_data = web.get_data_yahoo(symbols, start_date, end_date)

# Formatting for all future charts. labelFormatOut just moves the label out a little.

labelFormatOut = {'size': 20, 'weight': 'bold', 'labelpad': 20}
labelFormat = {'size': 20, 'weight': 'bold'}
titleFormat = {'size': 30, 'weight': 'bold', 'y': 1.03}

# Creates the Stock Prices Figure 

plt.figure(figsize = (12,8))
plt.plot(stock_data['Adj Close'])
plt.title('Tech Stocks Adjusted Price (2022)', **titleFormat)
plt.xlabel('Date', **labelFormatOut)
plt.ylabel('Adjusted Closing Price Over Time', **labelFormatOut)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 12)
plt.legend(symbols, title='Symbols')

# Creates the Simple Rates of Return figure

plt.figure(figsize = (12, 8))
plt.plot(stock_data['Adj Close'].pct_change())
plt.title('Simple Rates of Return Over Time (2022)', **titleFormat)
plt.xlabel('Date (YYYY-MM)', **labelFormatOut)
plt.ylabel('Daily Rate of Return', **labelFormatOut)
plt.xticks(fontsize = 15, rotation = 30)
plt.yticks(fontsize = 12)
plt.legend(symbols, title='Symbols')

# Creates Individual Rates of Returns figures

plt.figure(figsize = (12, 8))
stock_change = stock_data['Adj Close'].pct_change()

plt.subplot(321)
plt.plot(stock_change.MSFT)
plt.title('Microsoft', fontweight='bold')

plt.subplot(322)
plt.plot(stock_change.AMZN)
plt.title('Amazon', fontweight='bold')

plt.subplot(323)
plt.plot(stock_change.AAPL)
plt.title('Apple', fontweight='bold')

plt.subplot(324)
plt.plot(stock_change.GOOG)
plt.title('Google', fontweight='bold')

plt.subplot(325)
plt.plot(stock_change.META)
plt.title('Facebook (Meta)', fontweight='bold')

plt.tight_layout()

# Creates the Average Daily Rate of Return figure

average_change = stock_change.mean()

plt.figure(figsize = (12, 8))
colored_bars = lambda x: ['#90EE90' if y > 0 else '#FF4122' for y in x]
stock_per = [round(x * 100, 2) for x in average_change]
plt.bar(symbols, stock_per, color = colored_bars(stock_per))
plt.title('Average Daily Rate of Return', **titleFormat)
plt.ylabel('Rate of Return (%)', **labelFormatOut)
plt.xlabel('Technology Stocks', **labelFormat)

plt.ylim([-0.30, 0.05])

ax = plt.subplot()
ax.set_xticklabels(['Microsoft', 'Amazon', 'Apple', 'Google', 'Facebook (META)'], rotation = 30, size = 15)
plt.yticks(size = 12)

# Plots the Standard Deviation (Volatility) figure

stock_std = stock_change.std()

plt.figure(figsize = (12, 8))
plt.bar(symbols, stock_std, color='#92DFF3')
plt.title('Volatility of Stocks (Standard Dev.)', **titleFormat)
plt.xlabel('Company', **labelFormat)
plt.ylabel('Standard Deviation', **labelFormatOut)
plt.yticks(fontsize=12)

ax = plt.subplot()
ax.set_xticklabels(['Microsoft', 'Amazon', 'Apple', 'Google', 'Facebook'], rotation = 30, fontsize=15)

# Correlations chart (Visualized through Jupyter Notebook)

stock_corr = stock_data['Adj Close'].corr()
    
def color_map(val):
    color = '#cdcdcd' if val >= 1.0 else createShade(val)
    return 'background-color: %s' % color

def createShade(value):
    return '#FF{}FF'.format(hex(int(float(value)*255.0))[2:])

stock_corr = stock_corr.style.applymap(color_map)

# Shows all pyplot figures

plt.show()
