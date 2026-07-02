from storage import load_data
from bank_functions import (
    create_account,
    login,
    deposit,
    withdraw,
    transfer_money,
    check_balance,
    transaction_history,
    account_details,
    change_pin,
    delete_account,
    admin_login,
    view_all_accounts,
    search_account,
    unlock_account,
    bank_statistics,
    delete_any_account
)


def main_menu():
    while True:
        print("=" * 40)
        print("MAIN MENU".center(40))
        print("=" * 40)
        print("""
1. Create Account
2. Login
3. Admin Login
4. Exit
""")

        try:
            choice = int(input("Enter your choice: "))

            if 1 <= choice <= 4:
                return choice

            print("Invalid choice. Please enter 1-4.")

        except ValueError:
            print("Please enter a valid number.")


def banking_menu():
    while True:
        print("=" * 40)
        print("BANKING MENU".center(40))
        print("=" * 40)
        print("""
1. Deposit Money
2. Withdraw Money
3. Transfer Money
4. Check Balance
5. Transaction History
6. Account Details
7. Change PIN
8. Logout
9. Delete Account
""")

        try:
            choice = int(input("Enter your choice: "))

            if 1 <= choice <= 9:
                return choice

            print("Invalid choice. Please enter 1-9.")

        except ValueError:
            print("Please enter a valid number.")

def admin_menu():
    while True:
        print("=" * 40)
        print("ADMIN MENU".center(40))
        print("=" * 40)
        print("""
1. View All Accounts
2. Search Account
3. Unlock Account
4. Bank Statistics
5. Delete Any Account
6. Logout
""")

        try:
            choice = int(input("Enter your choice: "))

            if 1 <= choice <= 6:
                return choice

            print("Invalid choice. Please enter 1-6.")

        except ValueError:
            print("Please enter a valid number.")

def main():
    load_data()
    while True:
        choice = main_menu()
        if choice == 1:
            create_account()
        elif choice == 2:
            acc_no = login()
            if acc_no is None:
                continue
            while True:
                bank_choice = banking_menu()
                if bank_choice == 1:
                    deposit(acc_no)
                elif bank_choice == 2:
                    withdraw(acc_no)
                elif bank_choice == 3:
                    transfer_money(acc_no)
                elif bank_choice == 4:
                    check_balance(acc_no)
                elif bank_choice == 5:
                    transaction_history(acc_no)
                elif bank_choice == 6:
                    account_details(acc_no)
                elif bank_choice == 7:
                    change_pin(acc_no)
                elif bank_choice == 8:
                    print("Logged out successfully.")
                    break
                elif bank_choice == 9:
                    if delete_account(acc_no):
                        print("Logged out successfully.")
                        break
        elif choice == 3:
             if admin_login():
                while True:
                    admin_choice = admin_menu()
                    if admin_choice == 1:
                        view_all_accounts()
                    elif admin_choice == 2:
                        search_account()
                    elif admin_choice == 3:
                        unlock_account()
                    elif admin_choice == 4:
                        bank_statistics()
                    elif admin_choice == 5:
                        delete_any_account()
                    elif admin_choice == 6:
                        print("Admin Logged Out.")
                        break
        elif choice == 4:
            print("Thank you for using the Banking System.")
            break


if __name__ == "__main__":
    main()