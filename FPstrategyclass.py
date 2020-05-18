# futures strategy class.

import pandas as pd

from general_strategyclass import *



class strategy(general_strategy):

    ''' A class for the given trading strategy properties for this case study.'''

    def __init__(self, X, Y, N, futuresA, futuresB):


        ''' Simulates the strategy with the given futuresA and futures B securities and given X, Y, N.
        Note that the ordering of the inputted futuresA and futuresB pandas DataFrames with the futures_data list matters here. '''


        # current values on a given day. 
        current_cash = 0
        number_of_futures_contracts = 0
        current_futures_value = 0           # current value of all held futures
        current_cumulative_profit = 0       # current cumulative profit/loss


        # lists of daily values of the variables defined above.
        # Initial values are repeated for first N days as no trades can occur until day N+1 of the strategy.
        self.cash = [current_cash]*N
        self.contracts = [number_of_futures_contracts]*N
        self.futures_values = [current_futures_value]*N
        self.cumulative_profits = [current_cumulative_profit]*N


        self.dates = self.get_common_dates([futuresA,futuresB])  # only need to consider dates when we have both futures A and futures B data.


        rolling_sd = futuresB.rolling(window=N).std()


        daily_change = futuresB.diff()


        for i in range(N,len(self.dates)):       # loop through the dates of the data given, updating trades and values.

            day = self.dates[i]
    
            yesterday = self.dates[i-1]
    
            z = daily_change.loc[day][0]/rolling_sd.loc[yesterday][0]      # normalised daily change of futures B values on: day = dates[i]
    
            if z < -X:
                # buy futures A
                number_of_futures_contracts+=1
                current_cash-=futuresA.loc[day][0]
        

            elif z > Y:
                # sell futures A
                number_of_futures_contracts-=1
                current_cash+=futuresA.loc[day][0]
    
            current_futures_value = number_of_futures_contracts * futuresA.loc[day][0]

            current_cumulative_profit = current_cash + current_futures_value  # cumulative pnl includes cash profit/loss and profit/loss from held futures

            self.cumulative_profits.append( current_cumulative_profit )

            self.cash.append( current_cash )

            self.initial_cash = -min(self.cash) # minimum cash required to undertake the strategy in the given time interval


            # Below is useful data for this strategy, but not required for current case study:

            self.contracts.append( number_of_futures_contracts )

            self.futures_values.append( current_futures_value )


    ######################################################################################


    

        

        

        

            
            

        

        

        

        

        

        

        

        
        
        
        
        
        
        
        
        
        
        
