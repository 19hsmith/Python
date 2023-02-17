class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self   

    def user_balance(self):
        self.account.display_account_info(self.name)
        return self



class BankAccount:
    def __init__(self, int_rate = 5,balance = 50000): 
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount 
        return self
    def display_account_info(self,name):
        print(f"{name} Balance: ${self.balance}")
        return self
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self


carson = User("carson","verygoodatpokemon23@gmail.com")
brandon = User("brandon","snowboarder45@gmail.com")

carson.make_deposit(500).make_withdrawal(250).user_balance()
brandon.make_deposit(100).make_deposit(40000).make_withdrawal(90).user_balance()