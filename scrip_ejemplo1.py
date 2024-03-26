
import pandas as pd

week1 =  pd.read_csv("Restaurant - Week 1 Sales.csv")
week2 =  pd.read_csv("Restaurant - Week 2 Sales.csv")

mask1 = week1["Customer ID"] ==304
a= week1[mask1]


mask2 = week2 ["Customer ID"] ==304
b=week2 [mask2]

print( a )

print (b)