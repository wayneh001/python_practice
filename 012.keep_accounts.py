products = []

while True:
    item = input('Enter the product name.')
    if item == 'q':
    	break
    price = input('Enter the price of the product.')
    products.append([item, price])
print(products)

products[0][0]