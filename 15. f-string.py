"F strings allows you to format selected parts of a string"
price = 9000000000
fruits = "apples"
print(f"price is {price} dollars")
print(f"price upto two decimals is {price:.2f}")     #:.2f is a modifier
print(f"price in commas are {price:,}")              #, is modifier for the price
#you can perform operations in a f-string
#perform if else in the string
print(f"price is very {"expensive" if price > 40000 else "cheap"}")
print(f"I lovee to eat {fruits.upper()}")
print(f"      {price:<}")




quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))



age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))



myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))