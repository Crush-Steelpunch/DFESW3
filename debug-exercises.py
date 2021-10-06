# Exercise 2

#def product(n):
#    total = 1
#    for i in n:
#        total *= i
#    return total

#print(product([4,4,5]))

# Exercise 3

import pdb

pdb.set_trace()

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x):  
            if x % n == 0:
                return False
        return True

returnVar = is_prime(4)
print(returnVar)


# x == 3 range(2,x+1)  range(2,4)  2 
# x == 4 range(2,x+1)  range(2,5)  2 3 
# x == 5 range(2,6)    2 3 4 
# x == 6  range(2,7)   2 3 4 5 


