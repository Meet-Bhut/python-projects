board=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
def print_board(board):
    print("\n  0   1   2")
    print("0  "+" | ".join(board[0]))
    print("-" * 13)
    print("1  "+" | ".join(board[1]))
    print("-" * 13)
    print("2  "+" | ".join(board[2]))

def winner(board):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] and board[i][0]!=" ":
            return board[i][0]
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=" ":
            return board[0][i]
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=" ":
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!=" ":
        return board[0][2]
    else:
        return None

def move(board,player):
    while True:
        try:
            r = int(input("Enter the row: "))
            c = int(input("Enter the column: "))

            if not (0 <= r <= 2 and 0 <= c <= 2):
                print("Row and column must be between 0 and 2")
                continue
            
            if board[r][c] != " ":
                print("Cell is already occupied")
                continue
            
            board[r][c] = player
            break
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")


def board_full(board):
    flag=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                flag=1
                break
    
    if flag==0:
        return True
    return False

player="X"
while True:
    
    print_board(board)
    print(f"\nPlayer {player}'s turn")
    move(board, player)

    result = winner(board)

    if result:
        print_board(board)
        print(f"Congratulation!! {result} won the game")
        break
        

    if board_full(board):
        print_board(board)
        print("It's a Draw")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"