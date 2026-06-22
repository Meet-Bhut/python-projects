from datetime import datetime
import matplotlib.pyplot as plt

def add_expense():
    while True:
        category = input("Enter the category: ").strip().title()
        if category == "":
            print("Category cannot be empty.")
        else:
            break
    while True:
        try:
            amount = float(input("Enter the amount: ₹"))
            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    today = datetime.now()
    date=today.strftime("%Y-%m-%d")
    with open("expense.txt", "a") as file:
        file.write(f"{date},{category},{amount:.2f}\n")
    
    year,month,day=date.split("-")
    display_date=f"{day}-{month}-{year}"
    print("\n")
    print("-"*20)
    print("Expense Details:")
    print("Date:", display_date)
    print("Category:", category)
    print(f"Amount: ₹{amount:.2f}")
    print("-"*20)
    print("\nExpense added successfully.")

def show_expenses():
    with open("expense.txt", "r") as file:
        lines = file.readlines()
    if not lines:
        print("No expense found.\n")
        return

    print("-" * 50)
    print("Date           Category            Amount")
    print("-" * 50)
    for line in lines:
        date, category, amount = line.strip().split(",")
        year, month, day = date.split("-")
        display_date = f"{day}-{month}-{year}"
        print(f"{display_date:<15}{category:<20}₹{amount}")

    print("-" * 50)

def search_expense():
    with open("expense.txt", "r") as file:
        search = input("Enter category to search: ").strip().lower()
        found = False
        for line in file:
            date, category, amount = line.strip().split(",")
            year, month, day = date.split("-")
            display_date = f"{day}-{month}-{year}"
            if category.lower() == search:
                print("-" * 20)
                print(f"Date: {display_date}")
                print(f"Category: {category}")
                print(f"Amount: ₹{amount}")
                print("-"*20)
                found = True
        if not found:
            print("No such Category found")

def delete_expense():
    delete = input("Enter Category to delete: ").strip().lower()
    found = False
    matches=[]
    with open("expense.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            date, category, amount = line.strip().split(",")
            if category.lower() == delete:
                matches.append(line)
                found = True
    if not found:
        print("No such Category found")
        return
    
    print("\nMatching Expenses:")
    print("-" * 40)
    for i, line in enumerate(matches, start=1):
        date, category, amount = line.strip().split(",")
        year, month, day = date.split("-")
        display_date = f"{day}-{month}-{year}"
        print(f"{i}. {display_date} {category} ₹{amount}")
    print("-" * 40)
    while True:
        try:
            choice = int(input("Enter expense number to delete: "))
            if 1 <= choice <= len(matches):
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

    selected_line=matches[choice - 1]
    lines.remove(selected_line)
    with open("expense.txt", "w") as file:
        file.writelines(lines)
    print("Expense deleted successfully")


def total_expenses():
    totals={}
    total_amount =0
    with open("expense.txt", "r") as file:
        lines = file.readlines()
        if not lines:
            print("No expenses found.")
            return
        for line in lines:
            date, category, amount = line.strip().split(",")
            if category in totals:
                totals[category] += float(amount)
            else:
                totals[category] = float(amount)
    print("-"*30)
    for category,amount in totals.items():
        print(f"{category:<15} ₹{amount:.2f}")
        total_amount +=amount
    print("-"*30)
    print(f"\nTotal Spending: ₹{total_amount:.2f}")
    return totals

def category_graph():
    totals=total_expenses()
    if totals is None:
        return
    categories=list(totals.keys())
    amount=list(totals.values())
    plt.figure(figsize=(7,7))
    plt.pie(amount,labels=categories,autopct="%1.1f%%")
    plt.title("Expense Category Distribution")
    plt.show()

def month_graph():
    monthly_totals = {}
    with open("expense.txt", "r") as file:
        lines = file.readlines()
        if not lines:
            print("No expenses found.")
            return
        month_names = {
            "01": "Jan",
            "02": "Feb",
            "03": "Mar",
            "04": "Apr",
            "05": "May",
            "06": "Jun",
            "07": "Jul",
            "08": "Aug",
            "09": "Sep",
            "10": "Oct",
            "11": "Nov",
            "12": "Dec"
        }
        for line in lines:
            date, category, amount = line.strip().split(",")
            year, month, day = date.split("-")
            month_key = f"{month_names[month]} {year}"
            if month_key in monthly_totals:
                monthly_totals[month_key] += float(amount)
            else:
                monthly_totals[month_key] = float(amount)
    months=list(monthly_totals.keys())
    amounts=list(monthly_totals.values())
    plt.bar(months,amounts)
    plt.title("Monthly Expenses")
    plt.xlabel("Month")
    plt.ylabel("Amount (₹)")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()

while True:
    print("---------MENU--------")
    print("""
1. Add Expense
2. Show Expenses
3. Search Expense
4. Delete Expense
5. Total Spending
6. Category Graph
7. Monthly Graph
8. Exit
""")
    try:
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 8:
            print("Enter a number between 1 and 8")
            continue
    except ValueError:
        print("Please enter a valid number")
        continue
    if choice == 1:
        add_expense()
    elif choice == 2:
        show_expenses()
    elif choice == 3:
        search_expense()
    elif choice == 4:
        delete_expense()
    elif choice == 5:
        total_expenses()
    elif choice == 6:
        category_graph()
    elif choice == 7:
        month_graph()
    elif choice == 8:
        print("Exiting...")
        break