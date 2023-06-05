def calc(n):
    if n == 1:
        return 1
    else:
        return 10**(n-1) + 9*calc(n-1)

if __name__ == '__main__':
    calc()