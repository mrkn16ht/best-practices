**Todo List**
Let’s start with the good-old trusty todo list, the “Hello, World” of full programs. You’re going to write a command-line todo list program that meets the following specifications:

1. Prompt the user to enter a chore or task. Store the task in a permanent location so that the task persists when the
   program is restarted.
2. Allow the user to enter as many tasks as desired but stop entering tasks by entering a blank task. Do not store the blank
   task.
3. Display all the tasks.
4. Allow the user to remove a task, to signify it’s been completed.
5. Persist todos to Redis

**Answer: todolist.py**
```python
def checktasks():
    with open('todolistnew.txt', 'r+') as todo_file:
        print('Please check your tasks: ', todo_file.name)
        tasks=todo_file.read()
        print(tasks)

def checkinput1():
    if check_input=='1':
        checktasks()
        print('Thank you')
        
def checkinput2():
    if check_input=='2':
        task_input='0'
        while task_input!='':
            task_input=input('Please input your tasks. Leave blank and enter if finished: ')
            with open('todolistnew.txt', 'a+') as todo_file:
                todo_file.write('* '+task_input+'\n')
            if task_input=='':
                lines = open('todolistnew.txt').readlines()
                open('todolistnew.txt', 'w').writelines(lines[:-1])
                checktasks()
                print('Thank you')
                break

def checkinput3():
    if check_input=='3':
        checktasks()
        while True:
            delete_input=int(input('Which task line do you want to delete? '))
            with open('todolistnew.txt', 'r') as todo_file:
                lines = todo_file.readlines()
            with open('todolistnew.txt', 'w') as todo_file:
                todo_file.writelines(lines[:delete_input-1] + lines[delete_input:])
            checktasks()
            print('Thank you')
            break
       
def checkinput4():
    if check_input=='4':
        print('Thank you')
    
print('This is a simple to do list program.')
print('What do you want to do?')
print('1 - Check your tasks')
print('2 - Add your tasks')
print('3 - Delete your tasks')
print('4 - End this program')

check_input=input('Please select 1 / 2 / 3 / 4 : ')

checkinput1()

checkinput2()

checkinput3()

checkinput4()

```

**[Easy 1]**
Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

**Example Output:**
```
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz
Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz
41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz
61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz
Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz
```

**Answer: easy1.py**
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

**[Easy 2]**
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

**Answer: easy2.py**
```python
year = int( input ('Please input the year: '))
if year%400==0:
    print(year, '-> true')
elif year%400!=0 and year%100!=0 and year%4==0:
    print(year, '-> true')
else:
    print(year, '-> false')
```

**[Easy 3.1]**
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

**Answer: easy3_1.py**
```python
number = int(input('Please input number (n): '))
for i in range(number):
    print('*' * (i+1))
```

**[Easy 3.2]**
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

**Answer: easy3_2.py**
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

**[Easy 3.3]**
Write a program that produce the following output giving an integer input n.

**Example Output:**
```
n=1    n=2      n=3       n=4       n=5
*       *        *         *         *
       * *      * *       * *       * *
               *   *     *   *     *   *     
                        *     *   *     *
                                 *       *          
```

**Answer: easy3_3.py**
```python
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
```

**[Easy 3.4]**
Write a program that produce the following output giving an integer input n.

**Example Output:**
```
n=1  n=2  n=3    n=4    n=5
 *   **   * *   *  *   *   *
     **    *     **     * *
          * *    **      *  
                *  *    * *
                       *   * 
```

**Answer: easy3_4.py**
```python
number = int(input('Please input number (n): '))
column=number
for a in range (0, number):
    for b in range (0, column):
        if b==a or number-1-b==a:
            print (end='*')
        else:
            print (end=' ')
    print()
```

**[Easy 3.5 (NB Not Easy)]**
Write a program that produce the following output giving an integer input n.

**Example Output: -- Answer check easy3_5.py**
```
*    *     *     *      *          *
     *    ***   ***    ***        ***
           *    ***   *****      *****
                 *     ***      *******
                        *      *********
                                *******
                                 *****
                                  ***
                                   *
                                
n=1  n=2  n=3   n=4    n=5        n=9
```

**Answer: easy3_5.py**
```python
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
```

**[Easy 3.6]**
Write a program that produce the following output giving an integer input n.

**Example Output:**
```
n=1   n=2    n=3       n=4
+     A+B   AA+BB    AAA+BBB
      +E+   A+E+B    AA+E+BB
      C+D   +EEE+    A+EEE+B
            C+E+D    +EEEEE+
            CC+DD    C+EEE+D
                     CC+E+DD
                     CCC+DDD
```

**Answer: easy3_6.py**
```python
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
```

**[Easy 4]**
(Python specific) In Python, what is the difference between else and finally in exception handling?

**Answer**
```
- If Python script in the try block does not raise an exception, any python script in the else block will be executed.
- Whether Python script in the try block raises an exception or not, any code in the finally block will be executed. 
```

**[Medium 1]**
Write a program that finds all prime numbers up to n for input n. 

**Example Output:**
```
20 -> 2 3 5 7 11 13 17 19
```

**Answer: medium1.py**
```python
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
```
