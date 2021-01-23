products = []

while True:
    item = input('Enter the product name. ')
    if item == 'q':
    	break
    price = input('Enter the price of the product. ')
    products.append([item, price])

for i in products:
    print('The price of', i[0], 'is', i[1], '.')
    
with open('012.my_accounts.csv', 'w') as f:
    for i in products:
    	f.write(i[0] + ', ' + i[1] + '\n')