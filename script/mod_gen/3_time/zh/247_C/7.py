def func(n):
    if n == 1:
        return [1]
    else:
        return func(n-1) + [n] + func(n-1)
n = int(input())
print(*func(n))
