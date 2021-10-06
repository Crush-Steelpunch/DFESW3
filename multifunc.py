def add_two_to_two_numbers(num1In,num2In):
    out1Var = num1In + 2
    out2Var = num2In + 2
    outList = [ out1Var,out2Var]
    return outList

def calcuscore(hwIn,asmIn,feIn):
    perCent = round( ( ( hwIn + asmIn + feIn ) / 175 ) * 100 )
    # In this space grade scores between A-F
    return perCent

def leon_procedure(inputDataVar):
    print(inputDataVar)
    if inputDataVar < 5:
        exit()

def len():
    print('Len is the best')


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x):  
            if x % n == 0:
                return False
            return True