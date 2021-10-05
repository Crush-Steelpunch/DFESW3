import pdb

pdb.set_trace()

def leon_procedure(inputDataVar):
    print(inputDataVar)
    if inputDataVar < 5:
        exit()



x = 1000
y = 2000
z = x * y
leon_procedure(z)
z = y - x
leon_procedure(z)
z = y * (x/2)
leon_procedure(z)
z = x * x
leon_procedure(z)
z = y * y
leon_procedure(z)