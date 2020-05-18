# PrismFP case study: execution file TIMOTHY HOBSON

import pandas as pd

import matplotlib.pyplot as plt

from FPstrategyclass import *




# Importing relevant data (from files saved on PC):

futuresA = pd.read_csv('insert futuresA.csv file path')  

futuresB = pd.read_csv('insert futuresB.csv file path') 

#################################### FORMATTING DATA #######################################################

# All modules used here for analysis of futures timeseries assume that the data is formatted as a pandas dataframe/series with a (daily) DateTime index.
# This is the form the data shall be formatted to below.

# reordering dataframes:
futuresA = futuresA.iloc[::-1] 
futuresB = futuresB.iloc[::-1] 

# creating datetime index
yA = pd.to_datetime(futuresA['Date'], format = '%d/%m/%Y') 
yB = pd.to_datetime(futuresB['Date'], format = '%d/%m/%Y') 

# setting datetime indices
futuresA = futuresA.set_index(yA, drop = True)
futuresA.drop('Date', axis=1, inplace = True) 

futuresB = futuresB.set_index(yB, drop = True)
futuresB.drop('Date',axis=1, inplace = True) 

# setting frequency of data to 'daily'
futuresA = futuresA.asfreq('d')
futuresB = futuresB.asfreq('d') 

# interpolating missing data
futuresA.interpolate(method='time', inplace = True)
futuresB.interpolate(method='time', inplace = True) 



################################ STRATEGY ANALYSIS #################################################

# user-defined values:
X = 2.5
Y = 2.5
N = 15

our_strategy = strategy(X,Y,N,futuresA,futuresB) # creating an instance of the strategy class (see FPstrategyclass.py for details)

dates = futuresB.index

# plotting profit and loss

plt.plot(dates, our_strategy.cumulative_profits)

plt.title('X = '+str(X)+', Y = '+str(Y)+', N = '+str(N))

plt.axhline(0,ls='--',c='black')

plt.legend(['cumulative profit and loss'])

plt.show()



# annualised return and sharpe ratio:
print('Annualised return: ', our_strategy.annualised_return(as_percentage=True),'%')
print('Annualised Sharpe ratio: ', our_strategy.Sharpe(annualised = True))






