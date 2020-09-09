# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

# month = input('Enter the month of the year (Jan - Dec): ')
# if len(month) > 3:
#   month = input('Please enter the abbreviation of the month (Jan - Dec): ')
# day = int(input('Enter the day of the month: '))
# if day < 0 or day > 31:
#   day = int(input('Please enter an actual date: '))
# if month in ('Dec') and day >= 21:
#   season = 'Winter'
# elif month in ('Jan', 'Feb'):
#   season = 'Winter'
# elif month in ('Mar') and day <= 19:
#   season = 'Winter'
# elif month in ('Mar') and day >= 20:
#   season = 'Spring'
# elif month in ('Apr', 'May'):
#   season = 'Spring'
# elif month in ('Jun') and day <= 20:
#   season = 'Spring'
# elif month in ('Jun') and day >= 21:
#   season = 'Summer'
# elif month in ('Jul', 'Aug'):
#   season = 'Summer'
# elif month in ('Sep') and day <= 21:
#   season = 'Summer'
# elif month in ('Sep') and day >= 22:
#   season = 'Fall'
# elif month in ('Oct', 'Nov'):
#   season = 'Fall'
# elif month in ('Dec') and day <= 20:
#   season = 'Fall'
# else: 
#   print(f'{month} does not seem to exist')
# print(f'{month} {day} is in {season}')



month = input('Enter the month of the year (Jan - Dec): ')
if len(month) > 3:
  month = input('Please enter the abbreviation of the month (Jan - Dec): ')
day = int(input('Enter the day of the month: '))
if day < 0 or day > 31:
  day = int(input('Please enter an actual date: '))
if month in ('Jan', 'Feb') or month in ('Dec') and day >= 21 or month in ('Mar') and day <= 19:
  season = 'Winter'
elif month in ('Mar') and day >= 20 or month in ('Apr', 'May') or month in ('Jun') and day <= 20:
  season = 'Spring'
elif month in ('Jun') and day >= 21 or month in ('Jul', 'Aug') or month in ('Sep') and day <= 21:
  season = 'Summer'
elif month in ('Sep') and day >= 22 or month in ('Oct', 'Nov') or month in ('Dec') and day <= 20:
  season = 'Fall'
else: 
  print(f'{month} does not seem to exist')
print(f'{month} {day} is in {season}')







  



