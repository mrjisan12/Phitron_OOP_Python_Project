
# BANKING MANAGEMENT SYSTEM FOR USER

class Bank:
    def __init__(self):
         # Dictionary to store user accounts and their balances
        self.accounts = {} 
        # Dictionary to store transaction history
        self.transaction_history = {}  

    def create_account(self, user_name):
        if user_name not in self.accounts:
            self.accounts[user_name] = 0
            self.transaction_history[user_name] = []
            return True
        else:
            return False

    def deposit(self, user_name, amount):
        if user_name in self.accounts:
            self.accounts[user_name] += amount
            self.transaction_history[user_name].append(f"Deposited {amount} TAKA")
            return True
        else:
            return False

    def withdraw(self, user_name, amount):
        if user_name in self.accounts:
            if self.accounts[user_name] >= amount:
                self.accounts[user_name] -= amount
                self.transaction_history[user_name].append(f"Withdrew {amount} TAKA")
                return True
            else:
                # User cannot withdraw more than the available balance
                return "Bankrupt"  
        else:
            return False

    def check_balance(self, user_name):
        if user_name in self.accounts:
            return self.accounts[user_name]
        else:
            return False

    def transfer(self, sender_name, receiver_name, amount):
        if sender_name in self.accounts and receiver_name in self.accounts:
            if self.accounts[sender_name] >= amount:
                self.accounts[sender_name] -= amount
                self.accounts[receiver_name] += amount
                self.transaction_history[sender_name].append(f"Transferred {amount} TAKA to {receiver_name}")
                self.transaction_history[receiver_name].append(f"Received {amount} TAKA from {sender_name}")
                return True
            else:
                # User cannot transfer more than the available balance
                return "Bankrupt"  
        else:
            return False

    def get_transaction_history(self, user_name):
        if user_name in self.transaction_history:
            return self.transaction_history[user_name]
        else:
            return False

    def get_loan(self, user_name):
        if user_name in self.accounts:
            total_amount = self.accounts[user_name]
            loan_amount = 2 * total_amount
            self.accounts[user_name] += loan_amount
            self.transaction_history[user_name].append(f"Loan received: {loan_amount} TAKA")
            return True
        else:
            return False
        

# Creating a bank instance

bank = Bank()

# Creating user accounts
bank.create_account("Alex")
bank.create_account("Mark")

# Depositing money
bank.deposit("Alex", 10000)
bank.deposit("Mark", 5000)

# Withdrawing money
result = bank.withdraw("Alex", 2000)
if result == "Bankrupt":
    print("Sorry, the bank is bankrupt.")
elif result:
    print("Withdrawal successful.")
else:
    print("User does not exist.")

# Checking account balance
balance = bank.check_balance("Alex")
if balance:
    print("Alex's Acount balance:", balance)
else:
    print("User does not exist.")

# Transferring money
result = bank.transfer("Alex", "Mark", 1500)
if result == "Bankrupt":
    print("Sorry, the bank is bankrupt.")
elif result:
    print("Congratulation Transfer successful.")
else:
    print("One or both users do not exist.")

# Checking transaction history
history = bank.get_transaction_history("Alex")
if history:
    print("Alex's Bank Acount Transaction history:")
    for transaction in history:
        print(transaction)
else:
    print("User does not exist.")

# Taking a loan
result = bank.get_loan("Alex")
if result:
    print("Alex Your Loan received.")
else:
    print("User does not exist.")

