def f(n):
    if n < 3:
        return 0
    elif n == 3:
        return 1
    else:
        return f(n-1) + f(n-3)
S = int(input())
print(f(S) % (10**9 + 7))
