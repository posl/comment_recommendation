def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 4
    elif n == 5:
        return 7
    elif n == 6:
        return 12
    else:
        return f(n-1) + f(n-2) + f(n-3) + f(n-4) + f(n-5) + f(n-6)
L = int(input())
print(f(L+1))
