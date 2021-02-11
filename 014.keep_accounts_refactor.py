import os
def read_file(file_name):
    list = []
    with open(file_name, 'r', encoding = 'utf-8') as f:
        for line in f:
            if 'Item, Price' in line:
                continue                                                                                                                                                                                                                                                                                                                                                                                    
            item, price = line.strip().split(',')
            list.append([item, price])
    return list    

def user_input(list):
    while True:
        item = input('Enter the product name. ')
        if item == 'q':
            break
        price = input('Enter the price of the product. ')
        list.append([item, price])
    return list

def print_list(list):
    for i in list:
        print('The price of', i[0], 'is', i[1], '.')

def write_file(file_name, list):
    with open(file_name, 'w', encoding = 'utf-8') as f:
        f.write('Item, Price\n')
        for i in list:
    	    f.write(i[0] + ', ' + i[1] + '\n')

def main():
    file_name = '012.my_accounts.csv'
    if os.path.isfile(file_name):
        print('File opened')
        list = read_file('012.my_accounts.csv')
    else:
        print('No record found.')
    list = user_input(list)
    print_list(list)
    write_file('012.my_accounts.csv', list)

main()