import json
import csv
        
def menu():
    print('This is a simple inventory tracker program.')
    print('What do you want to do?')
    print('1 - Print out all of your inventory')
    print('2 - Add new inventory')
    print('3 - Search your inventory & print out')
    print('4 - End this program')

def print_all_inv():
    if checkmenu=='1':
        with open('my_invent.json','r+') as json_file:
            inventory = json.load(json_file)
        with open('my_invent.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Name','Serial Number', 'Value'])
            writer.writerow([''.join(item) for item in inventory['Name']])
            writer.writerow([''.join(item) for item in inventory['Serial Number']])
            writer.writerow([item for item in inventory['Value']])
##          need time to find out how to print into column

def add_inv():
    if checkmenu=='2':
        name='0'
        while name!='':
            name=input('Please enter the name. Leave blank and enter to cancel.\n')
            if name!='':
                serial=(input('Please enter the serial number of your inventory?\n'))
                value=int(input('Please enter the estimated value of your inventory?\n'))
                inventory['Name'].append(name)
                inventory['Serial Number'].append(serial)
                inventory['Value'].append(value)
        with open('my_invent.json', 'a+') as json_file:
            json.dump(inventory, json_file)

    
def find_inv():
    if checkmenu=='3':
        with open('my_invent.json','r+') as json_file:
            inventory = json.load(json_file)
        print('How do you want to search your inventory?')
        print('1 - By name?')
        print('2 - By serial number?')
        print('3 - By value?')
        find = input('Please select 1 / 2 / 3 : ')    
        if find=='1':
              find_name=input('Please enter the name. Leave blank and enter to quit this program.\n')
              for item in inventory['Name']:
                  pass
##                  if find_name in item:
##                     need time to find out how to print the item
##                     with open('my_invent.csv', 'w') as csv_file:
##                         writer = csv.writer(csv_file)
##                         writer.writerow(['Name','Serial Number', 'Value'])
##                         for item in inventory.values():
##                             writer.writerow(inventory.item)
##                         writer.writerow([item for item in inventory['Serial Number']])
##                         writer.writerow([item for item in inventory['Value']])
            
        elif find=='2':
            find_serial=input('Please enter the serial number. Leave blank and enter to quit this program.\n')
            for item in inventory['Serial Number']:
                if find_serial in item:
                    pass
##                     need time to find out how to print the item
        elif find=='3':
            find_value=int(input('Please enter the value. Leave blank and enter to quit this program.\n'))
            for item in inventory['Value']:
                if find_value == item:
                    pass
##                     need time to find out how to print the item

inventory={}
inventory.setdefault('Name', [])
inventory.setdefault('Serial Number', [])
inventory.setdefault('Value', [])                    

menu()
checkmenu=input('Please select 1 / 2 / 3 / 4 : ')
add_inv()
find_inv()
print_all_inv()


