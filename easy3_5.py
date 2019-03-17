number = int(input('Please input number (n): '))
if number%2==0:
    column=number-1
else:
    column=number-0
center =int((number-((3)+(-1)**number)/2)/2)
for a in range (0, number-center):
    for b in range (0, column):
        if center+a >=b>=center-a:
            print(end='*')
        else:
            print(end=' ')
    print()
for a in range (center-1, -1, -1):
    for b in range (0, column):
        if center-a<=b<=center+a:
            print(end='*')
        else:
            print(end=' ')
    print()
