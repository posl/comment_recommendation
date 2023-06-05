def calc(x, k, d):
    if x < 0:
        x = -x
    if x >= k * d:
        return x - k * d
    else:
        y = x % d
        if (k - x // d) % 2 == 0:
            return y
        else:
            return d - y
x, k, d = map(int, input().split())
print(calc(x, k, d))
