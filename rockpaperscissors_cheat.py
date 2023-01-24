computer_win = 0
while True:
    player = input("Rock, Paper, Scissors: ")
    
    if player == "Rock":
        print("The Computer used Paper to defeat Rock")
        computer_win = computer_win + 1
    elif player == "Paper":
        print("The Computer used Scissors to slice through Paper")
        computer_win = computer_win + 1
    elif player == "Scissors":
        print("The Computer used Rock to break the Scissors")
        computer_win = computer_win + 1

    ans = input("Play Again(Y/N): ")
    if ans.lower() != 'y':
        print("Player Score: 0")
        print("Computer Score:", computer_win)
        break
