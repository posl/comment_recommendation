def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 0
    if n == 3:
        return 1
    return f(n-1) + f(n-3)
s = int(input())
print(f(s)%1000000007)
