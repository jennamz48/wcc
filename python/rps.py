import random

def check_move(move):
    if move == 'rock' or move == 'Rock':
        return True
    elif move == 'paper' or move == 'Paper':
        return True
    elif move == 'scissors' or move == 'Scissors':
        return True
    else:
        return False

# Test the check_move function
#print check_move('rock') # Expects: True
#print check_move('paper') # Expects: True
#print check_move('scissors') # Expects: True
#print check_move('roc') # Expects: False
#print check_move(1) # Expects: False

def get_player_move():

    # Prompt the user to enter their move
    move = raw_input('Pick your move: rock, paper, or scissors? ')

    # This will happen on a loop until the user enters a valid move
    while check_move(move) == False:
        print('Invalid move; pick again.')
        # Run this function again, so they're asked to enter a new move
        move = get_player_move()

    # If they get out of the while loop, it means they
    # entered a valid move, so return it
    return move

# Test this function
#print 'You picked: ' + get_player_move()

# This function is provided; no edits are needed
# Parameters: None
# Returns: String of 'rock', 'paper', or 'scissors'
def get_computer_move():
    moves = ['rock', 'paper', 'scissors'];
    return random.choice(moves)

#print get_computer_move() # Expected: 'rock', 'paper', or 'scissors'
#print get_computer_move() # Expected: 'rock', 'paper', or 'scissors'
#print get_computer_move() # Expected: 'rock', 'paper', or 'scissors'


def judge(moveA, moveB):

    # YOUR CODE HERE
    if moveA == 'rock' and moveB == 'paper':
        return False
    elif moveA == 'rock' and moveB == 'scissors':
        return True
    elif moveA == 'paper' and moveB == 'rock':
        return True
    elif moveA == 'paper' and moveB == 'scissors':
        return False
    elif moveA == 'scissors' and moveB == 'rock':
        return False
    elif moveA == 'scissors' and moveB == 'paper':
        return True



#print judge('rock','paper') # Expected: False
#print judge('rock','scissors') # Expected: True
#print judge('paper','rock') # Expected: True
#print judge('paper','scissors') # Expected: False
#print judge('scissors','rock') # Expected: False
#print judge('scissors','paper') # Expected: True


def play():

    print('Welcome to Welcome to Rock, Paper, Scissors!')

    # Player goes
    moveA = get_player_move()

    # Computer goes
    moveB = get_computer_move()


    print('The computer picked: ' + moveB)

    # Figure out who won
    judge(moveA, moveB)
    # Print results; either: `Tie`, `You Won!`, or `The computer won.`
    if judge(moveA, moveB) == False:
        print('The computer won!')
    elif judge(moveA, moveB) == True:
        print('You won!')
    else:
        print('Tie!')
    # Prompt to play again
    play_again = raw_input('Play again? Type `y` or `n`: ')

    if(play_again == 'y'):
        play()
    else:
        print('Thanks for playing!')

# Run the game  
play()
