def is_divisible(x,y):   # is_division function from section 6.4 of textbook

    if x % y == 0:
       return True

    else:
        return False

def is_power(m,n):     # is_power function that takes two arguments

    if not is_divisible(m,n):   # is_power function calls is_divisible
        return False

    if n==m:            # is_power function include code of the base case of the two arguments being equal
        return True

    elif n==1:            # is_power function include code of the base case of the second argument being "1"
        return False

    return is_power(m/n,n)  # is_power function call itself recursively

print ("is_power(10,2) returns: ", is_power(10,2))
print ("is_power(27,3) returns: ", is_power(27,3))
print ("is_power(1,1) returns: ", is_power(1,1))
print ("is_power(10,1) returns: ", is_power(10,1))
print ("is_power(3,3) returns: ", is_power(3,3))
