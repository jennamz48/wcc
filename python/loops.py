#print '#'
#print '##'
#print '###'
#print '####'
#print '#####'
#print '######'
#print '#######'
#print '########'
#print '#########'
#print '##########'


#print '#' * 1
#print '#' * 2
#print '#' * 3
#print '#' * 4
#print '#' * 5
#print '#' * 6
#print '#' * 7
#print '#' * 8
#print '#' * 9
#print '#' * 10

counter = 1
#while counter <= 10:
#    print '#' * counter
#    counter = counter + 1

# First, define the sequence we'll loop through
numbers = range(0,10)
# Used Built-in Python function range() to produce a list: [0,1,2,3,4,5,6,7,8,9]

for counter in numbers:
    print '#' * counter


greeting = 'Hello World'
for letter in greeting:
    print letter

continents = ['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'Australia', 'South America']
for continent in continents:
    print continent + ' is a continent.'

print range(0, 15)

print range(10)

vowels = ['a', 'e', 'i', 'o', 'u']
for vowel in vowels:
    print vowel
