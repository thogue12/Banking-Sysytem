

class Account():
    def __init__ (self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print("sorry, inccorect pasword")
            return None

        if amountToDeposit < 0:
            print("You can not deposit a negative number")
            return None

        self.balance = self.balance + amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print("sorry, inccorect pasword")
            return None

        if amountToWithdraw < 0:
            print("You can not negative a negative number")
            return None

        if amountToWithdraw > self.balance:
            print("You can not withdraw more than you have")
            return None

        self.balance = self.balance - amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print("sorry, inccorect pasword")
            return None
        return self.balance

a1 = Account("Tim",7896, "TimBoslice")
a2 = Account("Dime", 90, "No Time")    

a2.withdraw(89, "No Time")
a2.deposit(2540, "No Time")
print(a2.getBalance("No Time"))




print(a1.deposit(1000, "TimBoslice"))
print(a1.withdraw(450, "TimBoslice"))

