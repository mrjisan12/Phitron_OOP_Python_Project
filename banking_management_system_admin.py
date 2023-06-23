
# BANKING MANAGEMENT SYSTEM FOR ADMIN

class Bank:
    def __init__(self):
        # Dictionary to store user accounts and their balances
        self.accounts = {}  
        # Dictionary to store transaction history
        self.transaction_history = {}  
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

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
            self.total_balance += amount
            return True
        else:
            return False

    def withdraw(self, user_name, amount):
        if user_name in self.accounts:
            if self.accounts[user_name] >= amount:
                self.accounts[user_name] -= amount
                self.transaction_history[user_name].append(f"Withdrew {amount} TAKA")
                self.total_balance -= amount
                return True
            else:
                return "Bankrupt, Not Enough Money"  # User cannot withdraw more than the available balance
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
                self.total_balance -= amount
                return True
            else:
                return "Bankrupt, Not Enough Money"  # User cannot transfer more than the available balance
        else:
            return False

    def get_transaction_history(self, user_name):
        if user_name in self.transaction_history:
            return self.transaction_history[user_name]
        else:
            return False

    def get_loan(self, user_name):
        if self.loan_feature_enabled:
            if user_name in self.accounts:
                total_amount = self.accounts[user_name]
                loan_amount = 2 * total_amount
                self.accounts[user_name] += loan_amount
                self.transaction_history[user_name].append(f"Loan received: {loan_amount} TAKA")
                self.total_balance += loan_amount
                self.total_loan_amount += loan_amount
                return True
            else:
                return False
        else:
            return "SORRY! Loan feature is currently disabled."

    def admin_check_total_balance(self):
        return self.total_balance

    def admin_check_total_loan_amount(self):
        return self.total_loan_amount

    def admin_toggle_loan_feature(self):
        self.loan_feature_enabled =  self.loan_feature_enabled
        return "Loan feature has been turned " + ("ON" if self.loan_feature_enabled else "OFF")



# Creating a bank instance
bank = Bank()

# Creating user accounts
bank.create_account("Alex")
bank.create_account("Mark")

# Depositing money
bank.deposit("Alex", 50000)
bank.deposit("Mark", 5200)

# Checking total available balance
total_balance = bank.admin_check_total_balance()
print("Total available balance:", total_balance)

# Checking total loan amount
total_loan_amount = bank.admin_check_total_loan_amount()
print("Total loan amount:", total_loan_amount)

# Turning off the loan feature
toggle_result = bank.admin_toggle_loan_feature()
print(toggle_result)

# Taking a loan
loan_result = bank.get_loan("Alex")
print(loan_result)

# Checking total available balance again
total_balance = bank.admin_check_total_balance()
print("Total available balance:", total_balance)

# Checking total loan amount again
total_loan_amount = bank.admin_check_total_loan_amount()
print("Total loan amount:", total_loan_amount)
