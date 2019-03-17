def checktasks ():
    with open("todolistnew.txt", "r") as todo_file:
        print('Please check your tasks: ', todo_file.name)
        tasks=todo_file.read()
        print(tasks)

def checkinput1():
    if check_input=='1':
        checktasks()
        print('Thank you')
        

def checkinput2():
    if check_input=='2':
        task_input=0
        while task_input!='':
            task_input=input('Please input your tasks. Leave blank and enter if finished: ')
            with open("todolistnew.txt", "a+") as todo_file:
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


