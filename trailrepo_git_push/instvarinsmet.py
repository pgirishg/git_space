class Dog:

    animal='dog'
    
    def __init__(self,breed):
        self.breed=breed

    def setcolour(self,colour):
        self.color=colour

    def getcolour(self):
        return self.color

#driver code
Rodger=Dog("pug")
Rodger.setcolour('brown')
print(Rodger.getcolour())

