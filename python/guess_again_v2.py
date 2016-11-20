import random

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

def compare(numA, numB):
    if numA > numB:
        return('high')
    elif numA < numB:
        return('low')
    else:
        return('correct')

def play():
    guess_count = 0
    # Pick a secret number
    secret_number = random.randint(1, 100)

    # When building your program, the following line will tell you what
    # the secret_number is; this will make it easier to test the game.
    # When done, remove or comment-out this line.
    #print('TEMPORARY DEBUGGING HELPER -> The secret number is: ' + str(secret_number))

    # Print message at the start the game
    print("\nI'm thinking of a number between 1 and 100; what do you think it is?")

    # Get the player's initial guess
    guess = get_guess()


    for guess_count in range(0,5):
        if guess!= secret_number:
            results = compare(guess, secret_number)
            guess_count = guess_count+1
            if 5-guess_count == 1:
                print('Too ' + results + '. You have ' + str(5-guess_count)+' guess left.\n')
            elif 5-guess_count >1:
                print('Too ' + results + '. You have ' + str(5-guess_count)+' guesses left.\n')
            guess = get_guess()
            if guess_count == 4 and guess != secret_number:
                    print ('Sorry, you ran out of turns! The secret number was ' + str(secret_number))
                    break
        elif guess == secret_number:
            print('You got it! The number was ' + str(secret_number))
            break

# Run the game
play()
