from abc import ABC, abstractmethod

class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False

#Now we are going to create the first subclass.

class Owl(Bird):

    def reproduce(self):
        self.babies += 6

    def eat(self):
        return "Peck peck"

#So we have used Polymorphism to override the reproduce method, Abstraction with the eat method and Inheritance in this child class.
#Now we will add another subclass.

class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        return "Nom nom"

    def reproduce(self):
        if not self.extinct:
            self.babies += 1

class Penguin(Bird):

    def eat(self):
        return "The Fish"
    
    def reproduce(self):
        if not self.extinct:
            self.babies += 20
            return self.babies


johnTheDodo = Dodo()
fredTheDodo = Dodo()

johnTheDodo.extinct = False
print(fredTheDodo.extinct)
johnTheDodo.reproduce()

trevthePenguin = Penguin()
print(trevthePenguin.reproduce())

wolTheOwl = Owl()

johnTheDodo.eat()

print(wolTheOwl.noise())


