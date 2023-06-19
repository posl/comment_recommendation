def nearest_10_pow(x, k):
    for i in range(k):
        if x % (10 ** (i+1)) == 0:
            continue
        else:
            x = x + 10 ** (i+1) - x % (10 ** (i+1))
    return x
x, k = map(int, input().split())
print(nearest_10_pow(x, k))
