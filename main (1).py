# leap year

"""
year%4==0&
year%==0/
year%400==0

"""
def isleapyear(year):
  if(year % 4 ==0 and year % 100 !=0) or year % 400 ==0:
    return true 
  else:
    return False

year=int(input("enter a year:"))

if isleapyear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is a leap year.'.format(year))
  