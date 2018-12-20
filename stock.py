import quandl
import matplotlib.pyplot as plt
import pandas as pd
quandl.ApiConfig.api_key = "bAqiaN9tTgprMomJXhzu"



class Stock:
    def __init__(self, symbol, currentDay):
        
        self._symbol = symbol
        temp=quandl.get("WIKI/"+(str(symbol)), end_date=currentDay, rows=1)
        self._currPrice=temp.Close[0]
		
		
		
    def printStock(self):
        print("This is the symbol "+self._symbol+" Curr Price:"+ str(self._currPrice)+" Moving Avg:"+ str(self._movingAvg))
	
    def movingAvg(self, numDays, currentDay):
        temp=quandl.get("WIKI/"+self._symbol, end_date=currentDay ,rows=numDays)
        sum=0
        for y in range(0, numDays):
            sum+=temp.Close[y]
        move=sum/numDays
        self._movingAvg=move
	
		



