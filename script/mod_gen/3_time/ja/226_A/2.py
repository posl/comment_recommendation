def rounding(x):
    x = x * 10
    x = int(x)
    if x % 10 >= 5:
        x = int(x / 10) + 1
    else:
        x = int(x / 10)
    return x
print(rounding(float(input())))
