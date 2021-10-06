class Dog:
#    breed = 'Corgi'
#    hight = 16
#    energy = 'medium'
    catagory = 'mammal'
#
    def __init__(self, breed, height, energy = 'low'):
        self.breed = breed
        self.height = height
        self.energy = energy

    def speak(self):
        print('yap')
    
    def whatami(self):
        print(self.breed)

    def add_two(self,intIn):
        return intIn + 2

    def iliketobark(self):
        for i in range(3):
            self.speak()
    


bilbo_waggins = Dog('Corgi',16,'medium')

chewbarka = Dog('Spaniel',1)



print(chewbarka.energy)


havoc = Dog('Cavapoo',1.5,'ultimate')
print(havoc.add_two(2))

#print(bilbo_waggins.breed)
#print(chewbarka.breed)



#class cloud_login():
#    username = 'admin'
#    password = 'password123'
#    auth_url = 'https://thecloud.cloud'
#
#    def login(self,username,password,auth_url):
#        # some code
#
#q
#prodcloud = cloud_login()
#
#prodcloud.username = 'admin_leon'
#prodcloud.password = 'leon_password123'
#
#testcloud = cloud_login()
#testcloud.username = 'test_leon'
#testcloud.password = 'test_pass123'
#
#testcloud.login()
#prodcloud.login()
#
#

