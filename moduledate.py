"""
Demonstration of some of the features of the datetime module.
"""
import datetime
from doctest import testfile

date2 = datetime.date(1233,3,31)

print(date2)
today = datetime.date.today()
print(today)
date1 = datetime.date(2022, 6, 28)

# COmpare dates

print("Comparing Dates")
print("*///////////////////////////*")
print(today > date2)

print(today == date2)

print( date1 >= date2)

# subtracting dates

print("subtraction dates")

print("/*********/")

diff = date2 - date1

print (diff)

print(diff.days)

diff2 = today - date1

print (diff2)

print(diff2.days)



# how to extract the year, day and month of a date> 
date3= datetime.date(2016, 1, 7)

print(date3)
print(date3.year)
print(date3.month)
print(date3.day)

print("Today's year is:",today.year)
print("Today's month is:",today.month)
print("Today's day is:",today.day)
print("Today is:",today)

# a data in portugues: just for fun
print("Hoje é:", today.day, "de", today.month, "do",today.year,".")

difference = date1 - today

print("The difference ",difference.days)