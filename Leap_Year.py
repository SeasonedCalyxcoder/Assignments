# Defining a function is_leap with one argument year
def is_leap(year):
    # Assumption is that the year is not a leap year
    leap = False
    # Checking if the year is divisible by 4
    if (year % 4 == 0):
        # Checking if the year is not divisible by 100 or divisible by 400
        if (year % 100 != 0) or (year % 400 == 0):
            # If conditions above are true, it is a leap year
            leap = True
    # If the year is a leap year, it will return true. If otherwise, false
    return leap
#Prompt the user to enter a year
year = int(input("Enter a year: "))
#Calling the function with the user input and printing the result
print(is_leap(year))