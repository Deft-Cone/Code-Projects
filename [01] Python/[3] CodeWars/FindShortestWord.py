# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def len_sort(x):
    return len(x)

def find_short(s):
    words = s.split()
    print(words)
    words.sort(key=len_sort)
    print(words)
    l = len(words[0])
    return l

# Best Practice
def find_short(s):
    return len(min(s.split(' '), key=len))

find_short("bitcoin take over the world maybe who knows perhaps")
find_short('turns out random test cases are easier than writing out basic ones')
find_short("lets talk about javascript the best language")
