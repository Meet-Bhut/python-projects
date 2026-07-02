import json
import data

def save_data():
    with open("bank_data.json", "w") as file:
        json.dump(data.accounts, file, indent=4)

def load_data():
    try:
        with open("bank_data.json", "r") as file:
            data.accounts = json.load(file)
            highest = 0
            for account in data.accounts.values():
                for transaction in account["history"]:
                    current = int(transaction["transaction_id"][3:])
                    if current > highest:
                        highest = current
            data.transaction_counter = highest + 1
    except FileNotFoundError:
        data.accounts = {}
        data.transaction_counter = 1