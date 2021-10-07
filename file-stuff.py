# Open, read out and close the file

openedfile = open('README.md')
listObject1 = openedfile.readlines()
openedfile.close()

# manipulate contents
print(listObject1)

singleline = listObject1.pop(4)
singleline = singleline.replace(' a ',' all ')
listObject1.insert(4,singleline)
print(listObject1)

bigstr = ''
for i in listObject1:
    bigstr  = bigstr + i


# Open in write mode, write and close

openedfile = open('stuff/README.md','x')
openedfile.write(bigstr)
openedfile.close()
