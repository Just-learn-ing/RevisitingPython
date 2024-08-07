"A class is a object instructor like a blueprint for making a object"

#create a class Myclass with a property x
class Myclass:
    myroll = 5
    myname = "Balkrishan"
    mystandard = "9th"

class Myclass1: #class with __str__
    def __init__(self, naaam, standard, rollno):
        self.name = naaam       #self.name --> property kehte hai ise
        self.standard = standard
        self.roll = rollno     #self apne aap hi paas ho jata like agar c = Myclass1(name, stan, roll) pass kiya to self ke taur par "c" apne aap paas ho jayega
    
    def method_kehte_hai_ise(self):
        print(f"I am {self.name}. My roll no is {self.roll}. And I study in class {self.standard}")

    def __str__(self):
        return f"I am {self.name}. My roll no is {self.roll}. And I study in class {self.standard}"
    #__str__ method controls what will be printed 
        
class Myclass2: #class without __str__
    def __init__(self, naaam, standard, rollno):
        self.name = naaam       #self.name --> property kehte hai ise
        self.standard = standard
        self.roll = rollno     #self apne aap hi paas ho jata like agar c = Myclass1(name, stan, roll) pass kiya to self ke taur par "c" apne aap paas ho jayega
    
    def method_kehte_hai_ise(self):
        print(f"I am {self.name}. My roll no is {self.roll}. And I study in class {self.standard}")
#the first parameter of any method in class is resevered for what we call it self, whatever name you give to it, but the 
#the first position will always be reserved by the self.



p2 = Myclass1("Balkrishan", "8th", 3) 
p3 = Myclass2("Balkrishan", "8th", 3) 
print(p2)
print(p3)


    

# #access class items
# p1 = Myclass()  #creating object here p1 is an object
# print(f"I am {p1.myname}. My roll no is {p1.myroll}. And I study in class {p1.mystandard}")
# print(f"I am {p2.name}. My roll no is {p2.roll}. And I study in class {p2.standard}")
