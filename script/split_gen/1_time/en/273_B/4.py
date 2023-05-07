def rounding(x, k):
    if k == 0:
        return x
    else:
        return rounding(round(x, -k), k-1)
x, k = map(int, input().split())
print(rounding(x, k))
