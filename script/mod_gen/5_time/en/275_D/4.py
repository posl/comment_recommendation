def f(x):
    if x == 0:
        return 1
    return f(x//2) + f(x//3)
print(f(int(input())))
