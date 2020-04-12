# program to illustrate the for loop

name = 'Rohan'

print('For loop start')

for i in range(5):
    print(str(i) + '--> my name is ' +name)

print('For loop end')

# equivalent while loop for the above for loop

print('while loop start')

i=0
while i < 5:
    print(str(i) + '--> my name is ' +name)
    i = i + 1
print('while loop end')

sum = 0

print('please enter the number till which you want to find the sum')
num = input()

for i in range(int(num)+1):
    sum = sum + i
print('The sum of all the numbers till ' +str(num)+ " is " + str(sum))

# while loop

total = 0 

print('Please enter the value of N:')
N = input()
I = 0
while I <= int(N):
    total = total + I
    I = I + 1
print(I) 