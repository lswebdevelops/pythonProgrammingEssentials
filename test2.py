x_0, y_0, x_1, y_1, x_2, y_2 = 2, 2, 5, 6, 7, 2
# distance x0 > x1
def point_distance_a_b(x_0, y_0, x_1, y_1):
    """
    Returns the Euclidian distance between two points (x0,y0) and (x1,y1).
    """
    
    return ((x_0 - x_1) ** 2 + (y_0 - y_1) ** 2) ** 0.5
print("distance from a to b")
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance_a_b(x_0, y_0, x_1, y_1)) + ".")