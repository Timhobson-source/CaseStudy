# general streategy class

import pandas as pd

from math import sqrt


class general_strategy():

    ''' A class of general strategy properties. '''

    # Functions below need these varibales to be defined in a derived trading strategy class:

    # self.cash (list/iterable): daily held cash in chronological order.

    # self.cumulative profits (list/iterable): daily cumulative profit and loss of the strategy in chronological order.

    # self.initial_cash: the initial cash / the minimum required cash to implement the strategy.

    # self.dates (pandas DataFrame/Series): The dates the strategy is implemented over in datetime format with daily frequency.
    

    def get_common_dates(self,futures_data):

        ''' Gets the common dates that the members (time series datasets) of futures_data share. futures data is an list/iterable of pandas DataFrame/Series datasets
            with different datetime indices. '''

        mins, maxs = [], []

        for data in futures_data:
            index = data.index # assuming datetime format of index
            mins.append(min(index))
            maxs.append(max(index))

        start = max(mins)
        end = min(maxs)

        return futures_data[0][start:end].index


    def daily_returns(self):

        k = pd.DataFrame(self.cumulative_profits)

        k = (k-k.shift(1))/(k.shift(1) + self.initial_cash) # daily return rates.

        # Here: revenue = cash profit + futures values profit + initial cash = cumulative profit + initial cash, as define in this algorithm.
        # daily returns (rate) = daily change of revenue / previous days revenue. See relevant derived class for details.

        k.loc[self.dates[0]]=0 # setting returns rate for first day as zero

        return k
    

    def return_rate(self, as_percentage=False):

        ''' Calculates the rate of return of the strategy across the whole time interval with respect to the minimum cash required for to undertake it.

        Default return is a fraction. If as_percentage is True then return is a percentage.'''


        self.final_profit = self.cumulative_profits[-1]

        ror = self.final_profit/self.initial_cash

        if as_percentage == True:

            return 100 * ror

        else:

            return ror

        

    def Sharpe(self, risk_free_rate=0, annualised = False):

        ''' Calculates the Sharpe ratio of the strategy and returns as a float. Risk free rate is default zero. '''

        DR = self.daily_returns()

        sigma = DR.std()[0]

        mu = DR.mean()[0]

        if annualised == True:

            return sqrt(252) * (mu - risk_free_rate)/sigma  # 252 trading days in the year. 

        else:

            return (mu - risk_free_rate)/sigma



    def annualised_return(self, as_percentage = False):

        ''' Calculates the annulaised return, and returns it as a float '''

        ann_ror = self.return_rate()

        assert ann_ror >= -1, 'annualized return not defined for rate of returns < -100%.'

        ann_ror = (1+ann_ror)**(365/len(self.daily_returns())) - 1

        if as_percentage == True:

            return 100 * ann_ror

        else:

            return ann_ror

    
