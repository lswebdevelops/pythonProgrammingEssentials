
import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if year > datetime.MINYEAR:   

      if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days_of_month = 31
        return days_of_month
      elif month == 2:
        days_of_month = 28
        return days_of_month

      elif month == 4 or month == 6 or month == 9 or month == 11:
        days_of_month = 30
        return days_of_month

    return 0



print(days_in_month(1986,1))