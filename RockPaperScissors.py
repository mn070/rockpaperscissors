"""
3 choices:
Rock, paper, scissors
-> use if-else statements
-> use random to pick the choices
"""

import random, time, sys

print('''Hello!!! Welcome to Rock, Paper, Scissors game. Here are a few rules for the game:
- Rock beats scissors
- Paper beats rock
- Scissors beats paper
''')

wins = 0
losses = 0
ties = 0

while True:     # Main game loop
    while True:     # keep asking until player enter R, P, S or Q
        print("{} Wins, {} Losses, {} Ties".format(wins, losses, ties)) 
        print('\n')
        print("Enter your move: (P)aper, (R)ock, (S)cissors or (Q)uit!")
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print("Thank you for playing!")
            sys.exit()

        # if player did not choose to quit, break the loop:
        if playerMove == 'P' or playerMove == 'R' or playerMove == 'S':
            break
        else:
            print("Please enter R, or P, or S, or Q to quit the game.")
    
    # Display player's choice
    if playerMove == "P":
        print("Paper versus...")
        playerMove = 'PAPER'
    elif playerMove == "R":
        print("Rock versus...")
        playerMove = 'ROCK'
    elif playerMove == "S":
        print('Scissors versus...')
        playerMove = 'SCISSORS'
    

    # Count to three before showing the computer's move (dramatic effect):
    time.sleep(0.5)
    print("1...")
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # Display computer's choice
    randomNum = random.randint(1, 3)
    if randomNum == 1:
        computerMove = 'ROCK'
    elif randomNum == 2:
        computerMove = 'PAPER'
    elif randomNum == 3:
        computerMove = 'SCISSORS'
    print(computerMove)
    time.sleep(0.5)
    
    # Display and record all the results
    if playerMove == computerMove:
        print("It's a tie!")
        ties += 1
    elif playerMove == "ROCK" and computerMove == 'SCISSORS':
        print('You win!!!')
        wins += 1
    elif playerMove == 'PAPER' and computerMove == 'ROCK':
        print("You win!!!")
        wins += 1
    elif playerMove == 'SCISSORS' and computerMove == 'PAPER':
        print('You win!!!')
        wins += 1
    elif playerMove == 'ROCK' and computerMove == 'PAPER':
        print("You lose!")
        losses += 1
    elif playerMove == 'PAPER' and computerMove == 'SCISSORS':
        print("You lose!")
        losses += 1
    elif playerMove == 'SCISSORS' and computerMove == 'ROCK':
        print('You lose!')
        losses += 1


