def func(n):
    if n == 1:
        return 0
    else:
        return 10**(n-1) - 9**(n-1)*2 + 8**(n-1)
n = int(input())
print(func(n)%(10**9+7))
