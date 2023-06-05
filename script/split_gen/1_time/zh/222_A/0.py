def print_4digits(num):
    if num < 10:
        print('000' + str(num))
    elif num < 100:
        print('00' + str(num))
    elif num < 1000:
        print('0' + str(num))
    else:
        print(str(num))
