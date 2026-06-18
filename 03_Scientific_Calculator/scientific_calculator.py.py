import math

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def power(a,b):
    return a**b

def square_root(x):
    return math.sqrt(x)

def logarithm(x):
    return math.log(x)

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

operations={
    1:add,
    2:sub,
    3:mul,
    4:div,
    5:power,
    6:square_root,
    7:logarithm,
    8:sine,
    9:cosine,
    10:tangent
}

while True:
    print("---------MENU--------")
    print("""
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Square Root
7. Logarithm
8. Sine
9. Cosine
10. Tangent
11. Exit
""")
    while True:
        try:
            choice = int(input("Enter your choice: "))

            if choice < 1 or choice > 11:
                print("Enter a number between 1 and 11")
                continue

            break

        except ValueError:
            print("Please enter a valid number")

    if choice == 11:
        print("Exiting...")
        break

    if choice <= 5:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = operations[choice](a, b)

            print(f"Result = {result}")

        except ValueError:
            print("Please enter valid numbers")

    else:
        try:
            x = float(input("Enter a number: "))

            result = operations[choice](x)

            print(f"Result = {result}")

        except ValueError:
            print("Please enter a valid number")
    print("---------MENU--------")
    print("\n1:add\n2:sub\n3:mul\n4:div\n5:power\n6:square_root\n7:logarithm,8:sine\n9:cosine,\n10:tangent\n11:Exit")
    try:
        choice=int(input("\nEnter your choice of operation: "))
        if choice < 1 or choice > 11:
            print("Enter the Number in range of 1-10")
            continue
        break
    except ValueError:
        print("Please enter a valid number")

    if choice<=5:
        a=float(input("Enter the 1st number: "))
        b=float(input("Enter the 2nd number: "))
    elif choice<=10:
        x=float(input("Enter a number: "))
    else:
        print("Exiting.......")