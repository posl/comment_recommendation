def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    elif n == 2:
        return 0
    elif n == 3:
        return 1
    else:
        return f(n-1) + f(n-3)
s = int(input())
print(f(s)%(10**9+7))
