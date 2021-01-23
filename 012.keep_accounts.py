# File open
list = []
with open('012.my_accounts.csv', 'r', encoding = 'utf-8') as f:
    for line in f:
    	if 'Item, Price' in line:
    		continue                                                                                                                                                                                                                                                                                                                                                                                    
    	item, price = line.strip().split(',')
    	list.append([item, price])

# User key-in
while True:
    item = input('Enter the product name. ')
    if item == 'q':
    	break
    price = input('Enter the price of the product. ')
    list.append([item, price])

# Key-in result print
for i in list:
    print('The price of', i[0], 'is', i[1], '.')
    
# File save
with open('012.my_accounts.csv', 'w', encoding = 'utf-8') as f:
    f.write('Item, Price\n')
    for i in list:
    	f.write(i[0] + ', ' + i[1] + '\n')