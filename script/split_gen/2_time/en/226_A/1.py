def round_to_nearest_int(x):
    if x % 1 >= 0.5:
        return int(x) + 1
    else:
        return int(x)
x = float(input())
print(round_to_nearest_int(x))
