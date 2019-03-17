i=1
counter=1
while(i<=100):
    if counter%20==1:
        print('\n')
    if i%15==0:
        print('FizzBuzz', end=' ')
    elif i%3==0:
        print('Fizz', end=' ')
    elif i%5==0:
        print('Buzz', end=' ')
    else:
        print(i, end=' ')
    i+=1
    counter+=1
