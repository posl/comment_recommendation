def f(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return f(x-1) + f(x-2)
