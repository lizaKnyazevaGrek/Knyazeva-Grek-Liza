class DogSpike:
   name = 'Spike'
   
   def __init__(self):
      self.is_walked = False 
      
   def walked(self):
      print('Dog walked')
      self.is_walked = True 
    
my_dog = DogSpike()

print(my_dog.name)
print(my_dog.is_walked)
# my_dog.walk()