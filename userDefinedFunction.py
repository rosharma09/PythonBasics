# python provide a number of inbuilt functions like -- > input() print() len()
# we can create our own functions

def printText():
    print('hello welcome to python tutorial')
    print('this is just a sample method')

printText()

def printName(name):
    print('Hello '+name+' how are you?')

printName('Rohan')
printName('testuser')

# create some sample methods:

# define a function to find whether the given nummber is palindrome: 

print('hello has '+str(len('hello'))+' letters in it')

def increment(number):
    return number + 1

incrementNumber = increment(10)
print(incrementNumber)

# by default the print() function puts a \n new line at the end of the string it displayed
print('hello')
print('world')

# we can change the end of the string as below:

print('hello' , end = ' ')
print('world')

print('hello' , 'world' , 'in a single line')
print('dog','cat','mouse',sep='-->')