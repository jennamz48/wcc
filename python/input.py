#name = raw_input('What is your name? ')
#print('Hi ' + name)

#name = raw_input('What is your name?')
#age = raw_input('How old are you?')
#print(name + ' is ' + age + ' years old.')

#age = raw_input('How old are you?')
#dog_years = age * 7
#print('You are ' + dog_years + 'old in dog years.')

#age = raw_input('How old are you? ')
#dog_years = int(age) * 7
#print('You are ' + str(dog_years) + ' years old in dog years.')


meal = float(raw_input('How much was your meal?'))
tip = round(float(meal)*0.20,2)
total_cost = round(float(meal + tip),2)

print("You should tip " + "$" + str(tip))
print("Your total cost would be " + "$" + str(total_cost))
