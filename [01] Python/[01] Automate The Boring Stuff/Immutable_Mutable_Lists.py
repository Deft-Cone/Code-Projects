import copy

spam = [1, 2, 3]

# python uses mutable values as references to a place in memory
# methods like .append that modify mutable values "in place" actually modify the original value that is being referenced

def eggs(spam):
    cheese.append('Hello')

# To prevent bugs, you need to make a copy of the referenced vaue in memory so you aren't mistakenly editing the same momory slot
# with two different references
def newCopy(spam):
    cheese = copy.deepcopy(spam)
    cheese.append('Hello Again')
    return cheese

eggs(spam)
newSpam = newCopy(spam)
print('spam is ' + str(spam))
print('newSpam is ' + str(newSpam))
