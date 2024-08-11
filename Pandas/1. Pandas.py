import pandas as pd 
'''Pandas is a library that is used to sort your data like presenting you list in form of tables and giving names to index of you dictionary and all'''
def series(): #displays data in tables and displays datatype of you data
    dict = {"A": "apple",
            "B": "Ball",
            "C": "Cat"}
    list = ["Apple", "Banana", "Cambridge"]
    df = pd.Series(dict)
    print(df,"\n")
    df = pd.Series(list)
    print(df,"\n")
    df = pd.Series(data=list, index=["A","B","C"])
    print(df,"\n")
    print(df[0])
    print(df["B"])
    calories = {"day1": 420, "day2": 380, "day3": 390}
    myvar = pd.Series(calories, index = ["day1", "day2"])
    print(myvar)
    # print(myvar["day3"]) Error

    
series()