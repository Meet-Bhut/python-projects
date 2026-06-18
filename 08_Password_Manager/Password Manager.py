def input_pass():
        with open("passwords.txt", "a") as file:
                website = input("Enter website: ")
                username = input("Enter username: ")
                password = input("Enter password: ")
                
                file.write(f"{website},{username},{password}\n")

def show():
        with open("passwords.txt","r") as file:
                for line in file:
                        web,user,pas = line.strip().split(",")
                        print("-"*20)
                        print(f"Website: {web}")
                        print(f"Username: {user}")
                        print(f"Password: {pas}")
                        print("-"*20)

def search():
    with open("passwords.txt", "r") as file:
        search = input("Enter website to search: ").lower()
        found = False
        for line in file:
            web, user, pas = line.strip().split(",")
            if web.lower() == search:
                print("-" * 20)
                print(f"Website: {web}")
                print(f"Username: {user}")
                print(f"Password: {pas}")
                print("-"*20)
                found = True
        if not found:
            print("No such website found")

def delete():
    delete = input("Enter website to delete: ").lower()
    found = False
    new_lines = []
    with open("passwords.txt", "r") as file:
        for line in file:
            web, user, pas = line.strip().split(",")
            if web.lower() == delete:
                found = True
            else:
                new_lines.append(line)
    if not found:
        print("No such website found")
    else:
        with open("passwords.txt", "w") as file:
            file.writelines(new_lines)
        print("Password deleted successfully")

def edit():
    website_to_edit = input("Enter website to edit: ").lower()
    found = False
    new_lines = []
    with open("passwords.txt", "r") as file:
        for line in file:
            web, user, pas = line.strip().split(",")
            if web.lower() == website_to_edit:
                new_username = input("Enter new username: ")
                new_password = input("Enter new password: ")
                new_lines.append(f"{web},{new_username},{new_password}\n")
                found = True
            else:
                new_lines.append(line)
        if not found:
            print("No such website found")
        else:
            with open("passwords.txt", "w") as file:
                file.writelines(new_lines)
            print("Password updated successfully")
	
while True:
    print("---------MENU--------")
    print("""
1. Add Password
2. Search by Website
3. Delete by Website
4. Show Passwords
5. Exit
""")
    try:
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 6:
            print("Enter a number between 1 and 6")
            continue
    except ValueError:
        print("Please enter a valid number")
        continue
    if choice == 1:
        input_pass()
    elif choice == 2:
        search()
    elif choice == 3:
        delete()
    elif choice == 4:
        show()
    elif choice == 5:
        edit()
    elif choice == 6:
        print("Exiting...")
        break
    

     
