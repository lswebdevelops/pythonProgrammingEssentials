"""
Demonstration of parameters and variables within functions.
"""



def fahrenheit_to_celsius(fahrenheit):
    """
    Return celsius temperature that corresponds to jahrenheit temperature input.
    """
    offset = 32
    multiplier = 5/9
    celsius = (fahrenheit - offset) * multiplier
    print("Inside function:", fahrenheit, offset, multiplier, celsius)
    return celsius

temperature = 95

converted = fahrenheit_to_celsius(temperature)

print(temperature, "° degrees Fahrenheit.")
print(converted, "° degrees Celcius" )



