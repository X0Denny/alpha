from fastquant import get_crypto_data
import pandas as pd
import matplotlib.pyplot as plt

BTC = get_crypto_data("BTC/USDT", "2020-01-01", "2022-03-07")


BTC.close.plot(figsize=(10, 6))
plt.title("Daily Closing Prices of BTC\nfrom 2020-01-01 to 2022-03-07", fontsize=20)

ma30 = BTC.close.rolling(30).mean()
close_ma30 = pd.concat([BTC.close, ma30], axis=1).dropna()
close_ma30.columns = ['Closing Price', 'Simple Moving Average (30 day)']

close_ma30.plot(figsize=(10, 6))
plt.title("Daily Closing Prices vs 30 day SMA of BTC\nfrom 2020-01-01 to now", fontsize=20)

all_in = pd.concat([BTC.open, BTC.high, BTC.close, ma30], axis=1).dropna()
all_in.tail(7)


#             open    high     low     close    volume
# dt                                                          
# 2018-12-01  4041.27  4299.99  3963.01  4190.02  44840.073481
# 2018-12-02  4190.98  4312.99  4103.04  4161.01  38912.154790
# 2018-12-03  4160.55  4179.00  3827.00  3884.01  49094.369163
# 2018-12-04  3884.76  4085.00  3781.00  3951.64  48489.551613
# 2018-12-05  3950.98  3970.00  3745.00  3769.84  44004.799448