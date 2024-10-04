# Make a program that takes a value (x) and returns "Bang" if the number is divisible by 3, "Boom" if it is divisible by 5,
# "BangBoom" if it divisible by 3and 5, and "Miss" if it isn't divisible by any of them.
# Note: Your program should only return one value
# Ex: Input: 105 --> Output: "BangBoom" Ex: Input: 9 --> Output: "Bang" Ex:Input: 25 --> Output: "Boom"

import random

def multiple(x):

    answer = 'Test'
    print(str(x) + ' % 3 = ' + str(x % 3),'\n', str(x) + ' % 3 = ' + str(x % 5))

    # The most specific case should be the first case of an if-statement, otherwise, the program may run without the case ever
    # being checked, therby returning an incorrect answer
    if x % 3 == 0 and x % 5 == 0:
        answer = 'BangBoom'
    elif x % 3 == 0:
        answer = 'Bang'
    elif x % 5 == 0:
        answer = 'Boom'
    else:
        answer = 'Miss'
    return answer

print(multiple(30))
print(multiple(3))
print(multiple(98))
print(multiple(65))
