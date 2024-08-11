'''To create a module you just need to save a file with .py exxtension'''
import MyModule as mm
x = dir(mm) #dir function can be used with any module to determine all the function the module have
print(x)


mm.Welcome("Balkrishan")
#when using a module use the syntax moduleName.ModuleFuction(arguments)
print(mm.person1["age"])

# You can also import specific functions we want to import

'''# from MyModule import Welcome 
# print(Welcome("balkrishan"))'''

#IMPORTANT: when using from keyword do not use the module name and function name, just only use function name 
