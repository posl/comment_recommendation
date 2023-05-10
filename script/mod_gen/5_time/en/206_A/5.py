def problem206_a():
    N = int(input())
    price = int(1.08*N)
    if price < 206:
        print('Yay!')
    elif price == 206:
        print('so-so')
    else:
        print(':(')

if __name__ == '__main__':
    problem206_a()