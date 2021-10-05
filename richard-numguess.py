import random

Randomnumber = random.randint(1,9)
Guess = 0
while Guess != Randomnumber:
    Guess = int(input('guess'))
    if Guess == Randomnumber:
        print('\\0/')
    else:
        print('nah')
# Alternative
checkInt = True
while checkInt:
    Guess = int(input('guess'))
    if Guess == Randomnumber:
        print('\\0/')
        checkInt = False
    else:
        print('nah')
