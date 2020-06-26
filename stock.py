from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()
import pandas as pd


ticker_list=[]

#Check if the user-input symbol is a company in NYSE
def checkComp():
    return


#This function adds user-desired companies to the list
def addComp():
    stock = input('Type in your company\'s stock symbol:')
    ticker_list.append(stock)
    answer = input('Do you want to add more companies?: (yes/no)')
    while answer=='yes':
        stock = input('Type in your company\'s stock symbol:')
        ticker_list.append(stock)
        answer = input('Do you want to add more companies?: (yes/no)')


addComp()

    


today = date.today()
start_date="2019-10-20"

files=[]
def getData(company):
    print(company)
    data = pdr.get_data_yahoo(company, start=start_date, end=today) 
    dataname = company + '_' +str(today)
    files.append(dataname)
    SaveData(data, dataname)

def SaveData(df, data):
    df.to_csv('./data/'+data+'.csv')

for tik in ticker_list:
    getData(tik)

for i in range(0,len(ticker_list)):
    df1 = pd.read_csv('./data/'+str(files[i]) + '.csv')
    print(df1.head)


