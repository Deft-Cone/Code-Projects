# Write, print and access strings in Python

print('Hello')

# Can use Double Quotes("") for sstrings with single quotes(')
print("That is Alice's cat")

# To use both double quotes and single quotes in a string, you must use "escape characters"
print('Say hi to Bob\'s mother')

# Common Escape Characters
# Prints As                 Escape Character
# Single Quote ____________ \'
# Double Quote ____________ \"
# Tab _____________________ \t
# Newline (line break) ____ \n
# Backslash _______________ \\

print('Hello there!\nHow are you?\nI\'m fine.')

print('\n\n\n\n')

# RAW STRINGS
# Same as normal string except beginning with r in front
# Raw strings negate escape characters, includeing the backslashes within the string
# helpful when typing a string with many backslashes

print(r'That is carol\'s cat.')
print(r'Say Hello!\nHello, friend!\nGood to see you\'re face!')

print('\n\n\n\n')

# Multi-line Strings
# Begins and ens with 3 single quotes(''') or double quotes (""")
# maintains multi-line format when printed
# useful when dealing with large strings, for example copy & pasting text from a book, poem, etc.

print("""Dear Alice,
Eve's cat has been arrested for catnaping, cat buglary, and extortion.
Sincerely,
Bob.""")

# when assigned a variable, python automatically formats it with \n
spam = """Dear Alice,
Eve's cat has been arrested for catnaping, cat buglary, and extortion.
Sincerely,
Bob."""

print('\n\n\n\n')

# Similarities between Strings and Lists
# Strings are a list-like value, with each character being like a value in the string which is like
# a list
soup = 'Hello World!'
print(soup)
# strings support indexing and slicing
print(soup[0])
print(soup[2:9])
print(soup[-1])
# strings suppoort "in" checks, NOTE: they are case sensitive
test = 'Hello' in soup
print(f"Is 'Hello' in soup?: {test}")
test2 = 'x' in soup
print(f"Is 'x' in soup?: {test2}")
test3 = 'HELLO' in soup
print(f"Is 'HELLO' in soup?: {test3}")
