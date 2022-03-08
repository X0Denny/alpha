from fastquant import get_crypto_data
import pandas as pd
import matplotlib.pyplot as plt

ETH = get_crypto_data("ETH/USDT", "2020-01-01", "2022-03-08")

%matplotlib inline
ETH.close.plot(figsize=(10, 6))


ma30 = ETH.close.rolling(30).mean()
close_ma30 = pd.concat([ETH.close, ma30], axis=1).dropna()
close_ma30.columns = ['Closing Price', 'Simple Moving Average (30 day)']

close_ma30.plot(figsize=(16, 6))
plt.title("Daily Closing Prices vs 30 day SMA of ETH\nfrom 2020-01-01 to now", fontsize=20)


all_in = pd.concat([ETH.open, ETH.high, ETH.close, ma30], axis=1).dropna()
all_in.tail(30)