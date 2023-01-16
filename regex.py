import re 

dateRegex = re.compile(r'''(
    (\d{2}) #day
    (/)
    (\d{2}) #month
    (/)
    (\d{4}) #year
    )''', re.VERBOSE
)
day = '' 
month = ''
year = '' 

#MonthBool
isLeapYear = False
isFebuary = False
is30days = False
isMonthValid = False

#DayBool
isDayValid = False

#YearBool
isYearValid = False

#DateBOOL
isDateValid = False

for group in dateRegex.findall('29/02/2000'):
    day = group[1]
    month = group[3]
    year = group[5]


#Boolinfos
#if int(year)%4 == 0 :
#    isLeapYear = True
#
#elif int(year)%100 == 0:
#    if int(year)%400 ==0 :
#        isLeapYear = False
#    else:
#        isLeapYear = True

if int(year)%400 == 0:
    isLeapYear = False
elif int(year)%100 == 0:
    isLeapYear = True
elif int(year)%4 == 0:
    isLeapYear = True

if int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
    is30days = True

if int(month) == 2:
    isFebuary = True



#isDayValid 
if is30days and int(day) < 30:
    isDayValid = True

if isFebuary:
    if isLeapYear:
        if int(day) <= 29 :
            isDayValid = True
        else:
            isDateValid = False
    else :
        if int(day) <=28 :
            isDayValid = True
        else:
            isDateValid = False
elif int(day) <= 31:
    isDayValid = True

#isMonthValid 
isMonthValid = (int(month) <= 12 and int(month) >=1)
isYearValid =(int(year) >= 1000 and int(month) <= 2999)
isDateValid = (isDayValid and isYearValid and isMonthValid)


print(isLeapYear)
print(isFebuary)
print(is30days)
print("##############################")
print(isDayValid)
print(isMonthValid)
print(isYearValid)
print(isDateValid)
print('##############################')
print(day)
print(month)
print(year)