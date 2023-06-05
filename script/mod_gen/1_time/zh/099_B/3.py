def snow(a, b):
    total = (b - a + 1) * (a + b) // 2
    return total - b
print(snow(8, 13))
print(snow(54, 65))
