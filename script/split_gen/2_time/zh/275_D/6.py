def f(x):
    if x == 0:
        return 1
    else:
        return f(x//2) + f(x//3)
n = int(input())
print(f(n))
