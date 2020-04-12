# python gives a number of inbuilt function and standard libraries 
# to use the functions under the standard libraries we need to import the module

# for Ex: randint() method is in random module

import random

randomNumber = random.randint(20,30)
print(randomNumber)

# we can import multiple module in one 

# import random , sys , os , math 

# another way to import the module is : from random import *

import sys

print('statement before the exit statement')

sys.exit()

print('statement after the exit statement')

import pyperclip

pyperclip.copy('hello world')
pyperclip.paste()