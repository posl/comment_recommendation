def calc(n, r):
    if n < r:
        return 0
    if n == r:
        return 1
    if n > r:
        return calc(n-1, r) + calc(n-1, r-1)

if __name__ == '__main__':
    calc()