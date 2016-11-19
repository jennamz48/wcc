import random

def multiply(a, b):
    result = a * b
    return result

# Test the function:
#solution = multiply(4, 5) # Invoke multiply giving it the arguments 4 and 5
#print(solution) # Expected: 20

#print(multiply(4,5))

multiply(4,5)

#print(multiply(4,5)) # 20
#print(multiply(9,11)) # 99
#print(multiply(0,10)) # 0
#print(multiply(.5,9)) # 4.5
#print(multiply(-1, -55)) # 55
#print(multiply(3, 'Hello')) # 'HelloHelloHello'

def isPositive(a):
    if a > 0:
        return True
    else:
        return False

#print(isPositive(-4)) # Expected: False
#print(isPositive(4)) # Expected: True
#print(isPositive(-9.9)) # Expected: False
#print(isPositive(9.9)) # Expected: True


def draw_random_card():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
    random.shuffle(cards)
    return cards.pop()

# Test the function
#print(draw_random_card()) # Expected: Random number b/n 1 & 11
#print(draw_random_card()) # Expected: Random number b/n 1 & 11
#print(draw_random_card()) # Expected: Random number b/n 1 & 11

def display_winner(winner, msg):
    if winner == 'Player':
        outcome = 'You win! '
    else:
        outcome = 'Computer wins! '

    print(outcome + '(' + msg + ')')

# Test the function
display_winner('Player', 'You were closest to 21') # Expected: You win! (You were closest to 21)
display_winner('Computer', 'It was closest to 21') # Expected: Computer wins! (It was closest to 21)
display_winner('Computer', 'You busted')  # Expected: Computer wins! (You busted)

def cube(a):
    product = a * a * a
    return product

#def isPositive(a):
#    return a > 0:

def mystery(x, y, z):
    result = x+y*z
    return result
    # ??? Your code here

# Test this function:
print mystery('Hello', 3, '!') # Expected: 'Hello!!!'
print mystery('Goodbye', 2, '@') # Expected: 'Goodbye@@'

def calculateTip (Price, Service):
    if Service == 'A':
        tip = 0.2*Price
    elif Service == 'B':
        tip = 0.18*Price
    elif Service == 'C':
        tip = 0.15*Price
    return tip

print(calculateTip(30.50, 'C')) # Expected: 4.575
print(calculateTip(15.00, 'B')) # Expected: 2.7
print(calculateTip(20.00, 'A')) # Expected: 4

def calculate_lucky_number(birth_month, birth_day):

    lucky_number = birth_month;

    if birth_month in [2, 4, 6]:
        lucky_number = birth_month + birth_day
        return lucky_number
    elif birth_month in [8, 10, 12]:
        lucky_number = (birth_month * 10) - birth_day
        return lucky_number

    return lucky_number * 2

print(calculate_lucky_number(2, 10)) # Expected: ???
print(calculate_lucky_number(10, 10)) # Expected: ???
print(calculate_lucky_number(11, 10)) # Expected: ???
