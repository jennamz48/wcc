import random

# Get the user's guess
# Params: None
# Returns: Integer
#
def get_guess():

    # Get initial guess
    guess = raw_input('Enter your guess: ')

    # Assume it's not valid, until it's proven otherwise
    valid = False

    while valid != True:

        try:
            # Try and convert this number to an integer
            # If it fails, the exception will occur
            guess = int(guess)
        except Exception:
            # Exception was thrown when trying to convert to number,
            # Report the issue and ask again
            print('Invalid input; please enter a whole number.')
            valid = False
            guess = get_guess()

        # If they get here, it means the number must have been valid
        # Set valid to be true to break out of the while loop
        valid = True

    return guess

#print get_guess()


def compare(numA, numB):
    if numA > numB:
        return('High')
    elif numA < numB:
        return('Low')
    else:
        return('Correct')

#print compare(100,1)  # Expected: 'high'
#print compare(1,100)  # Expected: 'high'
#print compare(99,100) # Expected: 'low'

def play():
    attempt_count = 1
    # Pick a secret number
    secret_number = random.randint(1, 200)

    # When building your program, the following line will tell you what
    # the secret_number is; this will make it easier to test the game.
    # When done, remove or comment-out this line.
    print('TEMPORARY DEBUGGING HELPER -> The secret number is: ' + str(secret_number))

    # Print message at the start the game
    print("\nI'm thinking of a number between 1 and 100; what do you think it is?")

    # Get the player's initial guess
    guess = get_guess()

    # Keep prompting until they get it correct
    # For every failed attempt, print 'Too x. Guess again.' where x is either 'high' or 'low'


#Jenna's attempt, which also works:

#    while compare(guess, secret_number) != 'Correct':
#        if guess > secret_number:
#            print('Too high. Guess again.')
#        elif guess < secret_number:
#            print('Too low. Guess again.')
#        attempt_count = attempt_count+1
#        guess = get_guess()


#More eloquent version from WCC:

    while guess != secret_number:
        results = compare(guess, secret_number);
        print('Too ' + results + '. Guess again.\n')
        attempt_count = attempt_count+1
        guess = get_guess()


    # Print conclusion
    if compare(guess, secret_number) == 'Correct':
        print('You got it! The number was ' + str(secret_number))
        if attempt_count == 1:
            print('It took you ' + str(attempt_count) +' guess!')
        else:
            print('It took you ' + str(attempt_count) +' guesses!')
# Run the game
play()
