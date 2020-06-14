from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()
import pandas as pd

#Tickers List
ticker_list=['DJIA', 'DOW', 'LB', "EXPE", 'PXD']

today = date.today()
start_date="2019-10-20"

files=[]
def getData(ticker):
    print(ticker)
    data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
    dataname = ticker + '_' +str(today)
    files.append(dataname)
    SaveData(data, dataname)

def SaveData(df, data):
    df.to_csv('./data/'+data+'.csv')


for tik in ticker_list:
    getData(tik)

for i in range(0,5):
    df1 = pd.read_csv('./data/'+str(files[i]) + '.csv')
    print(df1.head)


