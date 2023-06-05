def extra_coin(x):
    if x % 100 == 0:
        return 100
    else:
        return 100 - x % 100

if __name__ == '__main__':
    extra_coin()