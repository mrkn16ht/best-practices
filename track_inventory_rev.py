import json
import csv
from pathlib import Path
        
def big_menu():
    print('This is a simple inventory tracker program.\n')
    print('What do you want to do?')
    print('1 - View all of your existing inventory')
    print('2 - Add new inventory')
    print('3 - Find your inventory & print out')
    print('4 - Exit this program')
    input_menu()
    
def input_menu():
    checkmenu = '0'
    while checkmenu != '1' or checkmenu != '2' or checkmenu != '3' or checkmenu != '4':
        checkmenu = input('\nPlease select 1 / 2 / 3 / 4 : ')
        if checkmenu == '1':
            print_all_inv()
            small_menu()         
        elif checkmenu == '2':
            add_inv()
            break
        elif checkmenu == '3':
            find_inv()
            break
        elif checkmenu == '4':
            exit_inv()
            break
    
def small_menu():
    print('\nAnything else do you want to do?')
    print('1 - View all of your existing inventory')
    print('2 - Add new inventory')
    print('3 - Search your inventory & print out')
    print('4 - End this program')

def print_all_inv():
    file_name = Path('my_invent.csv')
    if file_name.is_file():
        print('\nPlease check your inventory: \n')
        with open('my_invent.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                print(f'Name: {row["Name"]}, Serial Number: {row["Serial Number"]}, Value: {row["Value"]}')
    else:
        print('\nYou don\'t have any inventory, please add new inventory first.' )

def exist_inv_to_dict():       
    file_name = Path('my_invent.csv')
    if file_name.is_file():
        with open('my_invent.csv') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
            for row in reader:
                inventory['Name'].append(row[0])
                inventory['Serial Number'].append(row[1])
                inventory['Value'].append(row[2])
    else:
        pass

def add_inv():
    exist_inv_to_dict()
    name = '0'
    add_again = '0'
    while name != '':
        name = input('\nPlease enter the name. Leave blank and enter to cancel.\n')
        if name != '':
            serial = (input('Please enter the serial number of your inventory?\n'))
            value=(float(input('Please enter numeric data for the estimated value of your inventory?\n')))
            inventory['Serial Number'].append(serial)
            inventory['Name'].append(name)
            inventory['Value'].append(value)
            file_name = Path('my_invent.csv')
            if file_name.is_file():
                with open('my_invent.csv', 'a+') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([name, serial, value])
            else:
                fieldnames = ['Name','Serial Number', 'Value']
                with open('my_invent.csv', 'w') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(fieldnames)
                    writer.writerow([name, serial, value])
            add_again = '0'
            while add_again != '1' or add_again != '2':
                add_again = input('Do you want to continue adding?\nPlease enter 1 for Yes or 2 for No? ')
                if add_again == '1':
                    add_inv()
                    break
                elif add_again == '2':
                    small_menu()
                    input_menu()
                    break
        else:
            exit_inv()
        break

def find_inv():
    file_name = Path('my_invent.csv')
    if file_name.is_file():
        with open('my_invent.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            print('\nHow do you want to find your inventory?')
            print('1 - By name?')
            print('2 - By serial number?')
            print('3 - By value?')
            find='0'
            while find != '1' or find != '2' or find != '3':
                find = input('\nPlease select 1 / 2 / 3 : ')    
                if find == '1':
                    find_name = input('\nPlease enter the name. Leave blank and enter to cancel.\n')
                    a = False
                    for row in reader:
                        if row['Name'] == find_name:
                            a=True
                            print(f'Name: {row["Name"]}, Serial Number: {row["Serial Number"]}, Value: {row["Value"]}')
                    if find_name != '' and a == False:
                        print('You don\'t have this item.')
                    find_again()
                    break

                if find == '2':
                    find_serial = input('\nPlease enter the serial number. Leave blank and enter to cancel.\n')
                    a=False
                    for row in reader:
                        if row['Serial Number'] == find_serial:
                            a=True
                            print(f'Name: {row["Name"]}, Serial Number: {row["Serial Number"]}, Value: {row["Value"]}')
                    if find_serial != '' and a == False:
                            print('You don\'t have this item.')
                    find_again()
                    break

                if find == '3':
                    find_value = (input('\nPlease enter the value. Leave blank and enter to cancel.\n'))
                    a=False
                    for row in reader:
                        if row['Value'] == find_value:
                            a=True
                            print(f'Name: {row["Name"]}, Serial Number: {row["Serial Number"]}, Value: {row["Value"]}')
                    if find_value != '' and a == False:
                            print('You don\'t have this item.')
                    find_again()
                    break
    else:
        print('\nYou don\'t have any inventory, please add new inventory first.' )
        small_menu()
        input_menu()

def find_again():
    find_again = '0'
    while find_again != '1' or add_again != '2':
        find_again=input('\nDo you want to find any other inventory?\nPlease enter 1 for Yes or 2 for No? ')
        if find_again == '1':
            find_inv()
            break
        elif find_again == '2':
            small_menu()
            input_menu()
            break
            
def exit_inv():
    print('\nThank you for using this program.')

inventory={}
inventory.setdefault('Name', [])
inventory.setdefault('Serial Number', [])
inventory.setdefault('Value', []) 
big_menu()

##uncomment to save to my_invent.json
##exist_inv_to_dict()
##with open('my_invent.json', 'w') as json_file:
##    json.dump(inventory, json_file)
