import re

message = 'My number is 415-555-4242'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject = phoneNumRegex.search(message) # returns a match object
# re.group() method returns entire pattern within string
print(matchObject.group())

# Use parentheses within the .search() method to specify a group within the pattern to search for
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchObject = phoneNumRegex.search(message)
print(matchObject.group())
print(matchObject.group(1))
print(matchObject.group(2))

# To define literal parentheses within a pattern, use escape characters
message2 = 'My number is (415) 555-4242'
phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d')
matchObject = phoneNumRegex.search(message2)
print(matchObject.group())

# Pipe character matches
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

# To find which suffix was found in pattern, pass in '1' to .group()
print(mo.group(1))

# if .search can't find regex pattern in the string, it will return 'None' to the matchObject
# calling .group() will return a NoneType error
mo = batRegex.search('Batmotorcycle lost a wheel')
print(mo)