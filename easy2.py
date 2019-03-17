year = int( input ('Please input the year: '))
if year%400==0:
    print(year, '-> true')
elif year%400!=0 and year%100!=0 and year%4==0:
    print(year, '-> true')
else:
    print(year, '-> false')
