def multiply(a, b):
    if a == 0 or b == 0:
        return 0
    elif a > 10**18 or b > 10**18:
        return -1
    else:
        return a * b

if __name__ == '__main__':
    multiply()