"""
Demonstration of importing modules.
"""

# Import the math module (look in the Docs for help)
import math
# you could say> import math as count and do that below:  print(count.pi) // 3.14159... instead of print(math.pi)// 3.14159



# Constants
print("Math constants")
print("==============")
print(math.pi)
print(math.e)
print("")

# Functions
print("Math functions")
print("==============")
print(math.sqrt(25))
print(math.trunc(14.83483))
print(math.sin(math.pi / 2.0))
print("")

# # Dir
print("Dir")
# print("===")
# print(dir(math))
# print(dir(example))
# print("")


# Import example module
import examples3_module as example


print(example.message)
# print(math.__name__)
print(example.__name__)
print(example.name)
