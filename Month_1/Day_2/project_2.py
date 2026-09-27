#mental diagram of prjocet
#class must have 2 attributes, 1: owner (which is name) 2: balance(which is amount) 
#so we are solving a question, whose bank is this an dhow much do they have in account.



#so three method inside the class.
# balance is stored in the BankAccount object as self.balance
# every method can read or update the same balance

#methods:
#   deposit amount: add in 500
# withdraw amount : subtract from deposit amount 
# get balance: showing after withdraw amount






class BankAccount:
    def __init__(self,owner,balance):
        self.owner  = owner 
        self.balance = balance 
        
    
    
    def deposit_amount(self):
        
        amount = int(input(f"Enter the amount you like to deposite:"))
        self.balance = self.balance + amount
        print(f"--> Balance becomes ${self.balance}")
        return self.balance
    
    def withdraw_account(self):
        
        amount = int(input(f"Enter the amount you like to withdraw:"))
        self.balance = self.balance - amount
        print(f"--> Balance becomes: ${self.balance}")
        return self.balance
    
    def get_balance(self):
        print(f"Your final balance is --> ${self.balance}")
        return self.balance


def main():
    account = BankAccount("Aayush",500)
    account.deposit_amount()
    account.withdraw_account()       
    account.get_balance()
    
    
if __name__ == "__main__":
    main()
        
        