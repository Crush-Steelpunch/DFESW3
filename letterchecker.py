
class Letterchecker():
    vowels = 'aeiou'

    def checkthing(self,x):
        return x in self.vowels


vowlchecker = Letterchecker()

print(vowlchecker.checkthing('f'))