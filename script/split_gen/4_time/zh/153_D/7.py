def func(h):
    if h == 1:
        return 1
    else:
        return 2 * func(int(h / 2)) + 1
h = int(input())
print(func(h))
