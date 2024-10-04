import pprint

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])

print('My cat has ' + myCat['color'] + ' fur.')

spam = {12345: 'Luggage combination', 42: 'The Answer'}

# .keys() method returns list of keys in dictionary
print(list(myCat.keys()))

# .values method returns list of values in dictionary
print(list(myCat.values()))

# .items() method - returns list of 2 item tuples for key-value pairs in dicionary
print(list(myCat.items()))

# .get method takes key and fallback default vaule to return if key is not in dictionary
# if called for and key does not exist, will result in a key error
print(myCat.get('age', 15))


# methods can be used in loops
for k in myCat.keys():
    print(k)
    
for v in myCat.values():
    print(v)

for k, v in myCat.items():
    print(k, v)

if 'size' in myCat:
    print(myCat['size'])

# .setdefault() method - if a key is not set, will create a key with a default value
myCat.setdefault('age', 16)
print(myCat['age'])
print('\n \n \n')

# this program counts the number of occurances of a character in a string
message = 'It was a bright cold day in April, and the clocks wer striing thirteen.'
count = {}
print(message)
for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1
text = pprint.pformat(count)
print(text)




    
