number = int(input('Please input number (n): '))
column=number*2-1
center=number-1

for a in range (0, center+1):
    for b in range (0, column):
        if b==center-a or b==center+a:
            print(end='+')
        elif a+b<=center-1:
            print(end='A')
        elif b-a>center:
            print(end='B')
        else:
            print(end='E')
    print()
    
for a in range (center-1, -1, -1):
    for b in range (0, column):
        if b==center-a or b==center+a:
            print(end='+')
        elif b<center-a:
            print(end='C')
        elif b>center+a:
            print(end='D')
        else:
            print(end='E')
    print()
