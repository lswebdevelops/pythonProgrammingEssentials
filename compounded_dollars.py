# Given p dollars, the future value of this money when compounded yearly\
#  at a rate of r percent interest for y years is  p (1 + 0.01 r)^y 

#  .(Remember that you don't need to understand how this formula works, only how \
# to translate it into Python.) Write a Python statement that\
#  calculates and prints the value of 
# 10000 dollars\
#  compounded at 
# 7 percent 
# interest for
#  10 years
"""
Template - Compute the future value of a given present value, annual rate, and number of years.
"""

###################################################
# Future value formula
# Student should enter statement on the next line.

present_value = 1000
annual_rate = 7
years = 10

interest = present_value * ((1 + (0.01 * annual_rate)) ** years)

print(present_value, "dollars compounded in ", years, "years of a", annual_rate, "%"," annual rate would give you $",interest," of interest." )
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#1967.15135729
