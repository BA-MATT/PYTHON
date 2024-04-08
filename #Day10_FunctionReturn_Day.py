leap_lear=True

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year")
        return leap_lear is True
      else:
        print("Not leap year")
    else:
      print("Leap year")
      return leap_lear is True
  else:
    print("Not leap year")
  
# TODO: Add more code here 👇
def days_in_month(c_year, c_month):
  n_year = is_leap(c_year)
  if n_year is True:
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[c_month-1]
  else:
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    return month_days[c_month-1]

  
#🚨 Do NOT change any of the code below 
year = int(input("Please enter the year: ")) # Enter a year
month = int(input("Please enter the month: ")) # Enter a month
days = days_in_month(year, month)
print(days)
