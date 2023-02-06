from bankaccount import bankaccount
class Usebankaccount(bankaccount) :
    def __init__(self, name, email):
         super().__init__(interest_rate=0.02, balance=0)
         self.name = name
         self.email = email
         self.account = bankaccount(interest_rate=0.02, balance=0)
    def make_deposit(self,amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self
    def make_withdraw(self,amount):
        self.account.withdraw(amount)
        print(self.account.balance)
        return self
    def display(self):
        self.account.display_account_info()
       
ahmed=Usebankaccount("ahmed","ahmed@gmail.com")
ahmed.make_deposit(100).make_withdraw(10).display()
