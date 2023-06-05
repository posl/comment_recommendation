def f(n,s):
    if n == 0:
        return 1 if s == 0 else 0
    elif n > s:
        return f(n-1,s)
    else:
        return f(n-1,s) + f(n,s-n)
print(f(2000,2000))
