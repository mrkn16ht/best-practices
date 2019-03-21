number=int(input("Enter maximum number: "))
prime=[]

for a in range(2,number+1):
    factor=0
    for i in range(2,a//2+1):
        if(a%i==0):
           factor=factor+1 
    if(factor<=0):
        prime.append(a)

print(number, '-> ', end='')
print(*prime)
