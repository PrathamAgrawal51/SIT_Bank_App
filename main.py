from Banking.account import SavingsAccount, CurrentAccount
from Banking.transactions import deposit, withdraw

accounts = {}

def create_account():
    acc_type = input("Enter account type (savings/current): ").strip().lower()
    name = input("Enter account holder's name: ").strip()
    initial_deposit = float(input("Enter initial balance: "))
    if acc_type == 'savings':
        acc = SavingsAccount(name, initial_deposit)
    elif acc_type == 'current':
        acc = CurrentAccount(name, initial_deposit)
    else:
        print("Invalid account type. Please choose 'savings' or 'current'.")
        return None
    accounts[acc.account_number] = acc
    print(f"Account created successfully. Account number: {acc.account_number}")

def login():
    acc_number = int(input("Enter your account number: "))
    if acc_number in accounts:
        user_acc = accounts[acc_number]
        print(f"Welcome {user_acc.name}!")

        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
            if isinstance(user_acc, SavingsAccount):
                print("\n5. Calculate Interest")
            choice = input("\nChoose an option: ")
            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                deposit(user_acc, amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                withdraw(user_acc, amount)
            elif choice == '3':
                user_acc.display_balance()
            elif choice == '4':
                print("Exiting...")
                break
            elif choice == '5' and isinstance(user_acc, SavingsAccount):
                user_acc.calculate_interest()
            else:
                print("Invalid option. Please try again.")
    else:
        print("Account not found. Please check your account number.")

def main():
    while True:
        print("\nWelcome to the SIT Banking System")
        print("1. Create Account\n2. Login\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()