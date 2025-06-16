# 💰💵 SIT Bank App
Created by Pratham Agrawal as a part of Edunet Training

[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-orange?logo=streamlit)](https://streamlit.io)

🔗 *Live App*: [Click here to use Sit Bank](https://sitbankapp-pratham.streamlit.app/)

| Interface           | Screenshot |
|---------------------|------------|
| 🏠 Home Page         | ![Home Page](https://github.com/PrathamAgrawal51/SIT_Bank_App/blob/56503a1b730c3846ff23fe977dbe2a01efee5206/home_page.png) |


## Project Overview
The SIT Bank project is a simple banking application that allows users to create bank accounts, deposit and withdraw funds, check balances, and calculate interest for savings accounts. The application is structured into a modular format, making it easy to maintain and extend.

## Project Structure
```
SIT Bank
├── Banking
│   ├── __init__.py
│   ├── account.py
│   └── transactions.py
├── main.py
├── app.py
└── README.md
```

### File Descriptions
- **Banking/__init__.py**: This file is the initialization file for the Banking module. It does not contain any code.
  
- **Banking/account.py**: This file defines the `BankAccount` class, which represents a bank account. It includes methods for getting the balance, depositing, withdrawing, and displaying the balance. It also defines two subclasses: `SavingsAccount`, which adds interest calculation, and `CurrentAccount`, which includes overdraft functionality.

- **Banking/transactions.py**: This file contains two functions, `deposit` and `withdraw`, which handle depositing and withdrawing amounts from a bank account.

- **main.py**: This file serves as the main entry point for the banking application. It allows users to create accounts, log in, deposit, withdraw, check balances, and calculate interest for savings accounts.

- **app.py**: This file serves as the Streamlit application for deploying the banking project. It provides a user interface for interacting with the banking functionalities.

## Getting Started
To run the application, ensure you have Python installed along with the required libraries. You can install Streamlit using pip:

```
pip install streamlit
```

### Running the Application
To start the Streamlit application, navigate to the project directory and run the following command:

```
streamlit run app.py
```

This will launch the application in your web browser, allowing you to interact with the banking functionalities.
