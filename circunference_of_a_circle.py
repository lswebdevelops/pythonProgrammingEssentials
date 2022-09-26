"""
Compute the circumference of a circle, given the length of its radius.
"""


# The area of a circle is 2πr 
#  where r is the radius of the circle. Write a Python statement that calculates\
#  and prints the circumference in inches of a circle whose\
#  radius is 8 inches. Assume that the constant π=3.14.


###################################################
# Circle circumference formula
# Student should enter statement on the next line.
from math import radians


π = 3.14
radius = 8
area = 2 * π * radius 
print("The area of a circle with radius of", radius, "inches is =" , area, "square inches.")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#50.24