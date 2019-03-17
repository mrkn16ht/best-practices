number = int(input('Please input number (n): '))
column=number
for a in range (0, number):
    for b in range (0, column):
        if b==a or number-1-b==a:
            print (end='*')
        else:
            print (end=' ')
    print()
