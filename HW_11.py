class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def teach_tricks(self, tricks):
        self.tricks.__add__add(tricks)

    def do_tricks(self):
        print(f"{self.name}")
        for trick in self.tricks:
            print(trick)

class DogRex(Dog):
    def __init__(self,age):
        self.age = age 

        self.tricks = []
        self.teach_tricks('sit')
        self.teach_tricks('stay')
        self.teach_tricks('come')






    