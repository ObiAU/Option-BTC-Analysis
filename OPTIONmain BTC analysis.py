import requests
import sqlite3
import pandas as pd
import numpy as np
import datetime
from math import pi, sin
from matplotlib import pyplot as plt

#Formatting dates for this Friday's expiration and next Friday's:
today = datetime.date.today()
friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
next_friday = friday + datetime.timedelta(7)

friday = (datetime.date.strftime(friday, "%d%b%y")).upper()
if friday[0] == "0":
    friday = friday[1:]

next_friday = (datetime.date.strftime(next_friday, "%d%b%y")).upper()
if next_friday[0] == "0":
    next_friday = next_friday[1:]

#Bitcoin strike prices
ints = np.arange(10000, 30000, 1000).tolist()
strike_prices = [str(x) for x in ints]

#API call formatting
token = "BTC"
expiration_date = [friday, next_friday]

#P=put C=call:
option_type = "C"

raw_strike_data=[]

for date in expiration_date:
    for strike in strike_prices:
        string = "https://test.deribit.com/api/v2/public/get_book_summary_by_instrument?instrument_name="+token+"-"+date+"-"+strike+"-"+option_type
        result = requests.get(string).json()
        if 'error' not in result:
            raw_strike_data.append([token, date, strike,result["result"][0]['volume'], result["result"][0]['open_interest'], result["result"][0]['underlying_price']])

strike_price_df = pd.DataFrame(raw_strike_data, columns =['Token','Expiration Date', 'Strike Price','Volume','Open Interest','Underlying Price'])
print(strike_price_df)

#Graph 1 will denote Volume against Strike price between 9SEP22 and 16SEP22 (Call options)
x1 = [*range(18000, 27000, 1000)]
y1 = [0.0, 2355.5, 612.2, 11.0, 3602.1, 0.0, 48.0, 0.0, 0.0]

plt.plot(x1, y1, label = '9SEP22')


x2 = [*range(18000, 26000, 1000)]
y2 = [0.0, 76.8, 61.1, 24.0, 0.0, 0.0, 217.3, 0.0]

plt.plot(x2, y2, label = '16SEP22')

plt.xlabel('Strike Price')
plt.ylabel('Volume')
plt.title('Call Options: Strike Price against Volume')
plt.legend()
plt.show()
#Graph 2 will denote Open Interest against Strike price between 9SEP22 and 16SEP22(Call options)

x1 = [*range(18000, 27000, 1000)]
y1 = [0.1, 772.9, 648.2, 1556.4, 8052.3, 690.4, 1038.1, 1156.5, 1213.0]

plt.plot(x1, y1, label = '9SEP22')

x2 = [*range(18000, 26000, 1000)]
y2 = [1051.1, 987.3, 1876.6, 1503.0, 2199.1, 1943.8, 542.3, 292.7]

plt.plot(x2, y2, label = '16SEP22')
plt.xlabel('Strike Price')
plt.ylabel('Open Interest')
plt.title('Call Options: Strike Price against Open Interest')
plt.legend()
plt.show()

#Graph 3 will analyse the differences between put and call options popularities w.r.t Volume on the given expiration (16SEP22) updating via the URL

#quick comparative def
option_type = "C"
option_type2 = "P"

x1 = [*range(18000, 26000, 1000)]
y1 = []
for date in expiration_date:
    for strike in strike_prices:
        string = "https://test.deribit.com/api/v2/public/get_book_summary_by_instrument?instrument_name="+token+"-"+date+"-"+strike+"-"+option_type
        result = requests.get(string).json()
        if 'error' not in result:
            y1.append(result["result"][0]['volume'])

plt.plot(x1, y1, label = 'Call Options')

x2 = [*range(18000, 26000, 1000)]
y2 = []
for date in expiration_date:
    for strike in strike_prices:
        string = "https://test.deribit.com/api/v2/public/get_book_summary_by_instrument?instrument_name="+token+"-"+date+"-"+strike+"-"+option_type2
        result = requests.get(string).json()
        if 'error' not in result:
            y2.append(result["result"][0]['volume'])

plt.plot(x2, y2, label = 'Put Options')

plt.xlabel('Strike Price')
plt.ylabel('Volume')
plt.title('Put against Calls: Volume 16SEP22')
plt.legend()
plt.show()





#Graph 4 will analyse the differences between put and call options popularities w.r.t Open Interest on the given expiration (16SEP22) from the URL

x1 = [*range(18000, 26000, 1000)]
y1 = []
for date in expiration_date:
    for strike in strike_prices:
        string = "https://test.deribit.com/api/v2/public/get_book_summary_by_instrument?instrument_name="+token+"-"+date+"-"+strike+"-"+option_type
        result = requests.get(string).json()
        if 'error' not in result:
            y1.append(result["result"][0]['open_interest'])

plt.plot(x1, y1, label = 'Call Options')

x2 = [*range(18000, 26000, 1000)]
y2 = []
for date in expiration_date:
    for strike in strike_prices:
        string = "https://test.deribit.com/api/v2/public/get_book_summary_by_instrument?instrument_name="+token+"-"+date+"-"+strike+"-"+option_type2
        result = requests.get(string).json()
        if 'error' not in result:
            y2.append(result["result"][0]['open_interest'])

plt.plot(x2, y2, label = 'Put Options')

plt.xlabel('Strike Price')
plt.ylabel('Open Interest')
plt.title('Put against Calls: Open Interest 16SEP22')
plt.legend()
plt.show()






#call data for 16SEP22 BTC


#C_data_BTC = [('BTC', '16SEP22', 18000, 0.0, 1051.1, 19670.97),
#                  ('BTC', '16SEP22', 19000, 37.9, 987.3, 19670.97),
#                  ('BTC', '16SEP22', 20000, 61.1, 1876.6, 19670.97),
#                  ('BTC', '16SEP22', 21000, 24.0, 1503.0, 19670.97),
#                  ('BTC', '16SEP22', 22000, 0.0, 2199.1, 19670.97),
#                  ('BTC', '16SEP22', 23000, 0.0, 1943.8, 19670.97),
#                  ('BTC', '16SEP22', 24000, 217.3, 542.3, 19670.95),
#                  ('BTC', '16SEP22', 25000, 0.0, 292.7, 19671.11),]





