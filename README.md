# CaseStudy

The files in this repository are as follows:

- FPexecution.py is the execution file for the case study, it plots the cumulative profit & loss of the given strategy and then the annualised return & Sharpe ratio.

- general_strategyclass.py is a file defining a class, "general_strategy", of all general trading strategy properties. This includes functions for analysis, such as the Sharpe ratio of the strategy. Some functions in this class rely on instance variables being defined by a derived class, e.g. the "cumulative_profits" list in "return_rate()".

- FPstrategy.py is a file defining the class "strategy", a derived class of the "general_strategy" class (see above). An instance of this class carries out the given case study trading strategy with given futures data and variables X, Y, N. 

- futuresA.csv, futuresB.csv are the case study futures data

The idea of this code is that not only does it carry out the trading strategy for any generic timeseries data (it must satisfy formatting conditions as defined in FPexecution.py), but also you can create another derived class of general_strategy for a new strategy which which you want to implement on given data. You can then use the analytical tools in the general_strategy class to do the same (or different!) analysis of the strategy as before, given that the derived class defines the necessary instance variables required in the general_strategy class.
