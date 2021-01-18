import random
start = input('Set the start number. ')
end =  input('Set the end number. ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
    count += 1
    num = input('Guess a number. ')
    num = int(num)
    if num == r:
    	print(count, 'times guess. You got it!')
    	break
    elif num > r:
    	print('Try a smaller one.')
    elif num < r:
    	print('Try a bigger one.')
    print(count, 'times guess.')