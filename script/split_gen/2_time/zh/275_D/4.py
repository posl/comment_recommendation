def f(x):
    if x == 0:
        return 1
    elif x == 1:
        return 2
    elif x == 2:
        return 3
    elif x == 3:
        return 4
    else:
        return f(x//2) + f(x//3)
n = int(input())
print(f(n))
