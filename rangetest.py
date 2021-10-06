import random

def roll(D,Times):
    rollList = []
    for i in range(Times):
        rollList.append(random.randint(1,D))
    return rollList
beep = roll(20,6)
for oot in beep: 
    print(oot)o
