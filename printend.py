listVar = ['violin','viola','cello','crumhorn','harp','flute','drums','triangle']
listVar2 = '0101011110101010'

inVar = int(input('Num in: '))
answerVar = 1
for tempVar in range(inVar):
    answerVar = answerVar * inVar
    inVar = inVar - 1

print(answerVar)

