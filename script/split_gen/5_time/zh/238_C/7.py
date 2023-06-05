def f(n):
    if n < 10:
        return n
    else:
        return f(n - 1) + 1
n = int(input())
print (f(n) % 998244353)
