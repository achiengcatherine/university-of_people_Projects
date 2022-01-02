def my_sqrt(a):   #define my_sqrt as a function
    epsilon = 0.0000001    #efine the value of epsilon
    x = a
    while True:
        y = (x + a/x) / 2.0
        if y == x:     #another way to check whether x and y are exactly equal, we can use {abs(y-x)< epsilon}.
            break
        x = y
    return y

print(my_sqrt(20))    #we call the function with a value to test if it works

import math           #we import math because we will need it to get the math.sqrt
def my_sqrt(a):
    epsilon = 0.0000001
    x = a
    while True:
        y = (x + a/x) / 2.0
        if abs(y-x)< epsilon:    #another way to check whether x and y are exactly equal.
            break
        x = y
    return y

def test_sqrt():       #define tes_sqrt as a new function
    a = 1              #the initial number is 1 not 0
    while a<26:        #the values will end with 25 number
        diff = my_sqrt(a) - math.sqrt(a)
        print('a =', a,'| my_sqrt(a) =',my_sqrt(a),'| math.sqrt(a) =', math.sqrt(a),'| diff =', abs(diff))
        a = a + 1
test_sqrt()    #call the function to print the results
