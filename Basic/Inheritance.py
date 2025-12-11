class Mammal:
     def walk(self):
        print('walk')



class Dog(Mammal):
    def brak(self):
        print("bark")
   

class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


class Cow(Mammal):
    pass


dog1 = Dog()
dog1.walk()
dog1.brak()

cat1 = Cat()
cat1.walk()
cat1.be_annoying()

cow1 =Cow()
cow1.walk()