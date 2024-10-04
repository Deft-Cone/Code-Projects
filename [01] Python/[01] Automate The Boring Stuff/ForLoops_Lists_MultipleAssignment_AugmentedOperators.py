for i in range(4):
    print(i)

supplies = ['pens', 'staples', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

cat = ['fat', 'orange', 'loud']

size, color, disposition = cat
size
color
disposition

size, color, disposition = 'skinny' , 'black', 'quiet'
