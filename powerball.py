"""
Template - Compute and print powerball numbers.
"""

import random

###################################################
# Powerball function
# Student should enter function on the next lines.
def powerball():

    numbers = random.sample(range(1,60), 6)
    
    theFive = numbers
   
    number1          = theFive[0]
    number2          = theFive[1]
    number3          = theFive[2]
    number4          = theFive[3]
    number5          = theFive[4]

    powerball_number = random.sample(range(1,36), 1)

    print("\nYour numbers are: " +  str(number1) + ", "+  str(number2) +  ", "+ str(number3) +  ", "+ str(number4) + " and "+   str(number5) + ".")

    print("Your Power Ball number is: " + str(powerball_number[0]) + ".\n")
   
    

    

    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()


###################################################################
# Some sample output appears below.  Note that numbers need not match
#Today's numbers are 46, 25, 49, 54, and  8. The Powerball number is 26.
#Today's numbers are 14, 11, 17, 6, and  30. The Powerball number is 16.
#Today's numbers are 58, 59, 39, 2, and  29. The Powerball number is 19.
