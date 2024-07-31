#1 is X and 2 is O
#0 is empty

def print_board(current_board):
    for i in range(0, 9, 3):
        print(current_board[i] + " | " + current_board[i+1] + " | " + current_board[i+2])
        if i < 6:
            print("-"*9)
        
def main():
    game_over = False
    current_board = [" ", " ", " "," ", " ", " ", " ", " ", " "]
    print_board(current_board)
    int(input("Enter a number between 1 and 9 to place your character in the box: "))

main()
