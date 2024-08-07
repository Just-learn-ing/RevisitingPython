import datetime as dt, math
x = dt.datetime.now()     #created a date/time object
print(x) #date contains year month day hours minutes second and microsecond
print(x.strftime("%A")) #prints day
y = dt.datetime(2006, 10, 9) # y = dt.datetime(2006, 10, 09) --> this code throws and err so don't put a zero before date
print(y.strftime("%A"))    #created a date/time object












"python math function-- builtin math functions"
'''min() - returns minimum in a function
   max() - returns maximum in a function
   abs() - returns absolute value(mod value) in a function
   pow(4,3)- 4 to the power 3

python builtin math module function -- usage math.func()
    sqrt(x) - print square root of x
    ceil(1.2) - rounds to the nearest upward integer
    floor(1.2) - rounds to the nearest downward integer
    pi()       - returns value of pi
    
   '''
a = [1,2,3,4,5,6,7,8,9,0,-343]
print(min(a),"\n",max(a))