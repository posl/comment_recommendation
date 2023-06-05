def f(n):
    if n == 1:
        return [1]
    else:
        a = f(n-1)
        return a + [n] + a
n = int(input())
print(*f(n))
