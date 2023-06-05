def f(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return f(n-1) + f(n-2) + f(n-3) + f(n-4)
L = int(raw_input())
print f(L)
