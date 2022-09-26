# two point (x0,y0) and (x1,y2) is ((x0 - x1)^2 +  (y0 - y1)^2) ^ 1/2

# Write a Python statement that calculates and prints the distance between the points
# (2,2) and (5,6)

"""
Template - Compute the distance between the points (x0, y0) and (x1, y1).
"""

###################################################
# Distance formula
# Student should enter statement on the next line.

# Hint: You need to use the power operation ** .


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#5.0


x0 = 2
x1 = 5
y0 = 2
y1 = 6

distance_two_points = (((x0 - x1)**2) +  ((y0 - y1)**2)) ** 0.5
print('The distance between (x0 - y0) being (2,2) and  (x1 - y1) being   (5,6) is : ', distance_two_points)