"""
Template - Compute and print tens and ones digit of an integer in [0,100).
"""

###################################################
# Digits function
# Student should enter function on the next lines.


#number divided per 10 show it's ten:
# 34 // 10 = 3

#the module 10 of  a number is its one digit
#34 % 10 = 4

def print_digits():
    number = input("Enter your number from 1 to 99: ")
    print("Your number is:", number)
    r = int(number) // 10
    m = int(number) %10
    print("When using the number: " + str(number) + ", the tens digit is: " + str(r) + " and the ones digit is: " + str(m) +".")






###################################################
# Tests
# Student should not change this code.
    
print_digits()



###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.
