def f(x):
    if x == 0:
        return 1
    elif x == 1:
        return 2
    elif x == 2:
        return 3
    else:
        return f(x//2) + f(x//3)
N = int(input())
print(f(N))
