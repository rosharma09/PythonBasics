# This program to illustrate If Else statements

myName = 'Rohan'
myPet = 'dog'

if myName == 'Rohan' and myPet == 'dog':
    print('Hello Rohan you need to buy dog food')
print('Done')

# below is an example for if else 

username = 'rosharma'
password = 'qwerty'

if username == 'rosharm' and password == 'qwerty':
    print('Access granted')
else: 
    print('Access denied')

# program to illustrate elif

user = 'testuser1'
age = 101

if user == 'testuser':
    print('welcome to python')
elif age < 18:
    print('You are not eligible to enter the website')
elif age >= 18 and age < 100: 
    print('Welcome to the website')
else:
    print('Are you seriously alive')
print('please let me know what to do: ')

print('Enter a name')
name = input()

if name != '': 
    print('Thank you for entering a name')
    print('User enterd name is: ' +name)
else: 
    print('No name entered by the user')