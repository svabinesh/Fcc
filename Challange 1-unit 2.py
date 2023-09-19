class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount} into the account. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount. Please deposit a positive amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount} from the account. New balance: ${self.__account_balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Please withdraw a positive amount."
        else:
            return "Insufficient balance for withdrawal."

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}"

# Create an instance of BankAccount
account1 = BankAccount("12345", "John Doe", 1000)

# Test deposit and withdrawal
print(account1.display_balance())  # Display initial balance
print(account1.deposit(500))       # Deposit $500
print(account1.withdraw(200))      # Withdraw $200
print(account1.display_balance())  # Display updated balance
