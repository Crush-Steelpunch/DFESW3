inputNamesList = []
numVar = 5
while numVar > 0:
    inputNameVar = input('Type IN: ')
    inputNamesList.append(inputNameVar)
    numVar = numVar - 1

for inName in inputNamesList:
    print(inName + ' is awesome')
