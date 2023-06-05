def f(n):
    if n == 1:
        return [1]
    else:
        s = f(n-1)
        return s + [n] + s
n = int(input())
print(*f(n))
