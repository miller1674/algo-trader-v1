

class Money:
    def __init__(self, start_money):
        self._start_money=start_money
        self._curr_money=start_money
        self._action_cost=5
    
    
    def buy(self, price, number):
        self._curr_money=self._curr_money-(price*number)
    
    def sell(self,price, number):
        self._curr_money=self._curr_money+(price*number)
        
    
    def gains(self, portfolio):
        total=self._curr_money+(portfolio[0]._currPrice*portfolio[0]._number_owned)+(portfolio[1]._currPrice*portfolio[1]._number_owned)+(portfolio[2]._currPrice*portfolio[2]._number_owned)
        print("Percent Gain: "+(str(((total-self._start_money)/total)*100)))