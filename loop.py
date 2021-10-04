# While and for 

# for loop
books = ['Winnie the Pooh','War and Peace', '1984', 'My family and other animals', 'Boy', 'Art of War', 'Of Mice and Men', 'Peter and Jane']

for bookItem in books:
    if bookItem == '1984':
        print(bookItem + " is the only book in the list that can be cast to int()")
    else:
        print(bookItem)

strVar = '01101010100'
for thisIsAVar in strVar:
    if int(thisIsAVar):
        print('This was False')
    else:
        print('The Truth!')

for numVar in range(100):
    print(numVar)

