import random
r = random.randint(1, 100)
while True:
    num = input('Guess a number from 1 to 100. ')
    num = int(num)
    if num == r:
    	print('You got it!')
    	break
    elif num > r:
    	print('Try a smaller one.')
    elif num < r:
    	print('Try a bigger one.')