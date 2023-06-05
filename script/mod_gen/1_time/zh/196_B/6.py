def round_up(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)
x = float(input())
print(round_up(x))
