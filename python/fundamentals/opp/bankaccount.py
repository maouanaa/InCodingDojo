
class bankaccount :
    
    def __init__(self, interest_rate,balance):
        self.interest_rate = interest_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance += amount
        return self
        
    def  withdraw(self, amount):
        if (self.balance -amount) >=0 :
            self.balance -= amount
       
        else :
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        return self
 

    def display_account_info(self):
       print(f"balance : {self.balance}")
       return self

    def  yield_interest(self) :
      if ( self.balance > 0):
        self.balance += (self.balance * self.interest_rate)
        return self
sofiene=bankaccount(0.1,3000)
ahmed=bankaccount(0.3,400)
sofiene.deposit(1000).deposit(400).deposit(150).withdraw(2450).yield_interest().display_account_info()
ahmed.deposit(200).deposit(560).withdraw(30).withdraw(40).withdraw(60).withdraw(38).display_account_info()
