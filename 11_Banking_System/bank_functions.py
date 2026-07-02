import data
from datetime import datetime
from storage import save_data
line = "=" * 40

def validate_name(prompt):
    while True:
        name = input(prompt).strip().capitalize()
        if name == "":
            print("Username cannot be empty.")
        else:
            break

    return name

def validate_pin(prompt):
    while True:
        pin = input(prompt)

        if not pin.isdigit():
            print("Invalid... Enter numbers only.")
        elif len(pin) != 4:
            print("Invalid... PIN must contain exactly 4 digits.")
        else:
            break

    return pin
    
def validate_initial_deposit():
    while True:
        try:
            initial=int(input("Enter initial Deposit: ₹"))
            if initial<500:
                print("Minimum opening balance is ₹500.")
            else:
                return initial
        except ValueError:
            print("Invalid.....Enter a number ")
            continue
    

def generate_account_number():
    if not data.accounts:
        return "AC1001"
    highest = max(
        int(acc_no[2:])
        for acc_no in data.accounts.keys()
    )

    return f"AC{highest + 1}"

def generate_transaction_id():
    transaction_id = f"TXN{data.transaction_counter:06d}"
    data.transaction_counter += 1
    return transaction_id


def record_transaction(acc_no, transaction_type, reason, amount, balance_after):
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    transaction = {
        "transaction_id": generate_transaction_id(),
        "type": transaction_type,
        "reason": reason,
        "amount": amount,
        "balance_after": balance_after,
        "time": current_time
    }
    data.accounts[acc_no]["history"].append(transaction)
    
def create_account():
    name = validate_name("Enter the Username: ")
    pin = validate_pin("Enter the 4-digit PIN: ")
    balance = validate_initial_deposit()
    account_number = generate_account_number()
    created_on = datetime.now().strftime("%d-%m-%Y")

    data.accounts[account_number] = {
        "name": name,
        "pin": pin,
        "balance": balance,
        "created_on": created_on,
        "attempts": 0,
        "last_login": None,
        "is_locked": False,
        "history": []
    }

    record_transaction(
        account_number,
        "Credit",
        "Initial Deposit",
        balance,
        balance
    )
    save_data()
    print(line)
    print("Account Created Successfully!".center(40))
    print(line)
    print(f"Account Number : {account_number}")
    print(f"Account Holder : {name}")
    print(f"Opening Balance: ₹{balance}")
    print("\nPlease save your Account Number.")
    

def login():
    while True:
        acc_no=input("Enter the Account number: ").strip().upper()
        if acc_no in data.accounts:
            break
        else:
            print("Account not found. Please enter a valid account number.")
            continue
    
    if data.accounts[acc_no]["is_locked"]:
        print(line)
        print("Your account has been locked.")
        print("Please contact the bank administrator.")
        print(line)
        return None
    
    while True:
        entered_pin =input("Enter the PIN number: ")
        if data.accounts[acc_no]["pin"]==entered_pin:
            current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            data.accounts[acc_no]["attempts"] = 0
            data.accounts[acc_no]["last_login"] = current_time
            save_data()
            print(line)
            print("Login Successful!")
            print(f"WELCOME, {data.accounts[acc_no]['name']}")
            print(line)
            return acc_no
        else:
            data.accounts[acc_no]["attempts"]+=1
            print("Incorrect PIN.")
            remaining = 3 - data.accounts[acc_no]["attempts"]
            print(f"Attempts Remaining: {remaining}")
            if data.accounts[acc_no]["attempts"] >= 3:
                data.accounts[acc_no]["is_locked"] = True
                save_data()
                print(line)
                print("Account Locked\nToo many incorrect PIN attempts.") 
                print(line)
                return None

def deposit(acc_no):
    while True:
        try:
            amount=int(input("Enter the amount to deposit: ₹"))
            if amount<=0:
                print("Amount must be greater than zero.")
            else:
                break
        except ValueError:
            print("Invalid.....Enter a number ")
            continue
    
    data.accounts[acc_no]["balance"]+=amount
    record_transaction(
        acc_no,
        "Credit",
        "Cash Deposit",
        amount,
        data.accounts[acc_no]["balance"]
    )
    save_data()
    print(line)
    print("Deposit Successful!\n")
    print(f"Amount Deposited : ₹{amount}")
    print(f"Current Balance : ₹{data.accounts[acc_no]['balance']}")
    print(line)

def withdraw(acc_no):
    while True:
        try:
            amount=int(input("Enter the amount to withdraw: ₹"))
            if amount<=0:
                print("Amount must be greater than zero.")
            elif data.accounts[acc_no]['balance']-amount<500:
                print("Withdrawal denied. Minimum account balance of ₹500 must be maintained.")
            else:
                break
        except ValueError:
            print("Invalid.....Enter a number ")
            continue
    
    data.accounts[acc_no]["balance"]-=amount
    record_transaction(
        acc_no,
        "Debit",
        "Cash Withdrawal",
        amount,
        data.accounts[acc_no]["balance"]
    )
    save_data()
    print(line)
    print("Withdrawal Successful!\n")
    print(f"Amount withdraw : ₹{amount}")
    print(f"Current Balance : ₹{data.accounts[acc_no]['balance']}")
    print(line)

def transfer_money(sender_acc):
    while True:
        receiver_acc=input("Enter the Recevier Account number: ").strip().upper()
        if receiver_acc==sender_acc:
            print("You cannot transfer money to your own account.")
            continue
        if receiver_acc in data.accounts:
            print(f"Recipient Name: {data.accounts[receiver_acc]['name']}")
            while True:
                try:
                    amount=int(input("Enter the amount to Transfer: ₹"))
                    if amount<=0:
                        print("Amount must be greater than zero.")
                    elif data.accounts[sender_acc]['balance']-amount<500:
                        print("Transfer denied. Minimum account balance of ₹500 must be maintained.")
                    else:
                        break
                except ValueError:
                    print("Invalid.....Enter a number ")
                    continue
            
            while True:
                print(line)
                print("TRANSFER DETAILS".center(40))
                print(line)
                print(f"Recipient Name : {data.accounts[receiver_acc]['name']}")
                print(f"Account Number : {receiver_acc}")
                print(f"Amount         : ₹{amount}")
                print(line)
                confirm = input("Confirm Transfer? (Y/N): ").strip().upper()
                if confirm == "Y":
                    break
                elif confirm == "N":
                    print("Transfer Cancelled.")
                    return
                else:
                    print("Invalid choice. Please enter Y or N.")

            data.accounts[sender_acc]["balance"]-=amount
            record_transaction(
                sender_acc,
                "Debit",
                f"Transfer to {receiver_acc}",
                amount,
                data.accounts[sender_acc]["balance"]
            )
            data.accounts[receiver_acc]["balance"]+=amount
            record_transaction(
                receiver_acc,
                "Credit",
                f"Transfer from {sender_acc}",
                amount,
                data.accounts[receiver_acc]["balance"]
            )
            save_data()
            print(line)
            print("Transfer Successful!\n")
            print(f"Transferred To : {data.accounts[receiver_acc]['name']}")
            print(f"Account Number : {receiver_acc}")
            print(f"Amount         : ₹{amount}")
            print(f"Balance        : ₹{data.accounts[sender_acc]['balance']}")
            print(line)
        else:
            print("Account not found. Please enter a valid account number.")
            continue
        return

def account_details(acc_no):
    status = "Locked" if data.accounts[acc_no]["is_locked"] else "Active"
    last_login = (
        "Never"
        if data.accounts[acc_no]["last_login"] is None
        else data.accounts[acc_no]["last_login"]
    )
    print(line)
    print("ACCOUNT DETAILS".center(40))
    print(line)
    print()
    print(f"Account Number : {acc_no}")
    print(f"Account Holder : {data.accounts[acc_no]['name']}")
    print(f"Current Balance: ₹{data.accounts[acc_no]['balance']}")
    print(f"Created On     : {data.accounts[acc_no]['created_on']}")
    print(f"Last Login     : {last_login}")
    print(f"Status         : {status}")
    print()
    print(line)

def transaction_history(acc_no):
    history=data.accounts[acc_no]['history']
    if not history:
        print("No transactions found.")
        return
    
    print(line)
    print("TRANSACTION HISTORY".center(40))
    print(line)
    for t in reversed(history):
        print()
        print(f"Transaction ID #{t['transaction_id']}")
        print()
        print(f"Date    : {t['time']}")
        print(f"Type    : {t['type']}")
        print(f"Reason  : {t['reason']}")
        print(f"Amount  : ₹{t['amount']}")
        print(f"Balance : ₹{t['balance_after']}")
        print()
        print("-"*40)
    print(line)

def change_pin(acc_no):
    while True:
        current_pin = validate_pin("Enter the current 4-digit PIN: ")
        if current_pin!=data.accounts[acc_no]['pin']:
            print("Error....Enter the correct PIN.")
            continue
        else:
            while True:
                new_pin = validate_pin("Enter the new 4-digit PIN: ")
                if new_pin==current_pin:
                    print("Error...New PIN can not be same as old PIN.")
                    continue
                while True:
                    confirm_pin = validate_pin("Confirm the new 4-digit PIN: ")

                    if confirm_pin != new_pin:
                        print("Error... Confirmation PIN does not match.")
                        continue

                    data.accounts[acc_no]["pin"] = new_pin
                    save_data()
                    print(line)
                    print("PIN Updated Successfully!")
                    print(line)
                    return
                 
def check_balance(acc_no):
    print(line)
    print("BALANCE DETAILS".center(40))
    print(line)
    print()
    print(f"Current Balance   : ₹{data.accounts[acc_no]['balance']}")
    print(f"Available Balance : ₹{max(0, data.accounts[acc_no]['balance'] - 500)}")
    print()
    print(line)

def delete_account(acc_no):
    if data.accounts[acc_no]['balance']!=500:
        print(line)
        print("Account cannot be closed.")
        print("\nPlease transfer or withdraw funds until only the minimum balance (₹500) remains.")
        print(line)
        return False
    
    attempts = 3
    while attempts > 0:
        entered_pin = validate_pin("Enter your current 4-digit PIN: ")
        if entered_pin == data.accounts[acc_no]["pin"]:
            break
        else:
            attempts -= 1
            print("Incorrect PIN.")
            print(f"Attempts Remaining: {attempts}")

    if attempts==0:
        print(line)
        print("Too many incorrect PIN attempts.")
        print("Account deletion has been cancelled.")
        print("Please visit the bank for assistance.")
        print(line)
        return False
    
    confirm = input(f"Type your account number ({acc_no}) to permanently delete this account: "
    ).strip().upper()

    if confirm != acc_no:
        print("Account deletion cancelled.")
        return False

    print(line)
    print("DELETE ACCOUNT".center(40))
    print(line)
    print(f"Account Number : {acc_no}")
    print(f"Account Holder : {data.accounts[acc_no]['name']}")
    print(f"Current Balance: ₹{data.accounts[acc_no]['balance']}")
    print()
    print("WARNING!")
    print("This action is permanent and cannot be undone.")
    print(line)
    
    while True:
        choice = input("Are you sure you want to permanently delete this account? (Y/N): ").strip().upper()

        if choice == "Y":
            break

        elif choice == "N":
            print("Account deletion cancelled.")
            return False

        else:
            print("Invalid choice. Please enter Y or N.")

    del data.accounts[acc_no]
    save_data()

    print(line)
    print("Account deleted successfully.")
    print("Thank you for banking with us.")
    print(line)

    return True


ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def admin_login():
    attempts = 3
    while attempts > 0:
        username = input("Enter Admin Username: ").strip()
        password = input("Enter Admin Password: ").strip()
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            print(line)
            print("Admin Login Successful!")
            print("WELCOME, MB")
            print(line)
            return True
        attempts -= 1
        print("Invalid Username or Password.")
        print(f"Attempts Remaining: {attempts}")
    print(line)
    print("Access Denied.")
    print("Returning to Main Menu...")
    print(line)
    return False

def view_all_accounts():
    if not data.accounts:
        print(line)
        print("No accounts found.")
        print(line)
        return

    print(line)
    print("ALL ACCOUNTS".center(40))
    print(line)
    for acc_no, details in data.accounts.items():
        status = "Locked" if details["is_locked"] else "Active"
        print()
        print(f"Account Number : {acc_no}")
        print(f"Name           : {details['name']}")
        print(f"Balance        : ₹{details['balance']}")
        print(f"Status         : {status}")
        print(f"Created On     : {details['created_on']}")
        print()
        print("-"*40)
    print(line)
    print(line)
    print(f"Total Accounts : {len(data.accounts)}")
    print(line)

def display_account(acc_no, details):
    status = "Locked" if details["is_locked"] else "Active"

    print()
    print(f"Account Number : {acc_no}")
    print(f"Name           : {details['name']}")
    print(f"Balance        : ₹{details['balance']}")
    print(f"Status         : {status}")
    print(f"Created On     : {details['created_on']}")
    print("-" * 40)
    
def search_account():
    while True:
        print(line)
        print("SEARCH ACCOUNT".center(40))
        print(line)
        print()
        print("1. Search by Account Number")
        print("2. Search by Account Holder Name")
        print("3. Back")
        print()
        print(line)
        try:
            choice = int(input("Enter your choice: "))

            if choice < 1 or choice > 3:
                print("Invalid choice. Please enter 1-3.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice==1:
            search_acc =input("Enter the Account Number to search: ").strip().upper()
            if search_acc in data.accounts:
                print(line)
                print("SEARCH RESULT".center(40))
                print(line)
                display_account(search_acc, data.accounts[search_acc])
            else:
                print(line)
                print("Account not found.")
                print(line)

            input("\nPress Enter to continue...")

        elif choice == 2:
            search_name = validate_name("Enter the Account Holder Name to search: ")
            found = False
            for acc_no, details in data.accounts.items():
                if search_name.lower() == details["name"].lower():

                    if not found:
                        print(line)
                        print("SEARCH RESULTS".center(40))
                        print(line)

                    found = True
                    display_account(acc_no, details)
            if not found:
                print(line)
                print("No account found with this name.")
                print(line)
            input("\nPress Enter to continue...")

        elif choice==3:
            return

def unlock_account():
    acc_no = input("Enter the Account Number to unlock: ").strip().upper()
    
    if acc_no not in data.accounts:
        print(line)
        print("Account not found.")
        print(line)
        return

    if not data.accounts[acc_no]["is_locked"]:
        print(line)
        print("This account is already active.")
        print(line)
        return

    print(line)
    print("ACCOUNT FOUND".center(40))
    print(line)

    display_account(acc_no, data.accounts[acc_no])

    while True:
        choice = input("Unlock this account? (Y/N): ").strip().upper()
        if choice == "Y":
            data.accounts[acc_no]["is_locked"] = False
            data.accounts[acc_no]["attempts"] = 0
            save_data()
            print(line)
            print("Account unlocked successfully!")
            print(line)
            return
        elif choice == "N":
            print("Unlock operation cancelled.")
            return
        else:
            print("Invalid choice. Please enter Y or N.")

def bank_statistics():
    if not data.accounts:
        print(line)
        print("No accounts found.")
        print(line)
        return
    print(line)
    print(" BANK STATISTICS".center(40))
    print(line)
    print()
    print(f"Total Accounts : {len(data.accounts)}")
    locked=0
    balances=[]
    for details in data.accounts.values():
        balances.append(details["balance"])
        if details["is_locked"]:
            locked += 1

    total=sum(balances)
    high=max(balances)
    low=min(balances)
    avg = total / len(data.accounts)
    print(f"Active Accounts     : {len(data.accounts)-locked}")
    print(f"Locked Accounts     : {locked}")
    print(f"Total Bank Balance  : ₹{total}")
    print(f"Highest Balance     : ₹{high}")
    print(f"Lowest Balance      : ₹{low}")
    print(f"Average Balance     : ₹{avg:.2f}")
    print()
    print(line)

def delete_any_account():
    acc_no = input("Enter the Account Number to delete: ").strip().upper()

    if acc_no not in data.accounts:
        print(line)
        print("Account not found.")
        print(line)
        return

    print(line)
    print("DELETE ACCOUNT".center(40))
    print(line)

    display_account(acc_no, data.accounts[acc_no])

    print()
    print("WARNING!")
    print("This action is permanent and cannot be undone.")
    print(line)

    while True:
        choice = input("Are you sure you want to permanently delete this account? (Y/N): ").strip().upper()
        if choice == "Y":
            del data.accounts[acc_no]
            save_data()
            print(line)
            print("Account deleted successfully.")
            print(line)
            return
        elif choice == "N":
            print("Account deletion cancelled.")
            return
        else:
            print("Invalid choice. Please enter Y or N.")