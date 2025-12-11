class Person:
    def __init__(self,name):
        self.name =name
        
    def talk(self):
        print(f"Hi, I am {self.name}")


maruf = Person("Maruf Ahammed")
print(maruf.name)
maruf.talk()

print('..................')

bob = Person("Bob Smith")
print(bob.name)
bob.talk()