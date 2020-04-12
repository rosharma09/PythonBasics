# Global vs local variables in python

var1 = 40 # global variable

def method1():
    var1 = 32 # local variable
    print('the value of the local variable is :'+str(var1))


method1()
print('the value of global variable is :'+str(var1))

def test():
    value = 100
    print(value)

test()
#print(value) # local variables cannot be used in global scope

def test1():
    value1 = 100
    test2()
    print(value1)

def test2():
    value2 = 200
    print(value2)

test1()

val3 = 3000

def test3():
    global val3
    val3 = 'test'
    print(val3)

test3()


