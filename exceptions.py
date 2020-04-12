# how to handle exceptions in pyhton:

def divideFunction(num1 , num2):
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        print('Error : you tried to divide the number by zero')
   
res = divideFunction(10 , 0)

print(res)

print('Please enter a number:')

num = input()
try:
    if int(num) >=100:
        print('the number is creater than 100.')
    else: 
        print('the number is smalled than 100.')
except ValueError:
    print('Error : User did not enter a numeric value')
    
