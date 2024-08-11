'''Lambda is an small anonymous function in python

Syntax--> lambda arguments: expression '''

def power(a):
    return lambda n: a * n
print(power(23)(5))


#the length of an array is always one more then the highest index of the array 
