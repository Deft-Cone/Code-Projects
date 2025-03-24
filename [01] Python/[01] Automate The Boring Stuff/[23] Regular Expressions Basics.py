# Import re module for regular expressions
import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 today.'

# Create Regular Expression Object
# re.compile() takes raw string as a pattern to search for
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# re.search method searches passed string for compiled pattern
matchObject = phoneNumRegex.search(message)

# regex.group() method returns the found pattern within text
print(matchObject.group())

# re.findall() method returns a list of all patterned text within given string
print(phoneNumRegex.findall(message))