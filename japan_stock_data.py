import pandas as pd 
import yfinance as yf
import json
#csv_list = pd.read_csv('japan_all_stock.csv')
success_list = []

for num in range(1301, 10000):
    try:
        stock_data = yf.download(f'{num}.T', period = '1d', interval='1d')
        success_list.append(f'{num}.T')
    except:
        continue

with open('japanese_success_stock.json', 'w') as json_file:
    json.dump(success_list, json_file)