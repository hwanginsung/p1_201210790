def sumOfMultiple3_5(begin,end):
    sum=0
    for i in range(begin,end):
        if (i%3==0 or i%5==0):
            sum=sum+i
    print sum
    return sum

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

def lab6():
    sumOfMultiple3_5(0,1001)
    leapYear()

def main():
    lab6()

if __name_=="__main__":
    main()

raw_input()