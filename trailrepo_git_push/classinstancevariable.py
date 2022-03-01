#class for dog
class Dog:
    #class variable
    animal='dog'

    #init method
    def __init__(self,breed,color):
        
    #intananiou method
        self.breed=breed
        self.color=color

#object of dog class

Rodger=Dog("pug","brown")
Buzo=Dog("Bulldog","black")

print('dog details')
print('rodger is a ',Rodger.animal)
print('breed ',Rodger.breed)
print('color of rod',Rodger.color)

print('buzo details')
print('buzo bree',Buzo.breed)
print('buzo color',Buzo.color)