from datetime import datetime

class Transaction:
    def __init__(self, narration, amount, transaction_type):
        self.date_time = datetime.now()
        self.narration = narration
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.date_time} | {self.transaction_type} | {self.narration} | {self.amount}"

class Account:
    def __init__(self, recipient, account_number):
        self.recipient = recipient
        self.__balance = 0
        self.__account_number = account_number
        self.transactions = []
        self.is_frozen = False
        self.minimum_balance = 0
        self.loan_balance = 0

    def check_if_frozen(self):
        return self.is_frozen

    def deposit(self, amount):
        if self.is_frozen:
            return "Account is frozen. Cannot deposit."
        if amount <= 0:
            return "Deposit amount must be positive."
        self.__balance += amount
        self.transactions.append(Transaction("You have received", amount, "Deposit"))
        return f"You have received {amount}. Your new balance is {self.get_balance()}"

    def withdraw(self, amount):
        if self.is_frozen:
            return "Your account is frozen. Withdrawal not possible."
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if self.get_balance() - amount < self.minimum_balance:
            return "Insufficient funds."
        self.__balance -= amount
        self.transactions.append(Transaction("Withdrawal", -amount, "Withdrawal"))
        return f"Withdrawal of {amount} successful. New balance is {self.get_balance()}"

    def transfer_funds(self, amount, target_account):
        if self.is_frozen:
            return "Account is frozen. You cannot transfer funds."
        if amount <= 0:
            return "Transfer amount must be positive."
        if self.get_balance() - amount < self.minimum_balance:
            return "Insufficient funds or minimum balance requirement not met."

        self.__balance -= amount
        self.transactions.append(Transaction(f"Transfer to {target_account.__account_number}", -amount, "Withdrawal"))
        target_account.__balance += amount
        target_account.transactions.append(Transaction(f"Transfer from {self.__account_number}", amount, "Deposit"))
        return f"Transfer successful. Your new balance is {self.get_balance()}"

    def get_balance(self):
        return self.__balance

    def request_loan(self, amount):
        if self.is_frozen:
            return "Account is frozen. Cannot request loan."
        if amount <= 0:
            return "Loan amount must be positive."
        self.loan_balance += amount
        self.__balance += amount  
        self.transactions.append(Transaction("Loan granted", amount, "CREDIT"))
        return f"Loan of {amount} has been granted to your account. Your new balance is {self.get_balance()}"

    def repay_loan(self, amount):
        if amount <= 0:
            return "Repayment amount must be positive."
        if self.loan_balance == 0:
            return "No outstanding loan to repay."
        repaying_amount = min(amount, self.loan_balance)
        if self.get_balance() - repaying_amount < self.minimum_balance:
            return "Insufficient funds to repay your loan."
        self.loan_balance -= repaying_amount
        self.__balance -= repaying_amount  
        self.transactions.append(Transaction("Loan repayment", -repaying_amount, "Deposit"))
        return f"Loan repayment of {repaying_amount} successful. Remaining loan: {self.loan_balance}"

    def view_account_details(self):
        return f"Owner: {self.recipient}, your Account Number is {self.__account_number}, your current balance is {self.get_balance()} and your loan is {self.loan_balance}"

    def change_account_owner(self, new_recipient):
        self.recipient = new_recipient
        return f"Account owner changed to {new_recipient}."

    def account_statement(self):
        print("Date/Time | Type | Narration | Amount")
        for transaction in self.transactions:
            print(transaction)

    def calculate_interest(self):
        if self.is_frozen:
            return "Your account is frozen. You cannot receive any interest."
        balance = self.get_balance()
        if balance > 0:
            interest = balance * 0.05
            self.__balance += interest
            self.transactions.append(Transaction("Interest applied", interest, "Deposit"))
            return f"Interest of {interest} has been applied. Your new balance is {self.get_balance()}"

    def freeze_account(self):
        self.is_frozen = True
        return "Your account has been frozen."

    def unfreeze_account(self):
        self.is_frozen = False
        return "Your account has been successfully unfrozen."

    def set_minimum_balance(self, minimum_balance):
        if minimum_balance < 0:
            return "Minimum balance must not be negative."
        self.minimum_balance = minimum_balance
        return f"Minimum balance is set to {minimum_balance}."

    def close_account(self):
        self.transactions.clear()
        self.loan_balance = 0
        self.__balance = 0  
        return "Account closed. Balance set to zero and all transactions cleared."

