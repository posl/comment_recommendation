def func(h):
    if h == 1:
        return 1
    elif h == 0:
        return 0
    else:
        return 2*func(h//2) + 1
h = int(input())
print(func(h))
