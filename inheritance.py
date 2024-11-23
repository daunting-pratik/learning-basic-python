class mammal:
    def walk(self):
        print("Walk")


class dog(mammal):
   
    def bark(self):
        print("Dog is barking")

class cat(mammal):
    pass


dogobj1=dog()
dogobj1.walk()
dogobj1.bark()

catobj1=cat()  
catobj1.walk()