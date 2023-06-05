def calSnow(a, b):
    return int((b - a) * (b - a + 1) / 2 - a)
a, b = map(int, input().split())
print(calSnow(a, b))
