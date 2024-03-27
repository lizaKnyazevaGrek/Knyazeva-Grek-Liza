class Dog:
   name = 'unknown'
   
   def __init__(self, breed, speed):
      self.is_walked = False 
      self.speed = speed
      self.breed = breed
      selh.tricks = []
            
   def walked(self):
      print('Dog walked')
      self.is_walked = True

    def learn_tricks(self) 

class DogSpike(Dog):
   name = 'Spike'
   def run(self): 
      print(f'dog {self.name is running {self.speed} km/h and is hungry')

class DogMike(Dog):
   name = 'Mike'
def run(self):
   print(f'dog {self.name} is running {self.speed} km/h and is thirsty')

my_dog = DogSpike('bulldog', 12)
friends_dog = DogMike('pitbul', 20)
print (f'my do name is {my_dog.name}')
print (f'my dog speed is {my_dog.speed} km/h')



#print('my dog name:', my_dog.name)
# print(my_dog.is_walked)
# my_dog.walk()
#print('friends dog name;', friends_dog.name)
