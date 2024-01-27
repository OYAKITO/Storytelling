
"""
BANK DEPOSIT AND WITHDRAWAL PROGRAM

This Python program will simulate an online banking application. A user will create an account with your fictitious bank. The account will include a savings account and a checking account. Users will then be able to make deposits or withdrawals from either account as long as the remaining balance is non negative.
"""

def get_info():
    """Get user information to store in a dict that represents a bank account"""
    print("Welcome to the Python First National Bank.")

    # Get user input
    name = input("\nHello, what is your name: ").title().strip()
    savings = int(input("How much money would you like to set up your savings account with: "))
    checking = int(input("How much money would you like to set up your checking account with: "))

    # Build a dict that represents a specific bank account
    return {"Name": name, "Savings": savings, "Checking": checking}

def make_transaction(bank_account, account, money, transaction_type):
    """Perform a deposit or withdrawal based on the transaction type."""
    if account in bank_account and transaction_type in {"Deposit", "Withdrawal"}:
        if transaction_type == "Deposit":
            bank_account[account] += money
            print(f"\nDeposited ₱{money} into {bank_account['Name']}'s {account.lower()} account.")
        elif transaction_type == "Withdrawal" and bank_account[account] - money >= 0:
            bank_account[account] -= money
            print(f"\nWithdrew ₱{money} from {bank_account['Name']}'s {account.lower()} account.")
        else:
            print(f"\nSorry, by withdrawing ₱{money} you will have a negative balance.")
    else:
        print("\nI'm sorry, we cannot do that for you today.")

def display_info(bank_account):
    """Display all key-value pairs in a given bank account"""
    print("\nCurrent Account Information")
    for key, value in bank_account.items():
        if key == 'Name':
            print(f"{key}: {value}")
        else:
            print(f"{key}: ₱{value}")

# Create a bank account
my_account = get_info()

running = True
while running:
    # Show the current state of the bank account
    display_info(my_account)

    # Get user input for the transaction information
    account_type = input("\nWhat account would you like to access (Savings or Checking): ").title()
    transaction_type = input("What type of transaction would you like to make (Deposit or Withdrawal): ").title()
    amount = float(input("How much money? "))

    # Make the correct function call based on previous user input
    make_transaction(my_account, account_type, amount, transaction_type)

    # Allow users to make another transaction
    choice = input("Would you like to make another transaction (y/n): ").lower()
    if choice != 'y':
        display_info(my_account)
        print("\nThank you. Have a great day!")
        running = False
