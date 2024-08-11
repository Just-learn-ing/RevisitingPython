import os

'''open() function takes two parameters first is file name and second is file mode
four different modes of opening a file in python:
"r" - read
"a" - append
"w" - write  
"x" - create
additionaly there are two modes whether file should be handled in binary to text
"t" - text
"b" - binary usage = "rt" - read text
                   = "rb" - read binary   '''

try:
    with open("demofile.txt","x") as f:
        pass
except:
    os.remove("demofile.txt")
f = open("demofile.txt", "w") #using "w" again will overwrite the files
f.write("how are you")
f.close()
f = open("demofile.txt", "a")
f.write("now the file has somemore content")
f.close()
f = open("demofile.txt", "r")
b = f.read(1)
print(b)

#to delete a file we must have to import os file first of all
os.remove("demofile.txt")

