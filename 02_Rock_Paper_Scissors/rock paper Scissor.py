import random

options=["rock","paper","scissor"]
player_score=0
computer_score=0
draw=0
win_rule={                            # dictionary (not part of mannual)
        "rock":"scissor",             # rock beats scissor
        "paper":"rock",               # paper beats rock
        "scissor":"paper"             # scissor beats paper
    }
while True:
    try:
        game = int(input("Enter number of games: "))
        if game <=0:
            print("Number of games must be greater than 0")
            continue
        break
    except ValueError:
        print("Please enter a valid number")

    
def rps():
    while True:
        player=input("Enter a choice (rock/paper/scissor): ").lower()
        if player in options:
            break
        print("Choose a valid input")
        
    computer=random.choice(options)
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player==computer:
        print("It's a Draw!")
        return "draw"
    elif win_rule[player]==computer:     #if both matches that means player wins
        print("You Win 🎉")
        return "player"                 
    else:                               #if not matches that means computer wins
        print("Computer Win")          
        return "computer"               
    
    # manual checking (replaced by dictonay and win rule )
    # elif player=="rock" and computer =="scissor":
    #     print("You Win 🎉")                                    
    #     return "player"
    # elif player=="rock" and computer =="paper":
    #     print("Computer Win")
    #     return "computer"
    # elif player=="paper" and computer =="scissor":
    #     print("Computer Win")
    #     return "computer"
    # elif player=="paper" and computer =="rock":
    #     print("You Win 🎉")
    #     return "player"
    # elif player=="scissor" and computer =="rock":
    #     print("Computer Win")
    #     return "computer"
    # elif player=="scissor" and computer =="paper":
    #     print("You Win 🎉")
    #     return "player"
    

for i in range(game):
    print(f"\nRound {i+1}")
    result=rps()
    if result == "player":
        player_score += 1
    elif result == "computer":
        computer_score += 1
    else:
        draw += 1

print(f"\nFrom Best of {game} games the scores are:")
print(f"Player: {player_score}")
print(f"Computer: {computer_score}")
print(f"Draw: {draw}")
if player_score > computer_score:
    print("\nCongratulation! you won the game🎉🎉")
elif player_score < computer_score:
    print("\nYou lost... Better luck next time")
else:
    print("\nIt's a Draw")



