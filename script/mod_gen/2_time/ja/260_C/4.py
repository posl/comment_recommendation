def calc(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x
    if n == 3:
        return x + y
    return calc(n - 1, x, y) + calc(n - 2, x, y)
n, x, y = map(int, input().split())
print(calc(n, x, y))

if __name__ == '__main__':
    calc()