def func(n):
    if n == 1:
        return [1]
    else:
        a = func(n-1)
        return a + [n] + a
n = int(input())
print(*func(n))
