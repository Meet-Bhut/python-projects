import random 


difficulty=input("Enter the difficulty level (Easy/Medium/Hard):")

def guess_the_number(upper):
    number=random.randint(1,upper)
    guesses=0
    while True:
        try:
            guess=int(input(f"Guess a number between 1-{upper}:"))
            if guess < 1 or guess > upper:
                print("Invalid! Number out of range")
                continue
        except ValueError:
            print("Invalid input")
            continue
        guesses+=1
        if guess > number:
            print("Too high!")
        elif guess <number:
            print("Too low!")
        else:
            print(f"Congratulations! You guessed correctly. The number was {guess}")
            break


    print(f"you required {guesses} guesses to guess the number")
    again=input("Would you like to play again?(press y to play again or press any key to exit)")
    if again=="y":
        guess_the_number(upper)
    else:
        print("Exiting.........")
if difficulty=="Easy":
    guess_the_number(50)

elif difficulty=="Medium":
    guess_the_number(100)

elif difficulty=="Hard":
    guess_the_number(1000)
else:
    print("Invalid difficulty level")


