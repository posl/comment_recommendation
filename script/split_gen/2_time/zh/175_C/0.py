def abs(x):
    if x >= 0:
        return x
    else:
        return -x
x, k, d = map(int, input().split())
x = abs(x)
