#Problem6
def is_leap(year):
    return (year%4==0 and year%100!=0 )or( year%400==0)
def days_in_month(month,year):
    if month<1 or month>12:
        return None
    if month==2:
        if is_leap(year):
            return 29
        else:
            return 28
    elif month in[4,6,9,11]:
        return 30
    else: 
        return 31
for year in [1900,2000,2024,2026]: 
    if is_leap(year):
        print(year,"is leap year")
    else:
        print(year,"is not leap year")

print("Feb 2024:",days_in_month(2,2024),"|Feb 2026:",days_in_month(2,2026),
      "|Apr:",days_in_month(4,2024),"|month13:",days_in_month(13,2024))
leap_years=[]
for year in range(2000,2100):
    if is_leap(year):
        leap_years.append(year)
print("Leap year from 2000 to 2021: "+str(len(leap_years)))