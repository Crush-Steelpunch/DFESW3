## While and for 
#
## for loop
books = ['Winnie the Pooh','War and Peace', '1984', 'My family and other animals', 'Boy', 'Art of War', 'Of Mice and Men', 'Peter and Jane']

for bookItem in books:
    if bookItem == '1984':
        continue
    print(bookItem)

 strVar = '01101010100'
 for thisIsAVar in strVar:
    if int(thisIsAVar):
        print('This was False')
    else:
        print('The Truth!')


 for numVar in range(100):
    print(numVar)

#


varForADictionary = { 'name':'Leon' , 'size':'nearly big', 'age':'I am still young' }

for thingsVar in varForADictionary.keys():
    print("The key is " + thingsVar + ", The value is: "+ varForADictionary[thingsVar])



# While 




inputNumVar = int(input('Shove a whole number in: '))
resultVar = 1
while inputNumVar > 0:
    resultVar = resultVar * inputNumVar
    inputNumVar = inputNumVar - 1

print(resultVar)
