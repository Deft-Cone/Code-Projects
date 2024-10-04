# you are given a number and have to make it negative. But maybe the number is already negative?

def makeNegative(number):
    return -abs(number)


print(makeNegative(-42))
print(makeNegative(42))
print(makeNegative(-9))
print(makeNegative(9))

