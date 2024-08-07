#try, except, raise;
'''try - tries a code block 
   except - used after try if try is failed except is executed
   else - it is executed when all try statement are executed otherwise it's not executed
   finally - it is executed regardless of try or except
   raise - it is used to raise an err'''
x = 2334

try:
    print(x)
except NameError: 
    print("NameError")
except:
    print("Some error")
else: #else is used before finally
    print("all blocks are exected")
finally:
    print("we have tried printing x")

#The try block will raise an error when trying to write to a read-only file:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  

x = 23

if x < 0:
  raise Exception("Sorry, no numbers below zero")

if type(x) is int:
   raise TypeError("integer is not allowed")

