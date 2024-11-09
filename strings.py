message = 'hello'
print(message)
print(type(message))

print("I'm having a great time in learning Python!")
print('My teacher said, "Keep Going, never give up!"')
print('They\'re over there shouting, "Help! Help!"')

word = 'Hello'
print(len(word))
print(word[4])
print(word[-5]) #Negative Indexing, last element as -1 - H

another_word = 'GoodBye'
print(another_word[0:4])
print(another_word[:-3])
print(another_word[:4])
print(another_word[4:7])
print(another_word[4:])
print(another_word[-3:]) # Bye
print(another_word[:])
print(another_word[1:6:2]) #ody - 3rd Parameter removes the element at specified position continously

print(another_word[::-1]) # Reverse String

numbers = '123456789'
print(numbers[1::2]) #2468

# String is immutable

# del word[0] - Not Possible, del word - Possible

text= 'Hello'
name = 'Andy'
print(text +' '+ name) # Hello Andy
print((text +' ') * 3) # Hello Hello Hello

print('a' in 'Gourab') #T
print('j' in 'Roxy') #F
juice = 'Apple Juice'
print('apple' in juice) #F
print('Apple' in juice) #T

sentence = 'I LOVE learning Python'
print(sentence.capitalize())
print(sentence.count('n'))
print(sentence.count('I', 1)) # Check for the specific char in specific Index - O/P is 0 because I is in 0the position
print(sentence.endswith('n')) # T
print(sentence.startswith('i')) # F
print(sentence.find('L')) # 2 
print(sentence.find('x')) # -1 - default - if not found
print(sentence.index('L'))
#print(sentence.index('z')) # Error
print('10'.isdigit()) #T
print('10a'.isdigit()) #F
print(sentence.isalpha()) #F - since it has space, it checks for only alphabetic strings
print(sentence.lower())
print(sentence.upper())
print(sentence.replace('Python', 'to code'))
print('   Hello    '.rstrip()) #Trim spaces from right side
print('   Hello   '.lstrip()) #Trim spaces from left side
print(sentence.title()) #First Letter Of Each Word Capitalize

print('I like to play {}'.format('Football'))
print('I also like to play {}, {} and {}'.format('Cricket', 'Badminton', 'Billiards'))
print('I also like to play {1}, {2} and {0}'.format('Cricket', 'Badminton', 'Billiards'))
print('I also like to play {a}, {b} and {c}'.format(a='Cricket', b='Badminton', c='Billiards'))