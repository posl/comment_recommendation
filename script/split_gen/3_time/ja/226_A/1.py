def round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)
x = float(input())
print(round(x))
