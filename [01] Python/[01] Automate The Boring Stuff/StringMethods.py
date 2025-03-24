# String Methods

# .upper() method returns string with all uppercase characters
spam = 'Hello World!'
print(spam)
print(spam.upper())

# .lower() method returns string with all lowercase characters
print(spam.lower())

# .title() method returns string with title casing on all words
print(spam.title())

# remember strings are immutable and can't be modified in place
# to modify the variable spam you would require:
#       spam = spam.upper() or spam = spam.lower()
# Non-letter characters ('",.!?) are unaffected

# Useful when you need a case-insensitive comparison
##print('Want to play again? Yes or No? (try any capitalization!')
##answer = input()
##if answer.lower() == 'yes':
##    print('playing again')

# .isupper and .islower returns a boolean value depending on if the string contains
#   uppercase or lowercase
test = spam.isupper()
print(test)
test2 = spam.islower()
print(test2)

## Other methods to check nature of the string, returning a boolean value
# .isalpha() - checks if letters only
# .isalnum() - checks if letters and numbers only
#. isdecimal() - checks if numbers only
# .isspace() - checks if whitespace only
# .istitle() - checks if TitleCase only (Words Begin With Uppercase And Folowed By Lower)

# .startswith() returns true if string begins with string that's passed through the method
spam.startswith('Hello')
# .endswith() returns true if string ends with string that's passed through the method
spam.endswith('world!')

# .join() joins a list of strings into a sinlge string value
# called on a string, is passed a list of strings, and returns a single string
# the string the method is called on will become the delimiter 
print(','.join(['cats', 'bats', 'rats']))
print(''.join(['cats', 'bats', 'rats']))
print(' '.join(['cats', 'bats', 'rats']))
print('\n\n'.join(['cats', 'bats', 'rats']))

# .split() is alled on a string value and retuns a list of stings
# splits on whitespace by default, but takes a character to split by
print('My name is Simon'.split())
print('My name is Simon'.split('m'))


# .ljust() and .rjust() return padded version of the sting they are called on
# to left justify or right justify text by a certain number of whitespaces
# unitl filled (original characters included)
# optional second argument to speciify a fill character

print('Hello'.rjust(10))
print('Hello'.ljust(10))
print('Hello'.rjust(20,'*'))
print('Hello'.ljust(25,'-'))

# .center() has the same funcitons, for centering
print('Hello'.center(20))
print('Hello'.center(20,'='))
print('\n\n\n')


# .strip(), .rstrip(), .lstrip() removes excess characters from left, right,
# or both sides of the string, excluding the center
# optional argument to specify what characters to strip by (not in order
beans = 'strip whitespace'.rjust(50)
print(beans)
print(beans.strip())
print(beans.lstrip())
print(beans.rstrip())
print('SpamSpamBaconSpamEggsSpamSpam'.strip('ampS'))

# .replace() takes two arguments, one string to look for and one to replace it with
bowls = 'Hello there!'
print(bowls)
print(bowls.replace('e', 'tjioaARFE'))


# pyperclip .copy() and .paste()

##import pyperclip
##pyperclip.copy('Hello!!!!!!')
##pyperclip.paste()
