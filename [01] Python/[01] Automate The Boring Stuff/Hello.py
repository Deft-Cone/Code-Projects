# This program says hello and asks for my name

print('Hello')
print('What is your name?') # ask for name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') # ask for age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')
