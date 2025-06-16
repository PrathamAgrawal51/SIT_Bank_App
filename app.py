import streamlit as st

# --- Account Classes ---

class Account:
    _acc_counter = 1000

    def __init__(self, name, initial_deposit, acc_type):
        self.name = name
        self.balance = float(initial_deposit)
        self.acc_type = acc_type
        self.account_number = Account._acc_counter
        Account._acc_counter += 1

    def deposit(self, amount):
        self.balance += float(amount)

    def withdraw(self, amount):
        if float(amount) > self.balance:
            return False
        self.balance -= float(amount)
        return True

# --- Session State Setup ---

if 'accounts' not in st.session_state:
    st.session_state['accounts'] = {}

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'current_acc' not in st.session_state:
    st.session_state['current_acc'] = None

# --- Account Creation ---

def create_account():
    st.header("Create Account")
    name = st.text_input("Account Holder Name")
    acc_type = st.selectbox("Account Type", ["Savings", "Current"])
    initial_deposit = st.number_input("Initial Deposit", min_value=0.0, value=0.0, step=1.0)
    if st.button("Create Account"):
        if not name:
            st.error("Please enter a name.")
            return
        acc = Account(name, initial_deposit, acc_type)
        st.session_state['accounts'][acc.account_number] = acc
        st.success(f"Account created! Your account number is: {acc.account_number}")

# --- Login & Banking Operations ---

def login():
    st.header("Login")
    acc_number = st.number_input("Account Number", min_value=1000, step=1)
    if st.button("Login"):
        acc_number = int(acc_number)
        accounts = st.session_state['accounts']
        if acc_number in accounts:
            st.session_state['logged_in'] = True
            st.session_state['current_acc'] = acc_number
            st.success(f"Welcome, {accounts[acc_number].name}!")
        else:
            st.error("Account not found.")

def banking_dashboard():
    acc_number = st.session_state['current_acc']
    acc = st.session_state['accounts'][acc_number]
    st.header(f"Welcome, {acc.name} ({acc.acc_type})")
    st.info(f"Account Number: {acc.account_number}")
    st.info(f"Current Balance: ${acc.balance:.2f}")

    action = st.selectbox("Choose Action", ["Deposit", "Withdraw", "Logout"])
    if action == "Deposit":
        amount = st.number_input("Deposit Amount", min_value=0.0, step=1.0, key="deposit")
        if st.button("Deposit"):
            acc.deposit(amount)
            st.session_state['accounts'][acc_number] = acc  # Update state
            st.success(f"Deposited ${amount:.2f}. New Balance: ${acc.balance:.2f}")
    elif action == "Withdraw":
        amount = st.number_input("Withdraw Amount", min_value=0.0, step=1.0, key="withdraw")
        if st.button("Withdraw"):
            if acc.withdraw(amount):
                st.session_state['accounts'][acc_number] = acc  # Update state
                st.success(f"Withdrew ${amount:.2f}. New Balance: ${acc.balance:.2f}")
            else:
                st.error("Insufficient funds.")
    elif action == "Logout":
        st.session_state['logged_in'] = False
        st.session_state['current_acc'] = None
        st.success("Logged out.")

# --- Main App ---

def main():
    st.title("Simple Bank App")
    st.write("Create an account, login, deposit, withdraw, and check your balance. Created by Pratham Agrawal")

    if not st.session_state['logged_in']:
        menu = st.radio("Menu", ["Create Account", "Login"])
        if menu == "Create Account":
            create_account()
        elif menu == "Login":
            login()
    else:
        banking_dashboard()

if __name__ == "__main__":
    main()