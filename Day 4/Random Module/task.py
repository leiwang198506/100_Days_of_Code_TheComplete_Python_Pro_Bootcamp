import random

# https://docs.python.org/3/library/random.html
# #random.randint is a function to give random integer numbers
# random.randint(a, b) # Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
random_integer= random.randint(1,10)
print(random_integer)
# use my own module
import my_module
print(my_module.my_favourite_number)

import random
import random floating numbers, 0<=number<1
random.random()
Return the next random floating-point number in the range 0.0 <= X < 1.0
random_number_0_to_1=random.random()
print(random_number_0_to_1)
#
between 0 and 10
# random_number_0_to_1=random.random()*10
# print(random_number_0_to_1)

## random.uniform(a,b): return a random floating number a<=N<=b,
## end-point value b may not be included in the range
random_float= random.uniform(1,10)
print(random_float)


#print out heads or tails
import random
result= random.randint(0,1)
if result == 0:
    print("Heads!")
else:
    print("Tails!")