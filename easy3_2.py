number = int(input('Please input number (n): '))
blank=number-1
star=1
for a in range (0, number):
    for b in range (0, blank):
        print(end=' ')
    blank-=1
    for c in range (0, star):
        print('*', end='')
    star+=1
    print()
