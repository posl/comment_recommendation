def a(n):
    if n == 1:
        return [1]
    else:
        return a(n-1) + [n] + a(n-1)
N = int(input())
print(*a(N))
