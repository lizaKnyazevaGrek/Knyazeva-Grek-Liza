class DogRex:
    def __init__(self):
        self.name = 'DogRex'
        self.voice = 'woof-woof'
        self.hungry = False

    def feed(self):
        self.hugry= True
    def walk(self):
        self.hungry = False 


my_dog = DogRex()

print('my dog name:', my_dog.name)
print('my dog voice:', my_dog.voice)
print('my dog is not hungry:', my_dog.hungry)
my_dog.feed()
print('my dog is not hungry:', my_dog.hungry)
my_dog.walk()
print('my dog is not hngry:', my_dog.hungry)