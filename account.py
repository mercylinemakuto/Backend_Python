class Account:
    def __init__(self, name, account_number):
        self.name = name
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.account_number = account_number
        self.loan = 0
        self.minimum_balance = 0

# Deposit: method to deposit funds, store the deposit and return a message with the new balance to the customer. It should only accept positive amounts.
    def deposit(self, amount):
        if amount > 0:
            self.deposits.append(amount)
            self.balance =+ sum(self.deposits)
            return f"Confirmed, you have received {amount} , new balance is {self.balance}"
        else:
            return "Deposit amount must be positive"
            
 #Withdraw: method to withdraw funds, store the withdrawal and return a message with the new balance to the customer. An account cannot be overdrawn. 
    def withdraw(self, amount):
        if amount <= sum(self.deposits):
            self.withdrawals.append(amount)

            new_balance = sum(self.deposits) - sum(self.withdrawals)
            return f"Your transaction of Ksh {amount} to agent has been successful. New balance: Ksh {new_balance}"
        else:
            return "Insufficient amount"
       

    def get_balance(self):
        return sum(self.deposits) - sum(self.withdrawals) 

# Transfer Funds: Method to transfer funds from one account to an instance of another account.
    def transfer_funds(self,recipient,amount):
        if amount <= self.balance:
             self.withdraw(amount)
             recipient.deposit(amount)
             return f"Transfer {amount} to this {recipient.account_number} account"
        else:
            return "Not enough funds"

# Request Loan: Method to request a loan amount.
    def request_loan(self, amount):
        if amount >= 0:
            self.loan += amount
            self.deposits.append(amount)
            return f"Loan of {amount} was successful.Your new balance is {self.get_balance()}"
        else:
            return "You are not elligible for a loan"

# Repay Loan: Method to repay a loan with a given amount.
    def repay_loan(self,amount):
        if amount > 0:
            self.loan -= amount
            self.balance -= amount
            return f"You've repaid  {amount}, your remaining debt is {self.loan}"

# View Account Details: Method to display the account owner's details and current balance.
    def view_account_details(self): 
        return f"Hello {self.name} , your balance is {self.get_balance()} and your loan is {self.loan}"

# Change Account Owner: Method to update the account owner's name.
    def change_account_owner(self, new_owner):
        self.name = new_owner
        return f"The account ownership has changed to {self.name}"

# Account Statement: Method to generate a statement of all transactions in an account. (Print using a for loop).
    def account_statement(self):
        print("All transactions")
        for i in self.deposits:
            print(f" Deposit :{i}")
        for i in self.withdrawals:
            print(f"Withdrawal:{i}")

# Interest Calculation: Method to calculate and apply an interest to the balance. Use 5% interest.
    def interest_calculation(self):
        interest = self.get_balance() * 0.05
        self.balance += interest
        return f"interest of {interest} has been applied."

# Freeze/Unfreeze Account: Methods to freeze and unfreeze the account for security reasons.
    def freeze_account(self):
        self.frozen = True
        return f"Unfortunately, your account is frozen"

    def unfreeze_account(self):
        self.frozen = False
        return f"Your account has been successfully unfrozen"

# Set Minimum Balance: Method to enforce a minimum balance requirement. You cannot withdraw if your balance is less than this amount
    def min_balance(self, amount):
         if amount >= 0:
             self.minimum_balance = amount
             return f"Minimum balance is {amount}"

            
# Close Account: Method to close the account and set all balances to zero and empty all transactions.
    def close_account(self):
        self.balance = 0
        self.deposits.clear()
        self.transaction.clear()
        self.withdrawals.clear()
        self.loan = 0
        self.minimum_balance = 0
        return "All balances have been set to zero and all accountss are closed"

       


