
import datetime 
from datetime import timedelta

from stock import *


array=["SHW", "MU", "TSLA", "JPM", "BIIB", "UFPI", "EOG", "WMT", "SBUX", "NKE","AMD", "BAC", "MSFT"]


class Control:
    def launch(self):
        
        currDay=datetime.date(2017, 3, 6)
        currDay=currDay+timedelta(1)   #moves to next date 
        stockList=[]
        
        
        for f in range(0, len(array)):
            p=Stock(array[f], currDay)
            p.movingAvg(30, currDay)
            p.printStock()
            stockList.append(p)
            
        
        
        
        
        print(currDay)
        
        
        
        #stockList[0].printStock()

f=Control()
f.launch()

