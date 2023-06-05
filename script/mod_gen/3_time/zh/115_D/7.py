def f(n,x):
    if n == 0:
        return 0
    elif x == 1:
        return 0
    elif x <= 1 + (2 ** n - 1) // 2:
        return f(n - 1, x - 1)
    elif x == 2 + (2 ** n - 1) // 2:
        return 1 + (2 ** n - 1) // 2
    elif x <= 2 + (2 ** n - 1):
        return 1 + (2 ** n - 1) // 2 + f(n - 1, x - 2 - (2 ** n - 1) // 2)
    else:
        return 1 + 2 * (2 ** n - 1)
n,x = map(int,input().split())
print(f(n,x))
