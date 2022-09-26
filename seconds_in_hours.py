"""
Template - Compute the number of seconds in a given number of hours, minutes, and seconds.
"""
# Write a Python statement that calculates and prints the number of seconds in 7 hours, 21 minutes and 37 seconds
###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter statement on the next line.

number_of_hours = 7
number_of_minutes  = 21
number_of_seconds = 37

secs_in_hours = number_of_hours * 60 * 60
secs_in_minutes = number_of_minutes * 60

total_number_seconds = number_of_seconds + secs_in_hours + secs_in_minutes

print("There are", total_number_seconds, "seconds in", number_of_hours, "hours", number_of_minutes, "minutes and ",number_of_seconds, "seconds.")
print("There are " + str(total_number_seconds) +  " seconds in " +  str(number_of_hours) +  " hours " +  str(number_of_minutes) +  " minutes and "   + str(number_of_seconds) +  " seconds.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#26497