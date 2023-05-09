def calc(x, y, n):
    if n == 1:
        return 0
    elif n == 2:
        return x + y
    else:
        return calc(x, y, n-1) + calc(x, y, n-2)
n, x, y = map(int, input().split())
print(calc(x, y, n))

if __name__ == '__main__':
    calc()