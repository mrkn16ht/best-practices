number = int(input('Please input number (n): '))
column=number*2-1
for a in range (0, number):
    starleft=number-1-a
    starright=number-1+a
    for b in range (0, column):
        if b==starleft or b==starright:
            print (end='*')
        else:
            print (end=' ')
    print()
