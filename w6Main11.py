years=raw_input("input year: ")
year=float(years)

def leapYear(year):
    if (year%4==0) and (year%100!=0 or year%400==0):
        res="leap year"
    else:
        res="not leap year"
    return res

res=leapYear(year)
leapYear(year)