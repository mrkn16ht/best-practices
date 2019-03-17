**Easy 1**
Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

**Example Output:**
```
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz
Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz
41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz
61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz
Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz
```
**Answer (check easy1.py)**
```python
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
```
**Easy 2**
Write a program that determine whether or not an integer input is a leap year.

Definition of leap year:
* Rule 1: A year is called leap year if it is divisible by 400.

Example: 1600, 2000 etc. are leap year while 1500, 1700 are not leap year.

* Rule 2: If year is not divisible by 400 as well as 100 but it is divisible by 4 then that year are also leap year.

Example: 2004, 2008, 1012 are leap year.

**Example Output:**
```
1600 -> true
2000 -> true
1500 -> false
2004 -> true
2008 -> true
2010 -> false
```
**Answer (check easy2.py)**

```python
year = int( input ('Please input the year: '))
if year%400==0:
    print(year, '-> true')
elif year%400!=0 and year%100!=0 and year%4==0:
    print(year, '-> true')
else:
    print(year, '-> false')
```
**Easy 3.1**
Write a program that produce the following output giving an integer input n.

**Example Output:**
```
n=3   n=4    n=6
*     *      *
**    **     **
***   ***    ***
      ****   ****
             *****
             ******
```
**Answer (check easy3_1.py)**
```python
number = int(input('Please input number (n): '))
for i in range(number):
    print('*' * (i+1))
```

**Easy 3.2**
Write a program that produce the following output giving an integer input n.

**Example Output:**
```
n=3    n=4      n=6
  *      *        *
 **     **       **
***    ***      ***
      ****     ****
              *****
             ******
```
**Answer (check easy3_2.py)**
```python
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
```

