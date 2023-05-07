def round_off(x, k):
    for i in range(k):
        if x % 10 != 0:
            x += 10 - x % 10
    return x
x, k = map(int, input().split())
print(round_off(x, k))
