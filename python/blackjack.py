import random

# Set up
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
random.shuffle(cards)

# Round 1
player_card1 = cards.pop()
computer_card_1 = cards.pop()

print('Your card: ' + str(player_card1))
print('computer card:  ' + str(computer_card_1))

#Round 2
decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

computer_card_2 = cards.pop()
if decision == 'h':
    player_card2 = cards.pop()

elif decision == 's':
    player_card2 = 0
print('Your new cards: ' +str(player_card1) + ", "+ str(player_card2))
print('Computer cards: ' +str(computer_card_1)+ ", "+str(computer_card_2))

#Round 3

decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

if decision == 'h':
    player_card3 = cards.pop()

elif decision == 's':
    player_card3 = 0

if computer_card_1 + computer_card_2 <= 16:
    computer_card_3 = cards.pop()
elif computer_card_1 + computer_card_2 > 16:
    computer_card_3 = 0

print('Your new cards: ' +str(player_card1) + ", "+ str(player_card2) + ", "+ str(player_card3))
print('Computer cards: ' +str(computer_card_1)+ ", "+str(computer_card_2)+ ", "+ str(computer_card_3))

#Results
print('\nGame Over')
player_score = player_card1 + player_card2 + player_card3
computer_score = computer_card_1 + computer_card_2 + computer_card_3

print('Your score: ' + str(player_score))
print('Computer score: ' + str(computer_score))

if player_score == computer_score:
    print ('Tie!')

elif player_score > 21 and computer_score >21:
    print ('Tie! (Both Player and Computer Busted)')

elif player_score <= 21 and computer_score >21:
    print ('You win! (Computer Busted)')
elif player_score > 21 and computer_score <= 21:
    print ('Computer wins! (You Busted)')
elif player_score <=21 and computer_score <= 21 and player_score > computer_score:
    print ('You win! (Closest to 21)')
else:
    print ('Computer won! (It was closest to 21)')
