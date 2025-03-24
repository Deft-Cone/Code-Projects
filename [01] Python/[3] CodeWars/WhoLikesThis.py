def likes(names):
    n = len(names)
    
    if n == 0:
        return '"No one likes this"'
    elif n == 1:
        return f"{names[0]} likes this"
    elif n == 2:
        return f"{names[0]}, and {names[1]} like this"
    elif n == 3:
        return f"{names[0]}, {names[1]}, and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]}, and {n-2} others like this"

# Best Practice
def likes(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.
    
    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4
    
    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others = length - 2)

result = likes([])
print(result)
result = likes(['Peter'])
print(result)
result =likes(['Jacob', 'Alex'])
print(result)
result =likes(['Max', 'John', 'Mark'])
print(result)
result = likes(['Alex', 'Jacob', 'Mark', 'Max'])
print(result)

