def meanArterialPressure(a, b):
    c = (a - b) / 3 + b
    return c
a, b = map(int, input().split())
print(meanArterialPressure(a, b))
