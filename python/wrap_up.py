#def addTogether(a, b):
#    return a + b

#addTogether(9, 50)
#month = raw_input('Write the first three letters of a month and I will tell you which season it is in.')

# Convert month to lower case so the search is case insensitive

# Setup season lists

#def getSeason(month):

#    month = month.lower()

#    winter = ['dec','jan','feb']
#    spring = ['mar', 'apr', 'may']
#    summer = ['jun', 'jul', 'aug']
#    fall   = ['sep', 'oct', 'nov']
    # Determine which season list the `month` is in

#    if month in winter:
#        print ('That month is in winter')

#    elif month in spring:
#        print ('That month is in spring')

#    elif month in summer:
#        print ('That month is in summer')

#    else:
#        print('That month is in fall')
#getSeason(month)
    # Use a cascading if statement



#temp = raw_input('Type the temperature in Fahrenheit: ')

#def getCelsius(temp):
#    Ctemp = (int(temp) - 32)/1.8
#    Ctemp = round(Ctemp, 2)
#    print'The temperature in Celsius is  '+ str(Ctemp) + ' degrees'

#getCelsius(F)


#temp = raw_input('Type the temperature in Celsius: ')

#def getFahrenheit(temp):
#    Ftemp = (int(temp) * 1.8) + 32
#    Ftemp = round(Ftemp, 2)
#    print'The temperature in Fahrenheit is  '+ str(Ftemp) + ' degrees'

#getFahrenheit(C)


#temp = int(raw_input('Type a temperature'))
#scale = str(raw_input('What scale would you like to convert to? '))

#def temperatureConverter(temp, scale):
#    if scale == 'C':
#        print (getCelsius(temp))

#    elif scale == 'F':
#        print (getFahrenheit(temp))

#    else:
#        print 'Invalid scale: choose C or F'

#temperatureConverter(temp, scale)
word = raw_input('Please type a word')

def vowel_counter(word):
    vowel_count = 0

    aeiou = ['a', 'e', 'i', 'o', 'u']
    for letter in word:
        if letter in aeiou:
            vowel_count = vowel_count+1
        else:
            vowel_count = vowel_count
    print 'There are ' + str(vowel_count) + ' vowels in your word'

vowel_counter(word)
