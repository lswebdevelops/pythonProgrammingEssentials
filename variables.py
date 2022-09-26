"""
Demonstration of the use of variables and how to assign values to
them.
"""

# The = operator can be used to assign values to variables
from audioop import mul
from math import remainder


bakers_dozen = 12 + 1
temperature = 93

# Variables can be used as values and in expressions

print(temperature, bakers_dozen)
print("Celsius: " , (temperature -32) * 5/9)
print("Fahernheit: ", float(temperature))
# You can assign a different value to an existing variable
temperature = 26
print("new value: ", temperature)
 
# Multiple variables can be used in arbitrary expressions

offset = 32

multiplier = 5.0  / 9.0
celsius  = ( temperature - offset) * multiplier
print("Celsius value: ", celsius)