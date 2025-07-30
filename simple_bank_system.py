# Define a class called 'bank' that models a simple bank account
class bank:
    # Constructor method to initialize a bank account
    def __init__(self, name, accType, amount):
        self.name = name           # Account holder's name
        self.accType = accType     # Type of account (e.g., Savings, Current)
        self.amount = amount       # Initial amount passed (not used directly in logic)
        self.balance = 0           # Initialize account balance to 0

    # Method to display account holder's information and current balance
    def display_info(self):
        print(f"Name of Account Holder: {self.name} Account Type: {self.accType} balance: {self.balance}")

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Add deposit amount to current balance
            print(f"{amount}$ is Deposited. Your New Account Balace is {self.balance}")
        else:
            print("Invalid Deposit Amount...")  # Print error if amount is not positive

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")  # Error if trying to withdraw more than available
        elif amount <= 0:
            print("Invalid Withdrawal amount")  # Error if amount is zero or negative
        else:
            self.balance -= amount  # Subtract amount from balance
            print(f"{amount} has been withdrawn....    Your Remaining Account Balance is {self.balance} ")

    # Method to check the current balance
    def check_balance(self):
        print(f" Dear {self.name} your current bank balance is: {self.balance}. Account Type:{self.accType}")
