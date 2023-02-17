class BankAccount:
    def __init__(self, int_rate,balance): 
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount 
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

bank_account1 = BankAccount(.07 , 100)
bank_account2 = BankAccount(0.9, 90000)

bank_account1.deposit(20).deposit(20).deposit(20).withdraw(50).yield_interest().display_account_info()

bank_account2.deposit(300).deposit(300).withdraw(1000).withdraw(1000).withdraw(1000).withdraw(1000).yield_interest().display_account_info()






        


