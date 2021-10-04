nameVar1 = "Brian"
listOfAnimals = ['sheep', 'elephant', 'rat', 'pig', 'llama' ,'Austrian tree frog','Pacific river mole']
varForADictionary = { 'name':'Leon' , 'size':'nearly big', 'age':'I am still young' }

#if not (nameVar1 != 'Brian' or not 'Leon' in varForADictionary.values()):
#    print('Leon is in the list of values')
#print('This line will always print')


#AND                       OR 
#1    t   f   t   f        t   t    f   f
#2    t   t   f   f        t   f    t   f
#out  t   f   f   f        t   t    t   f

if 'goat' in listOfAnimals:
    print('found a goat')
elif 'penguin' in listOfAnimals:
    print('found a penguin')
elif 'aardark' in listOfAnimals:
    print('found an aardvark')
elif 'dog' in listOfAnimals:
    print('found a dog')
else:
    print('found something weird')





