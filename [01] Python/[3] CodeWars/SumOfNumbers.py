#Given two integers a and b, which can be positive or negative, find the sum of all the integers between and
# including them and return it. If the two numbers are equal return a or b.

#Note: a and b are not ordered!

# This method results in a memory error at large integer values
##def get_sum(a,b):
##    
##    # if two numbers are equal return a
##    if a == b:
##        return a
##    else:
##        # order a and b
##        numList = []
##        numSet = sorted([a,b])
##        print(numSet)
##        # define range and find all integers between a and b
##        for i in range(numSet[0], numSet[1] + 1):
##            numList.append(i)
##        print(numList)
##        # sum all numbers in set
##        print(sum(numList))
##        return sum(numList)
##    
##get_sum(10,-100)

def get_sum(a, b):
    if a == b:
        return a
    else:
        # order a and b
        start, end = min(a, b), max(a, b)
        print(start, end, sep=', ')
        # find sum of range of integers between a and b
        print(sum(range(start, end + 1)))
        return sum(range(start, end + 1))

get_sum(10,-100)
