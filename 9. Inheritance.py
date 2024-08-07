'''With help of inheritance we can inherit the properties of the parent class to the children class'''
class person:#Parent class
    def __init__(self, f_name, l_name):
        self.firstname = f_name
        self.lastname = l_name
    def printname(self):
        print(self.firstname, self.lastname)
class Student(person):#child class
    pass
#Now the Student have the same properties as the class person have.

x = Student("Mike","Olsen")
x.printname()

#adding __init__ in child class 
# if we add __init__ in child class the child class will no longer inherit the properties of the parent class 
# But to keep inheritance of the parents __init__ function call the parent init function in child's init function 

class Student1(person):
    def __init__(self, f_name, l_name):
        person.__init__(self, f_name, l_name)
x = Student1("Mike","Olsen")
x.printname()

class Student2(person):#Super function inherits all the methods and properties of parent class to child class.
    def __init__(self, f_name, l_name,year):
        super().__init__(f_name, l_name)
        self.graduationyear = year
    def Welcome(self):
        print(f"\nyou are {self.firstname} {self.lastname}\nyou will be graduated in {self.graduationyear}")
    
x = Student2("Mike","Olsen",2029)
x.Welcome()
    
