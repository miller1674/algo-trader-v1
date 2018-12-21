
import datetime 
from datetime import timedelta

from stock import *


array=["SHW", "MU", "TSLA", "JPM", "BIIB", "UFPI", "EOG", "WMT", "SBUX", "NKE","AMD", "BAC", "MSFT"]
porfolio=[]


class Control:
    def __init__(self):
        self._portfolio=[]
        self._stock_list=[]
    
    def launch(self):
        
        currDay=datetime.date(2017, 3, 6)
        stock_list=[]
        while (currDay!=datetime.date(2017, 4, 24)):
            
            
            print(currDay)
            #if (currDay.weekday()==0):
            #stock_list=[]
            for f in range(0, len(array)):
                p=Stock(array[f], currDay)
                p.movingAvg(30, currDay)
                #p.printStock()
                stock_list.append(p)  
            self._stock_list=stock_list   
            #print(" ")
            self.portfolio()
            self._portfolio[0].printStock()
            self._portfolio[1].printStock()
            self._portfolio[2].printStock()
            stock_list.clear()
            currDay=currDay+timedelta(7) #moves to next week
            
                 
        
    def portfolio(self):
        stock=[]
        stock.append(self._stock_list[0])
        stock.append(self._stock_list[0])
        stock.append(self._stock_list[0])
        port=[]
        for i in range(0, (len(self._stock_list))):
            if (stock[0]._moving_avg<self._stock_list[i]._moving_avg):
                stock[0]=self._stock_list[i]
               
        for z in range(0, (len(self._stock_list))):
            if (stock[1]._moving_avg<self._stock_list[z]._moving_avg and self._stock_list[z]!=stock[0]):
                stock[1]=self._stock_list[z]
        
        for y in range(0, (len(self._stock_list))):
            if (stock[2]._moving_avg<self._stock_list[y]._moving_avg and self._stock_list[y]!=stock[0] and self._stock_list[y]!=stock[1]):
                stock[2]=self._stock_list[y]
        
        if (len(self._portfolio)!=0):
            
            #curr_in=False
            for t in range(0,3):
                curr_in=False
                for r in range(0, 3):
                    if (stock[t]._symbol==self._portfolio[r]._symbol):
                        port.append(self._portfolio[r])
                        curr_in=True
                    
                if (curr_in==False):
                    port.append(stock[t])
                
        else:
            port.append(stock[0])
            port.append(stock[1])
            port.append(stock[2])      
        
        
        self._portfolio=port
        
        
       
        
        
        
        

f=Control()
f.launch()

