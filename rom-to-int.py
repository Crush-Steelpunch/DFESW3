

class Romtont():
    easynums = { 'M':1000,'D':500,'C':100,'L':50, 'X':10,'V':5,'I':1 }
    stupidnums = {'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'IV':4}

    def thecalcmethod(self,romnumin):
        runnintotal = 0
        for loopVar in self.stupidnums.keys():
            runnintotal = runnintotal + (romnumin.count(loopVar) * self.stupidnums[loopVar])
            romnumin = romnumin.replace(loopVar,'')

        for loopVar in self.easynums.keys():
            runnintotal = runnintotal + (romnumin.count(loopVar) * self.easynums[loopVar])
        return runnintotal
    def callthecal():
        self.thecalcmethod('X')
    

asterixthegaul = Romtont()

getafixthedrid = Romtont()
getafixthedrid.easynums = {}
getafixthedrid.callthecal()

print(asterixthegaul.thecalcmethod('DCCCLXXIV'))
print(asterixthegaul.thecalcmethod('MCMXCIV'))

obj1 = 'leon is a loon'

obj1.__getnewargs__()