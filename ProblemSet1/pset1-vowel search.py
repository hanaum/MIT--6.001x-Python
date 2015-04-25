'''Counting Vowels: counts up the number of vowels contained in the string 's'
				Valid vowels are 'a','e','i','o','u'

ex: 
s = 'azcbobobegghakl' should print "Number of vowels: 5"

MIT-6.001x Python
Hana Um
'''

vowels = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        vowels += 1
print "Number of vowels: " + str(vowels)
