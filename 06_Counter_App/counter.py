counter=0
def increment(counter):
    return counter+1

def decrement(counter):
    return counter-1


def increment_by(counter,costum):
    return counter + costum


def decrement_by(counter,costum):
    return counter - costum

def reset():
    return 0


def show(counter):
    print(f"The counter is: {counter}")

while True:
    print("""
--------MENU--------
1. Increment (+1)
2. Decrement (-1)
3. Increment by Custom Value
4. Decrement by Custom Value
5. Reset Counter
6. Show Counter
7. Exit""")

    try:
        choice=int(input("Enter the choice: "))
        if choice < 1 or choice > 7:
            print("Enter a number between 1 and 7")
            continue
    except ValueError:
        print("Invalid...Enter a number")
        continue

    if choice == 1:
        counter = increment(counter)

    elif choice == 2:
        counter = decrement(counter)

    elif choice == 3:
        try:
            custom = int(input("Enter value to increment: "))
            counter = increment_by(counter, custom)
        except ValueError:
            print("Invalid number")

    elif choice == 4:
        try:
            custom = int(input("Enter value to decrement: "))
            counter = decrement_by(counter, custom)
        except ValueError:
            print("Invalid number")

    elif choice == 5:
        counter = reset()

    elif choice == 6:
        show(counter)

    elif choice == 7:
        print("Exiting...")
        break

