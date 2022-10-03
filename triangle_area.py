"""
Template - Compute the area of a triangle (using Heron's formula),
    given its side lengths.
"""

###################################################
# Triangle area (Heron's) formula
# Student should enter function on the next lines.
# Hint:  Use point_distance as a helper function.

# Heron's formula states that the area of a triangle whose sides have lengths a, b, and c is
###################################################
# coordenates:
x_0, y_0 = 2, 2
x_1, y_1 = 5, 6
x_2, y_2 = 7, 2

def point_distance_a_to_b(x_0, y_0, x_1, y_1):
    """
    Returns the Euclidian distance between two points (x0,y0) and (x1,y1).
    """
    
    return ((x_0 - x_1) ** 2 + (y_0 - y_1) ** 2) ** 0.5
print("distance from a to b")
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance_a_to_b(x_0, y_0, x_1, y_1)) + " cm.")

# distance x1 > x2
def point_distance_b_to_c(x_1, y_1, x_2, y_2):
    """
    Returns the Euclidian distance between two points (x_1, y_1 and (x_2, y_2).
    """
    
    return ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5
print("distance from b to c")
print("The distance from (" + str(x_1) + ", " + str(y_1) + ") to (" + 
      str(x_2) + ", " + str(y_2) + ") is " + str(point_distance_b_to_c(x_1, y_1, x_2, y_2)) + " cm.")



# distance x2 > x0
def point_distance_c_to_a(x_2, y_2, x_0, y_0):
    """
    Returns the Euclidian distance between two points (x_2, y_2) and (x_0, y_0).
    """
    
    return ((x_2 - x_0) ** 2 + (y_2 - y_0) ** 2) ** 0.5

print("distance from c to a")
print("The distance from (" + str(x_2) + ", " + str(y_2) + ") to (" + 
      str(x_0) + ", " + str(y_0) + ") is " + str(point_distance_c_to_a(x_2, y_2, x_0, y_0)) + " cm.")




# now calculating the area of a triangle given the distances: 


###################################################
# side a : A
# side b : B 
# side c : C
# semi-perimeter:  s = (a + b + c) / 2

def calculateAreaTriangle(a,b,c):
   
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c))**(1/2)
    return area

#Semi-perimeter:  s = (a + b + c) / 2
#Area of a triangle:  area = (s*(s-a)*(s-b)*(s-c))**(1/2)
print("--------------------------------------------")
print("------------------ x1y1(b) -----------------")
print("-------------------*----*-------------------")
print("-----------------*--------*-----------------")
print("---------------*------------*---------------")
print("------------ S1 -------------- S2 ------------")
print("-----------*--------------------*-----------")
print("---------*------------------------*---------")
print("-------*----------------------------*-------")
print("-----*--------------------------------*-----")
print(" x0y0(a) -*---*---*--- S3 ---*---*----x2y2(c)")
print("--------------------------------------------")
print("--------------------------------------------")
print("\n")

# asigning the distances of the sides from the coordenates:
S1 = point_distance_a_to_b(x_0, y_0, x_1, y_1)
S2 = point_distance_b_to_c(x_1, y_1, x_2, y_2)
S3 = point_distance_c_to_a(x_2, y_2, x_0, y_0)
areaOfTriangle = calculateAreaTriangle(S1,S2,S3)

print("The area of the triangle is:", areaOfTriangle, "cm²\n")


###################################################
# Tests
# Student should not change this code.




###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.
