import random
while True:
    try:
        length=int(input("Enter the length of password: "))
        if length<=0:
            print("Length must be greater than 0")
            continue
        break
    except ValueError:
        print("Invalid..Enter a number")
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
special="!@#$%^&*"

char=lowercase
def yes_no(prompt):                     #prompt is just random name use for parameter
    while True:
        answer = input(prompt).lower()

        if answer in ["y", "n"]:
            return answer

        print("Please enter y or n")
    
upper = yes_no("Include Uppercase(y/n): ")
num = yes_no("Include numbers(y/n): ")
spl = yes_no("Include Special(y/n): ")


if upper=="y":
    char+=uppercase
if num=="y":
    char+=numbers
if spl=="y":
    char+=special


password=""
for i in range(length):
    password+=random.choice(char)

print(f"your password is:\n{password}")
