# program to illustrate infinite loops:

while True:
    print('Enter your name')
    name = input()
    if name == 'Rohan':
        break
print('Welcome' + name)

# use of continue statement 

val = 0

while val <= 10:
    val = val + 1
    if val % 2 == 0 and val != 1: 
        print(str(val) + ' is even')
        continue
print('End of while loop')
