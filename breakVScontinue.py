# this program to illustrate the use of break and continue keyword in python

val = 0

while val < 10: 
   
    if val == 5:
        break
    print('loop execution:' + str(val))
    val = val + 1

val = 0

while val < 10:
    val = val + 1
    if val == 5:
        continue
    print('loop execution:' +str(val))


