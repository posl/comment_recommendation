def floor(x):
    if x >= 0:
        return int(x)
    else:
        return int(x) - 1
print(floor(int(input()) / 10))
