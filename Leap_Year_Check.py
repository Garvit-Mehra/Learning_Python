def isLeap_year(year):
    if (year%4 ==0 and year%100 != 0) or (year%400 == 0):
        return True

year = int(input("Enter a year: "))
if isLeap_year(year):
    print (f"{year} is a leap year")
else:
    print (f"{year} is not a leap year")