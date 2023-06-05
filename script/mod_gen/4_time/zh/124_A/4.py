def max_coin(a, b):
    if a < b:
        return b + b - 1
    elif a > b:
        return a + a - 1
    else:
        return a + b

if __name__ == '__main__':
    max_coin()