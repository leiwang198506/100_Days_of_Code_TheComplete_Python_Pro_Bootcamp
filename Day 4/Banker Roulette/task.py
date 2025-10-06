#who will pay the bill using random and list
#method 1: way too complicated
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
payer =random.randint(0,4)
if payer==0:
    print(friends[0])
elif payer ==1:
    print(friends[1])
elif payer == 2:
    print(friends[2])
elif payer == 3:
    print(friends[3])
else:
    print(friends[4])

# method 2
#easier way using random.choice()
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))

#method 3
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
payer =random.randint(0,4)
print(friends[payer])
