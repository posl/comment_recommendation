def rec(n):
    if n == 1:
        return [1]
    else:
        return rec(n-1) + [n] + rec(n-1)
n = int(input())
print(*rec(n))
