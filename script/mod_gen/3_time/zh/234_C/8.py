def findk(k):
    n = 1
    while True:
        if n == 1:
            if k == 1:
                return 2
            else:
                k -= 1
                n += 1
        else:
            if k <= 2 ** (n - 1):
                n -= 1
            else:
                k -= 2 ** (n - 1)
                n += 1

if __name__ == '__main__':
    findk()