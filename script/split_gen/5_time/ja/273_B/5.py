def rounding(x, k):
    for i in range(k):
        if x % 10 == 0:
            x //= 10
        else:
            x += 10 - (x % 10)
    return x
x, k = map(int, input().split())
print(rounding(x, k))
