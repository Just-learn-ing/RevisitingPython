#In functions if we do not know about number of arguments add * before the parameter to pass a tuple
def asterisk(*kids):
    print("the third kid is", kids[2])
kid = ["navneet","trimude","golden","umang"]
asterisk(*kid)


#convention is you have to place normal arguments first the args then kwargs like 
#def function(normal, *args, **kwargs)    otherwise error



def default_parameter(country = "India"):
    print(f"I am from {country}")
default_parameter("Brazil")
default_parameter()

"Function definition cannot be empty but for some reason if you have to leave the func definition empty you can use pass statement"
def This_is_empty():
    pass

"Positional only argument, Use ,/ after all parameter to make the fuction positional only"
"Keyword only argument: Use (*, argument...)  to make a function key word only calling function with position will throw an error in this case "


def combine_positionalonly_keywordonly_argument(a, b, /, *, c , d):
    print(a, b, c, d)
combine_positionalonly_keywordonly_argument("ramesh","suresh", c = "mahesh", d = "dhunesh")
# combine_positionalonly_keywordonly_argument(a = "ramesh","suresh", "mahesh", d = "dhunesh")   thrws an err
