class BankAccount:
    """A class representing a bank account."""
    account_counter = 1000
    
    def __init__(self, name, balance=0):
        self.account_number = BankAccount.account_counter
        BankAccount.account_counter += 1
        self.name = name
        self.__balance = balance

    def get_balance(self):
        """Returns the current balance of the account."""
        return self.__balance
    
    def deposit(self, amount):
        """Deposits a specified amount into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f} into account {self.account_number}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """Withdraws a specified amount from the account if sufficient funds are available."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_number}.")
        else:
            if amount <= 0:
                print("Withdrawal amount must be positive.")
            else:
                print("Insufficient funds for withdrawal.")
    
    def display_balance(self):
        """Displays the current balance of the account."""
        print(f"Account Number: {self.account_number}, Name: {self.name}, Balance: ${self.__balance:.2f}")

class SavingsAccount(BankAccount):
    """A class representing a savings account with interest."""
    
    def __init__(self, name, balance=0, interest_rate=0.05):
        super().__init__(name, balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        """Applies interest to the current balance."""
        months = int(input("Enter the number of months to apply interest: "))
        interest = self.get_balance() * self.interest_rate * months
        self.deposit(interest)
        print(f"Applied interest of ${interest:.2f} to account {self.account_number} and new balance is {self.get_balance()}.")

class CurrentAccount(BankAccount):
    """A class representing a current account with overdraft."""
    
    def __init__(self, name, balance=0, overdraft_limit=100000):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        """Withdraws a specified amount from the account considering overdraft limit."""
        if 0 < amount <= (self.get_balance() + self.overdraft_limit):
            self._BankAccount__balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_number}.")
        else:
            if amount <= 0:
                print("Withdrawal amount must be positive.")
            else:
                print("Insufficient funds for withdrawal including overdraft limit.")