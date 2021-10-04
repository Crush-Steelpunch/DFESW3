palinVar = input('TYPE IN: ')

numChars = len(palinVar) - 1
raVnilap = ''

while numChars >= 0:
    raVnilap = raVnilap  + palinVar[numChars]
    numChars = numChars - 1

if raVnilap == palinVar:
    print('PALINDROME')
else:
    print('no')