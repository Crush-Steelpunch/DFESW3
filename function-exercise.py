# The program should take the students name, 
# homework score (/25), assessment score (/50)
# and final exam score (/100) as inputs,
# and output their name and final ICT grade as a percentage.

# Convention, input() and print() shouldn't be in a function
def calcuscore(hwIn,asmIn,feIn):
    perCent = round( ( ( hwIn + asmIn + feIn ) / 175 ) * 100 )
    # In this space grade scores between A-F
    return perCent

hwScore = 200
asmScore = 200
feScore = 200

studentName = input('NAME IN: ')
while hwScore > 25:
    hwScore = int(input('HW IN: '))
while asmScore > 50
    asmScore = int(input('ASM IN: '))
while feScore > 100:
    feScore = int(input('FES IN: '))

outVar = calcuscore(hwScore,asmScore,feScore)

print(f"Yo {studentName} {outVar}%")