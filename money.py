

class Money:
    def __init__(self, start_money):
        self._start_money=start_money
        self._curr_money=start_money
        self._action_cost=5
    
    
    def buy(self, price, number):
        self._curr_money=self._curr_money-(price*number)
    
    def sell(self,price, number)
        self._curr_money=self._curr_money+(price*number)
        
    
    def gains(self):
        print((self._curr_money-self._start_money)/self._curr_money)