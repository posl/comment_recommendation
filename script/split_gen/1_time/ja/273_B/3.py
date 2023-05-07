def round(x, k):
    for i in range(k):
        x = (x + 10 ** i - 1) // (10 ** i) * (10 ** i)
    return x
x, k = map(int, input().split())
print(round(x, k))
