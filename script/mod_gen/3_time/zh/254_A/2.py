def print_last_two_digits(num):
    if num > 99 and num < 1000:
        print(str(num)[-2:])
    else:
        print('error')

if __name__ == '__main__':
    print_last_two_digits()