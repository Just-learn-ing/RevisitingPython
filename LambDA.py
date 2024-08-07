'''Lambda is an small anonymous function in python

Syntax--> lambda arguments: expression '''

def power(a):
    return lambda n: a * n
print(power(23)(5))