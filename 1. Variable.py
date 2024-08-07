def MultipleValues(): #Multiple values assinging to different variable on same time
    '''You can assing mutiple variable at a single time'''
    x, y, z = "mango", 899, [7,3,2,"2343"]

    print(x)
    print(y)
    print(z)

def SameValue(): #Same values to different variables at a single time
    
    '''One value to multiple variables'''
    a = b = c = "Same value"
    print(a)
    print(b)
    print(c)

def Unpacking_A_List(): #Unpacking a list using variables

    fruits = ["apple", "Banana", "Cherry", "Mango"]
    a, b, c, d = fruits
    print(a)
    print(b)
    print(c)
    print(d)

def Global(): #Gobal variables 
    '''You can create global variable in python by just writing it at the top outside of every function and you can also create a global variable
    inside a function using lobal keyword simply or u can use global keyword to change global variable'''
    # global glob_var = 899        This is a wrong syntax
    global glob_var
    glob_var = 899

def Nonlocal(): #nonlocal variable
    def myfunc():
        x = 300
        def myinnerfunc():
            nonlocal x
            x = "The value has been assigned to variable outside the function"
        myinnerfunc()
        print(x)
    myfunc()
Nonlocal()









# Global() #calling the function to initialize global variable first otherwise it will generate NameError due to being undefined
# print (glob_var)