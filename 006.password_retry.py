true_password = 'a123456'
i = 2
while i >= 0:
    password = input('Please enter the password ')
    if password == true_password:
        print('Weclome to login.')
        break
    elif password != true_password:
        print('Wrong password, you have', i, 'times to try.')
        i = i - 1
        if i < 0:
            print('Try again later.')
            break