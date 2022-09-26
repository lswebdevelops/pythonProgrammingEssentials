# The perimeter of a rectangle is 2w + 2h, where w and h are the lengths of its sides. Write a Python statement that calculates\
#  and prints the length in inches of the perimeter of a rectangle with sides of length 4 and 7 inches. 

from turtle import heading, width


print("rectangle:")
print(" _________W______ ")
print("|                |")
print("|                |")
print("|                |")
print("h                h")
print("|                |")
print("|                |")
print("|                |")
print("|________W_______|")

print("Perimeters = w * 2 + h * 2")

width = 4
height = 7

perimeter = (2*width) + (2*height)

print('The perimeter of a rectangle of width=', width , "and height =", height, "is :" , perimeter)
